import geocoder
import random
import sys
import time
import re
from datetime import datetime
from sketchpy import library as ink

def start():
    intro = """Hello there! I'm PyChat, your custom-built Chatbot!
I can crack jokes, share fun facts, give you your current location, draw graphics, and more.
Just type "What can you do?" to see all my features. Let's have some fun chatting together!"""
    print(intro)

def correct_input(cmd):
    cmd = re.sub(r'[^\w\s]', '', cmd)
    cmd = ' '.join(cmd.split())
    variations = [
        ('whatcan you do', 'what can you do'),
        ('openmyaccount', 'open my account'),
        ('showme my current location', 'show me my current location'),
        ('tellme a joke', 'tell me a joke'),
        ('tellme a fun fact', 'tell me a fun fact'),
        ('startdrawing', 'start drawing'),
        ('set a timer', 'set a timer'),
        ('startcounting', 'start counting'),
        ('exit', 'exit')
    ]
    for variation in variations:
        cmd = cmd.replace(variation[0], variation[1])
    return cmd

def chat_with_user():
    jokes = ["""Why don’t scientists trust atoms? Because they make up everything!""", 
"""I’m on a seafood diet. I see food and I eat it.""", 
"""Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.""", 
"""I would tell you a construction joke, but I’m still working on it.""", 
"""Why don’t skeletons fight each other? They don’t have the guts.""", 
"""I told my wife she was drawing her eyebrows too high. She looked surprised.""", 
"""I’d tell you a chemistry joke, but I know I wouldn’t get a reaction.""", 
"""The future, the present, and the past walked into a bar. Things got a little tense.""", 
"""I used to play piano by ear, but now I use my hands.""", 
"""What do you call fake spaghetti? An impasta!""", 
"""I used to be a baker, but I couldn’t make enough dough.""", 
"""Why did the scarecrow win an award? Because he was outstanding in his field!""", 
"""I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.""",
"""Why was the math book sad? Because it had too many problems.""", 
"""What’s orange and sounds like a parrot? A carrot."""]

    facts = ["""Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.""", 
"""A shrimp's heart is located in its head.""", 
"""Bananas are berries, but strawberries aren’t!""", 
"""A day on Venus is longer than a year on Venus.""", 
"""An octopus has three hearts.""", 
"""Wombat poop is cube-shaped.""", 
"""It’s impossible to hum while holding your nose.""", 
"""Dolphins have names for each other.""", 
"""Koalas have fingerprints that are almost identical to human fingerprints.""", 
"""There are more stars in the universe than grains of sand on all the Earth's beaches.""", 
"""A group of flamingos is called a 'flamboyance.""", 
"""Sea otters hold hands while they sleep to keep from drifting apart.""", 
"""A bolt of lightning contains enough energy to toast 100,000 slices of bread.""", 
"""Your nose can remember 50,000 different scents.""", 
"""The Eiffel Tower can be 15 cm taller during the summer because of the expansion of iron in the heat."""]

    year = datetime.now().year

    bday1 = datetime(year, 5, 14)
    bday2 = datetime(year, 11, 24)
    bday3 = datetime(year, 8, 1)

    today_date = datetime.today()
    
    print("How can I assist you today?")
    while True:
        cmd = input('>>> ').strip().lower()
        cmd = correct_input(cmd)

        if cmd == 'what can you do':
            print("""I can crack jokes, share fun facts, give your current location, draw graphics, and more.
Here are the commands you can use:
- Open my account
- Show me my current location
- Tell me a joke
- Tell me a fun fact
- Start drawing
- Set a timer
- Start counting
- Exit""")
        
        elif cmd.startswith('open my account'):
            ID = input('Please enter your 5-digit PyChat ID: ').strip()
            if not ID.isdigit() or len(ID) != 5:
                print('Invalid ID. Please enter a valid 5-digit ID.')
                continue
            if ID == '00001':
                print('Hello Sarthak, nice to meet you!')
                if bday1.date() == today_date.date():
                    print('Happy Birthday Sarthak! You are ', year - 2012, 'years old!')
            elif ID == '00002':
                print('Hello Prajakta, nice to meet you!')
                if bday2.date() == today_date.date():
                    print('Happy Birthday Prajakta! You are ', year - 1981, 'years old!')
            elif ID == '00003':
                print('Hello Pandharinath, nice to meet you!')
                if bday3.date() == today_date.date():
                    print('Happy Birthday Pandharinath! You are ', year - 2012, 'years old!')
            elif ID == '00004':
                print('Hello Rohit, nice to meet you!')
            elif ID == '00005':
                print('Hello Manisha, nice to meet you!')
            elif ID == '00006':
                print('Hello Rucha, nice to meet you!')
            else:
                print('Unknown ID. Could you please double-check?')

        elif cmd == 'show me my current location':
            map_me = geocoder.ip('me')
            try:
                print('Here is your current location in terms of latitudes and longitudes:')
                print('Latitude:', map_me.latlng[0])
                print('Longitude:', map_me.latlng[1])
            except (AttributeError, TypeError):
                print('Error: Unable to retrieve location. Please ensure you are connected to the internet.')

        elif cmd == 'tell me a joke':
            random_joke = random.choice(jokes)
            print('Here is one of my favourite jokes:')
            print(random_joke)
            print('(Some jokes might repeat due to a limited list.)')

        elif cmd == 'tell me a fun fact':
            random_fact = random.choice(facts)
            print('Here is a fun fact which might surprise you:')
            print(random_fact)
            print('(Some facts might repeat due to a limited list.)')

        elif cmd == 'start drawing':
            shape = input("""Please mention your choice in the format shown below.
Supported commands:-
- Tony Stark
- Tom Holland
- Vijay Thalpathy
-> """).strip().lower()
            if shape == 'tony stark':
                pen = ink.rdj()
                print('Sketch in progress')
                pen.draw()
                print('Sketching complete!')
            elif shape == 'tom holland':
                pen = ink.tom_holland()
                pen.draw()
                print('Sketching complete!')
            elif shape == 'vijay thalpathy':
                pen = ink.vijay()
                pen.draw()
                print('Sketching complete!')
            else:
                print('Unknown command. Could you try again?')

        elif cmd == 'set a timer':
            try:
                setter = int(input('Enter the time in seconds -> ').strip())
                for x in range(setter, 0, -1):
                    seconds = x % 60
                    minutes = int(x / 60) % 60
                    hours = int(x / 3600)
                    print(f"{hours:02}:{minutes:02}:{seconds:02}")
                    time.sleep(1)
                print("Time's up!")
            except ValueError:
                print('Invalid input. Please enter an integer.')

        elif cmd == 'exit':
            print('Thank you for visiting PyChat, hope you had a nice time chatting with me!')
            sys.exit(0)

        elif cmd == 'start counting':
            try:
                n = int(input('Enter the last number: ').strip())
                for i in range(n + 1):
                    print(i)
                print('Process complete!')
            except ValueError:
                print('Invalid input. Please enter an integer.')

        else:
            print('Sorry, I did not understand this command. Check your case, spelling, and punctuation, or type "What can you do?" for help.')

def main():
    start()
    chat_with_user()

main()
