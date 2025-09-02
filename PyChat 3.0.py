import nltk # type: ignore
from nltk.chat.util import Chat, reflections # type: ignore
import os
import re
import json
import time
import sys

pairs_file = "pairs.json"

def save_pairs(pairs):
    with open(pairs_file, "w") as file:
        json.dump(pairs, file)

def load_pairs():
    if os.path.exists(pairs_file):
        with open(pairs_file, "r") as file:
            return json.load(file)
    return [
        ['how are you|how are you bro|how r u', ['I am fine, thanks. How are you?']],
        ['i am fine', ['Great to hear that.']],
        ['not actually|nah bro|no|i am sad', ['I am sorry to hear that. What can I do to cheer you up?']],
        ['what is your name', ['I am PyChat 3.0, your Python Chatbot.']],
        ['bye', ['Goodbye!']],
        ['change the username|change username', ['Okay, let\'s change your name. What\'s your new name?']],
        ['delete the username|delete username', ['Username deleted.']],
        ['i want to train you', ['Sure, what input would you like to train me with?']],
        ['start stopwatch', ['Stopwatch started. Press Enter to stop it.']]
    ]

pairs = load_pairs()
chatbot = Chat(pairs, reflections)

def save_user_name(name):
    with open("user_name.txt", "w") as file:
        file.write(name)

def load_user_name():
    if os.path.exists("user_name.txt"):
        with open("user_name.txt", "r") as file:
            return file.read().strip()
    return None

def delete_user_name():
    if os.path.exists("user_name.txt"):
        os.remove("user_name.txt")
        return True
    return False

def is_math_question(user_input):
    # Regular expression to match basic arithmetic expressions
    return re.match(r'^[\d\s\+\-\*/\(\)]+$', user_input)

def add_new_pair(input, response):
    pairs.append([input, [response]])
    save_pairs(pairs)
    print("PyChat: I have learned the new input-response pair.")
    print(f"Debug: New pair added - Input: {input}, Response: {response}")
    global chatbot
    chatbot = Chat(pairs, reflections)

def start_stopwatch():
    return time.time()

def get_elapsed_time(start_time):
    return time.time() - start_time

def delete_all_pairs():
    global pairs
    pairs = []
    save_pairs(pairs)
    global chatbot
    chatbot = Chat(pairs, reflections)
    print("PyChat: All inputs have been deleted.")

def nltk_chatbot():
    user_name = load_user_name()
    stopwatch_start_time = None
    
    if user_name is None:
        user_name = input("PyChat: Hi! What's your name?\nYou: ")
        save_user_name(user_name)
        
    print(f"PyChat: Hi {user_name}, I am PyChat. How can I help you?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("PyChat: Goodbye!")
            time.sleep(2)
            break
        elif user_input.lower() == "change the username":
            user_name = input("PyChat: What's your new name?\nYou: ")
            save_user_name(user_name)
            print(f"PyChat: Hi {user_name}, how can I help you?")
        elif user_input.lower() == "delete the username":
            if delete_user_name():
                print("PyChat: Username deleted.")
                user_name = None
            else:
                print("PyChat: No username to delete.")
        elif is_math_question(user_input):
            try:
                result = eval(user_input)
                print(f"PyChat: The answer is {result}")
            except:
                print("PyChat: Sorry, I couldn't understand the math question.")
        elif user_input.lower() == "i want to train you":
            new_input = input("PyChat: What input would you like to train me with?\nYou: ")
            new_response = input("PyChat: What should be my response to this input?\nYou: ")
            add_new_pair(new_input, new_response)
        elif user_input.lower() == "start stopwatch":
            stopwatch_start_time = start_stopwatch()
            print("PyChat: Stopwatch started. Press Enter to stop it.")
            input("Press Enter to stop the stopwatch...")
            if stopwatch_start_time is not None:
                elapsed_time = get_elapsed_time(stopwatch_start_time)
                print(f"PyChat: Stopwatch stopped. Elapsed time: {elapsed_time:.2f} seconds")
                stopwatch_start_time = None
        elif user_input.lower() == "delete all inputs":
            delete_all_pairs()
        else:
            response = chatbot.respond(user_input)
            if response is None:
                new_input = user_input
                new_response = input("PyChat: I don't know how to respond to that. What should be my response?\nYou: ")
                add_new_pair(new_input, new_response)
            else:
                print(f"PyChat: {response}")

nltk_chatbot()
