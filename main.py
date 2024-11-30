"""
math facts game
four different modes  [ subtract,add,multiplying,divide ]
has three different difficulties 1,2,3 (1, 1x1 , 2 2x2, 3 3x2)
user profiles to save data.


Database Structure (JSON)
name = str
password_encrypted = str
attributes = {
  rank = str default=none
  streak = int default=0
  puzzles_solved = int - default=0
  easy_solved = int default=0
  medium_solved = int default=0
  hard_solved = int default=0

}

Future Updates:
- figure out how to add timer
- Extra options for min and max numbers.


Runtime:
References list in data.json and pulls object out of profile into main memory, saves at end by updating file.
All through objects
"""

import json
import base64

import user_class
import screens
from event_class import *
import encryption
import pygame

#glbobal variable between screens and here
screen_size = (1280,720)


def main():
    #load or create json file, error validation
    global user_object
    running = False
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            print(f"JSON File Loaded {file.name}")
    except FileNotFoundError:
        with open("data.json", "w") as file:
            data = []
            json.dump(data, file)
            print(f"JSON File Created {file.name}")


    #load or create key file, error validation
    try:
        if open("encryption.key", "rb").read():
            print(f"Key File loaded")
    except FileNotFoundError:
        encryption.generate_file_key()
        print("Encryption File Created.")

    #load key
    key = encryption.load_key()
    print("Encryption key loaded.")

    #start app
    print("---------------")
    print("""
Welcome to the math game...
Options:
1. Create new user profile.
2. Load user profiles.
3. Quit   
""")
    print("Objects in DB:", len(data))
    while True:
        #user input validation
        while True:
            try:
                user_option_select = int(input("Option: "))
                if user_option_select <= 3:
                    break
                raise ValueError
            except ValueError:
                print("Invalid option")


        #option select
        if user_option_select == 1:
            user_name = input("Select a name for the new profile. ")
            user_password = input("Select a password for the new profile. ")
            password_encrypted = base64.b64encode(encryption.encrypt(user_password, key)).decode('utf-8')
            new_data = {
                "name": user_name,
                "password": password_encrypted,
                "attributes": {"rank": "none", "time_select": 1, "puzzles_solved": 0, "easy_solved": 0, "medium_solved": 0, "hard_solved": 0}
            }
            with open("data.json", "w+") as file:
                #append new data to old existing data to avoid data loss
                data.append(new_data)
                #dump contents to json
                json.dump(data, file, indent=4)

            print(f"User Profile {user_name} created successfully!")
            print("Select 'option 2' to load it.", end="\n\n")
            continue

        elif user_option_select == 2:
            user_name = input("Name of profile: ")
            #find profile in database
            for profile_object in data:
                if profile_object["name"] == user_name:
                    #loop for incorrect password
                    while True:
                        user_password = input("Enter the password: ")
                        #decrypt password by first decoding base64
                        password_decrypted = base64.b64decode(profile_object.get("password"))
                        password_decrypted = encryption.decrypt(password_decrypted, key)
                        if user_password == password_decrypted:
                            running = True
                            print("User Authenticated.")
                            #create object for runtime
                            user_object = user_class.User(user_name,
                                                      profile_object["attributes"]["puzzles_solved"],
                                                      profile_object["attributes"]["rank"],
                                                      profile_object["attributes"]["time_select"]
                            )
                            print("User Object Created.")
                            break
                        else:
                            print("Incorrect Password. Try Again.")
                            continue

            if running:
                break
            #if loop doesn't break out it was not found.
            print("Profile was not found.")
            if running:
                break
        elif user_option_select == 3:
            print("Goodbye")
            break


    #start game
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Math Facts Game")

    #initiziale class (event)
    game = Event("menu")
    game.current_time = user_object.settings_time *15 #seconds


    #local
    time_count = 0

    try:
        while running:

            #if time_count has been started (set to 1) then count 10 ticks then make "incorrect" disappear
            if time_count:
                time_count += 1/60
                if time_count >1.5:
                    game.reset_input()
                    time_count = 0

            #countdown for game-timer
            if game.state == "running":
                if game.current_time >= 0:
                    game.decrement_time()
                if game.current_time <= 0:
                    game.set_state("game-over")



            if game.state == "menu":
                screens.main_screen(screens.main_screen_rectangles, screens.main_screen_texts)

            elif game.state == "menu2":
                screens.main2_screen(screens.main_screen_rectangles, screens.main2_screen_texts)


            elif game.state == "settings":
                screens.settings_screen(user_object.settings_time*15)

            elif game.state == "running":
                screens.game_screen(game.operands, game.operator, game.input_answer, game.streak, user_object.get_puzzles_solved, game.temp_solved, round(game.current_time,2), user_object.rank_name())

            elif game.state == "game-over":
                screens.game_over(game.streak, game.temp_solved, user_object.settings_time*15)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if game.state == "settings":
                        index: int = dynamic_click_event(event.pos, screens.main_screen_rectangles)
                        if index < 0:
                            continue
                        elif index == 0:
                            #{1:15, 2: 30, 3:45, 4:60, 5:90}
                            user_object.time_set()
                        elif index == 1:
                            pass
                        elif index == 2:
                            pass
                        elif index == 3:
                            game.set_state("menu")

                    elif game.state == "menu":
                        index: int = dynamic_click_event(event.pos, screens.main_screen_rectangles)
                        if index < 0:
                            continue
                        if 0 <= index <= 2:
                            #difficulty screens and buttons
                            #2 different difficulties need to be updated for now because two classes are separate
                            user_object.difficulty = index +1
                            game.difficulty = index+1

                            game.set_state("menu2")
                            #difficulty func

                        #settings button
                        if index == 3:
                            game.set_state("settings")

                    elif game.state == "menu2":
                        index: int = dynamic_click_event(event.pos, screens.main_screen_rectangles)
                        if index <0:
                            continue

                        game.operator = index+1 #index+ 1 , 1 is addition, 2 is subtraction, 3 is multiplication, 4 is division
                        game.operand_randomizer()
                        game.set_state("running") #start game

                    elif game.state == "running":
                        #exit button
                        if screens.run_button.collidepoint(event.pos):
                            game.reset(user_object.settings_time*15)

                    elif game.state == "game-over":
                        if screens.run_button.collidepoint(event.pos):
                            game.reset(user_object.settings_time*15)


                if event.type == pygame.KEYDOWN:
                    if game.state == "running":
                        #event keys 0-9 add to a string that calculates the answer
                        if 57 >= event.key >= 48:
                            if game.input_answer == "Incorrect":
                                continue
                            keys_to_numbers = {48:0, 49:1, 50:2, 51:3, 52:4, 53:5, 54:6, 55:7, 56:8, 57:9}
                            game.append_input(str(keys_to_numbers[event.key]))

                        #delete key
                        if event.key == 8:
                            if game.input_answer == "Incorrect":
                                continue
                            game.delete_input_character()

                        #enter key
                        if event.key == 13:
                            #check if correct
                            if game.input_answer == "" or game.input_answer == "Incorrect":
                                continue

                            #if not correct solution
                            if not stat_saver(game):
                                game.set_input("Incorrect")
                                time_count = 1
                                game.reset_streak()







            pygame.display.update() if game.state == "running" else pygame.display.flip()
            pygame.time.Clock().tick(60)
    finally:
        user_class.save_data(user_object)
        pygame.quit()


#screens in screens.py

def dynamic_click_event(event_position: tuple, rectangles : tuple) -> int:
    #take event.pos pygame tuple where the mouse is located.
    #take list of rectangle objects and check if event_position is in the rectangle using collide-point method
    for object_rectangle in rectangles:
        if object_rectangle.collidepoint(event_position):
            index_rectangle = rectangles.index(object_rectangle)
            return index_rectangle
    return -1

def stat_saver(game_object):
    if game_object.input_answer == "":
        game_object.input_answer = 0
    operations = {
        1: lambda arguments : int(game_object.input_answer) == arguments[0] + arguments[1],
        2: lambda arguments : int(game_object.input_answer) == arguments[0] - arguments[1],
        3: lambda arguments : int(game_object.input_answer) == arguments[0] * arguments[1],
        4: lambda arguments : int(game_object.input_answer) == arguments[0] // arguments[1]

    }
    correct_solution = operations[game_object.operator](game_object.operands)
    if correct_solution:
        user_object.increment_solved()
        game_object.increment_streak()
        game_object.reset_input()
        game_object.temp_solved += 1
        game_object.operand_randomizer()
        user_object.rank_upgrade()
        return True
    return False



if __name__ == "__main__":
    main()

