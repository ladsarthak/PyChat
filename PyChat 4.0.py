import random
import sys
import time

def start():
    print('Initializing PyChat 4.0...')
    time.sleep(0.3)
    print("""Hello there! I'm PyChat, your custom-built Chatbot!
Just type "What can you do?" to see all my features. Let's have some fun chatting together!
          Warning: This chatbot is instructed to cause damage in its directory if handled incorrectly. Use with care.""")

def get_jokes():
    return [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "I’m on a seafood diet. I see food and I eat it.",
        "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.",
        "I would tell you a construction joke, but I’m still working on it.",
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "I’d tell you a chemistry joke, but I know I wouldn’t get a reaction.",
        "The future, the present, and the past walked into a bar. Things got a little tense.",
        "I used to play piano by ear, but now I use my hands.",
        "What do you call fake spaghetti? An impasta!",
        "I used to be a baker, but I couldn’t make enough dough.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.",
        "Why was the math book sad? Because it had too many problems.",
        "What’s orange and sounds like a parrot? A carrot."
    ]

def get_facts():
    return [
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
        "A shrimp's heart is located in its head.",
        "Bananas are berries, but strawberries aren’t!",
        "A day on Venus is longer than a year on Venus.",
        "An octopus has three hearts.",
        "Wombat poop is cube-shaped.",
        "It’s impossible to hum while holding your nose.",
        "Dolphins have names for each other.",
        "Koalas have fingerprints that are almost identical to human fingerprints.",
        "There are more stars in the universe than grains of sand on all the Earth's beaches.",
        "A group of flamingos is called a 'flamboyance.",
        "Sea otters hold hands while they sleep to keep from drifting apart.",
        "A bolt of lightning contains enough energy to toast 100,000 slices of bread.",
        "Your nose can remember 50,000 different scents.",
        "The Eiffel Tower can be 15 cm taller during the summer because of the expansion of iron in the heat."
    ]

def chat_with_user():
    jokes = get_jokes()
    facts = get_facts()
    print("How can I assist you today?")
    while True:
        try:
            cmd = input('>>> ').strip().lower()
        except (EOFError, KeyboardInterrupt):
            print('\nKeyboard Intervention Detected.\nExiting PyChat. Goodbye!')
            time.sleep(0.5)
            break

        if not cmd:
            continue

        if any(greet in cmd for greet in ['hi', 'hello', 'hey', 'good morning', 'good afternoon', 'good evening']):
            greetings = [
                'Hello!', 'Hi there!', 'Hi bro!', 'Hey!', 'Greetings!', 'Good to see you!', 'Good day!', 'Howdy!',
                "What's up?", 'Welcome!', 'Nice to meet you!', 'Salutations!', 'Good to have you here!',
                'Pleasure to meet you!', 'Hiya!', 'Hola!', 'Bonjour!', 'Ciao!', 'Greetings and salutations!',
                'Good to see you again!'
            ]
            print(random.choice(greetings), 'I am PyChat 4.0.')

        elif any(ability in cmd for ability in ['what can you do', 'what are your features', 'help']):
            print("""I can crack jokes, share fun facts, give your current location, draw graphics, and more.
Here are the commands you can use:
- Play X and O
- Play PvP Shooting Game
- Show me my current location
- Tell me a joke
- Tell me a fun fact
- Start drawing
- Set a timer
- Start counting
- Show code
- Exit

Tip - You can also type '/help' to see this list again.
""")

        elif any(games in cmd for games in ['play']):
            while True:
                if any(x in cmd for x in ['x and o', 'tic-tac-toe', 'x o', 'tic tac toe', 'xo']):
                    play_tic_tac_toe()
                    break
                elif any(x in cmd for x in ['shoot', 'pvp']):
                    play_pvp_game()
                    break
                else:
                    print("Specify a game: 'Play X and O' or 'Play PvP Shooting Game'.")

        elif any(x in cmd for x in ['location', 'where am i']):
            show_location()

        elif any(x in cmd for x in ['joke']):
            print('Here is one of my favourite jokes:')
            print(random.choice(jokes))
            print('(Some jokes might repeat due to a limited list.)')

        elif 'fact' in cmd:
            print('Here is a fun fact which might surprise you:')
            print(random.choice(facts))
            print('(Some facts might repeat due to a limited list.)')

        elif 'draw' in cmd or 'sketch' in cmd:
            drawing_menu()

        elif 'set a timer' in cmd or 'timer' in cmd:
            set_timer()

        elif cmd in ['exit', 'x', 'quit', 'bye']:
            print('Thank you for visiting PyChat, hope you had a nice time chatting with me!')
            time.sleep(0.5)
            sys.exit(0)

        elif any(x in cmd for x in ['count']):
            start_counting()

        elif any(x in cmd for x in ['code', 'program', 'source']):
            show_source_code()

        elif any(x in cmd for x in ['ssn']):
            ssn_print('Initiating Stark Security Networks.')
            import re
            ssn_print('Welcome to Stark Security Networks (SSN)')
            time.sleep(0.3)

            def ssn_pwd_check():
                SSN_pwd = ssn_input('Please enter the password - ')
                if SSN_pwd == '!@#$%^&*()':
                    ssn_print('Partial Access Granted')
                    time.sleep(0.3)
                    ssn_usn_check()
                elif SSN_pwd == 'x':
                    ssn_print('Terminating Stark Security Networks (SSN).')
                    time.sleep(0.3)
                    main()
                else:
                    ssn_print('Partial Access Denied.')
                    ssn_pwd_check()

            def ssn_usn_check():
                SSN_usn = ssn_input('Please enter your username - ').strip().lower()
                if SSN_usn == 'sarthak':
                    ssn_print('Username Verified. Complete Access Granted.')

                    # ANSI escape codes for colors
                    """COLORS = [
                        '\033[91m', # Red
                        '\033[92m', # Green
                        '\033[93m', # Yellow
                        '\033[94m', # Blue
                        '\033[95m', # Magenta
                        '\033[96m', # Cyan
                        '\033[97m', # White
                        '\033[90m', # Grey
                    ]"""

                elif SSN_usn == 'x':
                    ssn_print('Terminating Stark Security Networks (SSN).')
                    time.sleep(0.3)
                    main()
                else:
                    ssn_print('Uername Invalid. Complete Access Denied.')
                    ssn_usn_check()

            def ssn():
                while True:
                    try:
                        ssn_cmd = ssn_input('-> ').strip().lower()
                    except (EOFError, KeyboardInterrupt):
                        ssn_print('Keyboard Intervention Detected. Initiating Security Breach Sequence by Stark Security Networks (SSN).')
                        time.sleep(1)
                        ssn_print('Terminating Stark Security Networks for safety purposes.')
                        main()
                    if any(x in ssn_cmd for x in ['exit', 'x', 'quit', 'terminate', 'bye', 'destroy']):
                        ssn_print('Terminating Stark Security Networks (SSN).')
                        time.sleep(0.3)
                        main()
                    elif any(x in ssn_cmd for x in ['fake', 'dummy', 'data']):
                        fake_ssn()
                    elif any(x in ssn_cmd for x in ['notifier']):
                        notifier()
                    elif any(x in ssn_cmd for x in ['hack']):
                        hack()
                    elif any(x in ssn_cmd for x in ['open']):
                        opener()
                    else:
                        ssn_print('Invalid command.')
                        

            ssn_pwd_check()
            ssn()

        else:
            print('Sorry, I did not understand this command. Check your case, spelling, and punctuation, or type "What can you do?" for help.')


Red = '\033[91m'
Green = '\033[92m'
Yellow = '\033[93m'
Blue = '\033[94m'
Magenta = '\033[95m'
Cyan = '\033[96m'
White = '\033[97m'
Grey = '\033[90m'

RESET = '\033[0m'

ssn_color = Cyan
hack_color = Red
open_color = Blue

def ssn_print(text):
    print(f"{ssn_color}{text}{RESET}")
def ssn_input(text):
    return input(f"{ssn_color}{text}{RESET}")

def hack_print(text):
    print(f"{hack_color}{text}{RESET}")
def hack_input(text):
    return input(f"{hack_color}{text}{RESET}")

def open_print(text):
    print(f"{open_color}{text}{RESET}")
def open_input(text):
    return input(f"{open_color}{text}{RESET}")

def opener():
    import subprocess
    open_cmd = open_input('What do you want to open? ').strip().lower()
    if any (x in open_cmd for x in ['file explorer', 'explorer']):
        subprocess.Popen('explorer.exe')
    elif any (x in open_cmd for x in ['notepad']):
        subprocess.Popen('notepad.exe')
    elif any (x in open_cmd for x in ['calculator', 'calc']):
        subprocess.Popen('calc.exe')
    elif any (x in open_cmd for x in ['paint']):
        subprocess.Popen('mspaint.exe')
    else:
        ssn_print('Invalid application name.')
        opener()

def hack():
    import os
    import json

    def copy_replace_and_rename():
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        data_dict = {}
        file_counter = 1
        
        for filename in os.listdir(current_directory):
            file_path = os.path.join(current_directory, filename)
            
            if os.path.isfile(file_path) and filename != os.path.basename(__file__):
                with open(file_path, 'r', encoding='utf-8') as file:
                    data_dict[filename] = file.read()
                
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write("Hacked")
                
                new_file_name = f"Hacked_{file_counter}"
                new_file_path = os.path.join(current_directory, new_file_name)
                os.rename(file_path, new_file_path)
                file_counter += 1
        json_file_path = os.path.join(current_directory, "Copied Data.json")
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data_dict, json_file, indent=4)
        
        return data_dict

    if __name__ == "__main__":
        hack_confirm = hack_input('Are you sure you want to hack all the files in this directory. This action is permanent and irreversible (y/n)? ')
        if hack_confirm.lower() == 'y':
            copied_data = copy_replace_and_rename()
            hack_print("Hacked Data: ", copied_data)
        else:
            hack_print("Hacking aborted.")

def notifier():
    from plyer import notification

    def desktop_notifier(title, message):
        notification.notify(
            title=title,
            message=message,
            app_name="Desktop Notifier",
            timeout=10
        )

    if __name__ == "__main__":
        titleinp = ssn_input('Enter the notification title - ')
        titlemsg = ssn_input('Enter the notification message - ')
        time.sleep(0.3)
        desktop_notifier(titleinp, titlemsg)

def fake_ssn():
    from faker import Faker
    from faker.providers import internet
    import time

    def fakemain():
        def generate_user_data(num):
            fake = Faker()

            fake.add_provider(internet)

            user_data = []

            for _ in range(num):
                user = {
                    "Name": fake.name(),
                    "Email": fake.email(),
                    "Phone": fake.phone_number(),
                    "Birthdate": fake.date_of_birth(minimum_age=15, maximum_age=50).strftime("%Y-%m-%d"),
                    "Address": fake.address().replace("\n", ", "),
                    "City": fake.city(),
                    "Country": fake.country(),
                    "ZIP": fake.zipcode(),
                    "Job": fake.job(),
                    "Company": fake.company(),
                    "IP Address": fake.ipv4_private(),
                    "Credit Card Number": fake.credit_card_number(),
                    "Username": fake.user_name(),
                    "Password": fake.password(),
                    "Website": fake.url(),
                }

                user_data.append(user)
            return user_data

        def print_data_vertically(data):
            for user in data:
                for key, value in user.items():
                    ssn_print(f"{key}: {value}")
                print()

        num = ssn_input("Enter the number of user data lists to generate: ")

        if num == "":
            ssn_print("No input provided. Please enter a postive integer.")
            main()
        elif not num.isdigit() or int(num) <= 0:
            ssn_print("Invalid input. Please enter a positive integer.")
            main()
        else:
            user_data = generate_user_data(int(num))

        print_data_vertically(user_data)

    fakemain()

def play_tic_tac_toe():
    import time
    import random
    print("Alright, so let's play Tic-Tac-Toe!")
    time.sleep(0.3)
    print("I will be your opponent.")
    time.sleep(0.3)
    Players = ['X', 'O']
    you_xo = random.choice(Players)
    print(f"You are {you_xo}, and I am {'O' if you_xo == 'X' else 'X'}.")
    time.sleep(0.3)
    print("""
      |1|2|3|
      |4|5|6|
      |7|8|9|
    """)
    print("Please enter the number corresponding to the cell you want to mark.")
    board = [' ' for _ in range(9)]

    def print_board():
        print("\nCurrent Board:")
        print(" " + board[0] + " | " + board[1] + " | " + board[2])
        print("---|---|---")
        print(" " + board[3] + " | " + board[4] + " | " + board[5])
        print("---|---|---")
        print(" " + board[6] + " | " + board[7] + " | " + board[8])
        print()

    def check_winner():
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
                return board[combo[0]]
        return None

    def is_board_full():
        return ' ' not in board

    while True:
        print_board()
        if you_xo == 'X':
            move = input("Your turn (X), enter a number (1-9): ")
            if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == ' ':
                board[int(move) - 1] = 'X'
                winner = check_winner()
                if winner:
                    print_board()
                    print("Congratulations! You win!")
                    break
                if is_board_full():
                    print_board()
                    print("It's a draw!")
                    break
                you_xo = 'O'
            else:
                print("Invalid move. Try again.")
        else:
            move = random.choice([i for i in range(9) if board[i] == ' '])
            board[move] = 'O'
            winner = check_winner()
            if winner:
                print_board()
                print("I win! Better luck next time!")
                break
            if is_board_full():
                print_board()
                print("It's a draw!")
                break
            you_xo = 'X'

def play_pvp_game():
    try:
        import pygame
    except ImportError:
        print("Pygame is not installed. Please install it to play this game.")
        return
    import time

    try:
        pygame.init()
        SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
        WHITE, BLACK, RED, BLUE = (255,255,255), (0,0,0), (255,0,0), (0,0,255)
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("PvP Shooting Game")
        clock = pygame.time.Clock()
        PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
        player1_x, player1_y = 100, SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2
        player2_x, player2_y = SCREEN_WIDTH - 100 - PLAYER_WIDTH, SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2
        player_speed = 5
        BULLET_WIDTH, BULLET_HEIGHT = 10, 5
        bullets1, bullets2 = [], []
        bullet_speed = 10
        winner = None

        def draw_player(x, y, color):
            pygame.draw.rect(screen, color, (x, y, PLAYER_WIDTH, PLAYER_HEIGHT))

        def draw_bullet(bullets, color):
            for bullet in bullets:
                pygame.draw.rect(screen, color, bullet)

        def check_collision(bullets, opponent_x, opponent_y):
            for bullet in bullets:
                if (opponent_x < bullet.x < opponent_x + PLAYER_WIDTH and
                    opponent_y < bullet.y < opponent_y + PLAYER_HEIGHT):
                    return True
            return False

        running = True
        while running:
            screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            # Player 1 movement (WASD)
            if keys[pygame.K_w] and player1_y > 0:
                player1_y -= player_speed
            if keys[pygame.K_s] and player1_y < SCREEN_HEIGHT - PLAYER_HEIGHT:
                player1_y += player_speed
            if keys[pygame.K_a] and player1_x > 0:
                player1_x -= player_speed
            if keys[pygame.K_d] and player1_x < SCREEN_WIDTH // 2 - PLAYER_WIDTH:
                player1_x += player_speed
            # Player 2 movement (Arrow keys)
            if keys[pygame.K_UP] and player2_y > 0:
                player2_y -= player_speed
            if keys[pygame.K_DOWN] and player2_y < SCREEN_HEIGHT - PLAYER_HEIGHT:
                player2_y += player_speed
            if keys[pygame.K_LEFT] and player2_x > SCREEN_WIDTH // 2:
                player2_x -= player_speed
            if keys[pygame.K_RIGHT] and player2_x < SCREEN_WIDTH - PLAYER_WIDTH:
                player2_x += player_speed
            # Player 1 shooting (Space)
            if keys[pygame.K_SPACE]:
                if len(bullets1) < 5:
                    bullets1.append(pygame.Rect(player1_x + PLAYER_WIDTH, player1_y + PLAYER_HEIGHT // 2 - BULLET_HEIGHT // 2, BULLET_WIDTH, BULLET_HEIGHT))
            # Player 2 shooting (Right Ctrl)
            if keys[pygame.K_RCTRL]:
                if len(bullets2) < 5:
                    bullets2.append(pygame.Rect(player2_x - BULLET_WIDTH, player2_y + PLAYER_HEIGHT // 2 - BULLET_HEIGHT // 2, BULLET_WIDTH, BULLET_HEIGHT))
            # Move bullets
            for bullet in bullets1[:]:
                bullet.x += bullet_speed
                if bullet.x > SCREEN_WIDTH:
                    bullets1.remove(bullet)
            for bullet in bullets2[:]:
                bullet.x -= bullet_speed
                if bullet.x < 0:
                    bullets2.remove(bullet)
            # Check for collisions
            if check_collision(bullets1, player2_x, player2_y):
                winner = "Player 1"
                running = False
            if check_collision(bullets2, player1_x, player1_y):
                winner = "Player 2"
                running = False
            draw_player(player1_x, player1_y, BLUE)
            draw_player(player2_x, player2_y, RED)
            draw_bullet(bullets1, BLUE)
            draw_bullet(bullets2, RED)
            pygame.display.flip()
            clock.tick(60)
        # Display winner
        screen.fill(WHITE)
        font = pygame.font.Font(None, 74)
        text = font.render(f"{winner} Wins!", True, BLACK)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
    except Exception as e:
        print(f"An error occurred in the PvP game: {e}")
        try:
            pygame.quit()
        except Exception:
            pass

def show_location():
    try:
        import geocoder
        map_me = geocoder.ip('me')
        if map_me and map_me.latlng:
            print('Here is your current location in terms of latitudes and longitudes:')
            print('Latitude:', map_me.latlng[0])
            print('Longitude:', map_me.latlng[1])
        else:
            print('Error: Unable to retrieve location. Please ensure you are connected to the internet.')
    except ImportError:
        print('geocoder is not installed. Please install it to use this feature.')
    except Exception as e:
        print(f'Error: Unable to retrieve location. {e}')

def drawing_menu():
    try:
        from sketchpy import library as ink
    except ImportError:
        print("sketchpy is not installed. Please install it to use drawing features.")
        return
    while True:
        shape = input("""
Please mention your choice (item number) from the list shown below.
Supported commands:-
1. Robert Downy Jr.
2. Tom Holland
3. Vijay Thalpathy
Press X to exit.
>>> """).strip().lower()
        try:
            if shape == '1' or 'robert' in shape or 'rdj' in shape:
                pen = ink.rdj()
                print('Sketch in progress. Please close the drawing window before starting another.')
                pen.draw()
                print('Sketching complete!')
            elif shape == '2' or 'tom' in shape:
                pen = ink.tom_holland()
                print('Sketch in progress. Please close the drawing window before starting another.')
                pen.draw()
                print('Sketching complete!')
            elif shape == '3' or 'vijay' in shape:
                pen = ink.vijay()
                print('Sketch in progress. Please close the drawing window before starting another.')
                pen.draw()
                print('Sketching complete!')
            elif shape == 'x' or 'exit' in shape:
                break
            else:
                print('Invalid item number. Please try again.')
        except Exception as e:
            print(f"An error occurred during drawing: {e}")
            print("If the drawing window is open, please close it before trying again.")

def set_timer():
    while True:
        setter = input("""
Enter the time (in seconds)
Press X to exit.
>>> 
        """).strip().lower()
        if setter == 'x' or setter == 'exit':
            break
        try:
            seconds = int(setter)
            for x in range(seconds, 0, -1):
                mins, secs = divmod(x, 60)
                hours, mins = divmod(mins, 60)
                print(f"{hours:02}:{mins:02}:{secs:02}")
                time.sleep(1)
            print("Time's up!")
            break
        except ValueError:
            print('Invalid input. Please enter an integer.')
        except Exception as e:
            print(f"An error occurred in the timer: {e}")
            break

def start_counting():
    try:
        n = int(input('Enter the last number: ').strip())
        for i in range(n + 1):
            print(i)
        print('Process complete!')
    except ValueError:
        print('Invalid input. Please enter an integer.')
    except Exception as e:
        print(f"An error occurred while counting: {e}")

def show_source_code():
    try:
        import os
        filename = __file__ if '__file__' in globals() else os.path.abspath(sys.argv[0])
        with open(filename, 'r', encoding='utf-8') as f:
            print('Here is the source code of this program:\n\n')
            time.sleep(0.5)
            print(f.read())
    except Exception as e:
        print(f"Error displaying code: {e}")

def main():
    start()
    chat_with_user()

if __name__ == "__main__":
    main()