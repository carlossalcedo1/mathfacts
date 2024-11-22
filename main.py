'''
math facts game
four different modes  [ subtract,add,multipling,divide ]
has three different difficulties 1,2,3 (1, 1x1 , 2 2x2, 3 3x2)
user profiles to save data.


Database Strucutre (JSON)
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
'''

import json
import base64

import user_class
import encryption
import math
import time



def main():
    #load or create json file, error validation
    global running, user_profile
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            print(f"JSON File Loaded {file.name}")
    except:
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
4. Switch App (Coming Soon!)    
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
                "attributes": {"rank": "none", "streak": 0, "puzzles_solved": 0, "easy_solved": 0, "medium_solved": 0, "hard_solved": 0}
            }
            with open("data.json", "w+") as file:
                #append new data to old exisitng data to avoid data loss
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
                            user_auth = True
                            running = True
                            print("User Authenticated.")
                            #create object for runtime
                            user_object = user_class.User(user_name,
                                                      profile_object["attributes"]["puzzles_solved"],
                                                      profile_object["attributes"]["rank"],
                                                      profile_object["attributes"]["streak"])
                            print("User Object Created.")
                            break
                        else:
                            print("Incorrect Password. Try Again.")
                            continue

            if running:
                break
            #if loop doesnt break out it was not found.
            print("Profile was not found.")
        elif user_option_select == 4:
            print("Coming Soon!")
        elif user_option_select == 3:
            print("Goodbye")
            break

    while running:
        print("start game here")
        print(user_object)
        running = False





if __name__ == "__main__":
    main()

