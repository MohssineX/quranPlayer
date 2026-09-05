# mimi is a nice cat 

# github : https://github.com/MohssineX

# Copyright (C) 2026 Mohssine <https://github.com/MohssineX>

# input_hundler.py

import config as cfg
from config import COLOR_RED, COLOR_RESET

def get_user_input():
    while True:
        print(f"Choose what you want {cfg.appName} to do.")
        print("")

        print("[1] Listen to the Quran online")
        print("[2] Download audio file")
        print("")

        option = input("Enter option number : ") 
        print("")

        if option == "1" or option == "2":
            break

        else:
            print(f"{COLOR_RED}Err101 : Invalid option [Please choose 1 or 2]{COLOR_RESET}")
            print("")

    print("Quran Reciters : ")

    print(cfg.reciters)

    while True:
        reciter = input("Enter your preferred reciter number : ")
        print("")

        if reciter in cfg.reciters_urls:
            url = cfg.reciters_urls[reciter]
            break

        else:
            print(f"{COLOR_RED}Err102 : Invalid reciter number [Please enter a number from 1 to 30]{COLOR_RESET}")
            print("")

    while True:

        while True: 
            try:
                Nsurah = int(input("Enter the number of the surah in the Quran : "))
                print("")
                break

            except ValueError:
                print("")
                print(f"{COLOR_RED}Err103 : Invalid input [Please enter a number only]{COLOR_RESET}")
                print("")

        if 1 <= Nsurah <= 114:
            Nsurahint = f"{Nsurah:03}"
            break
        
        else:
            print(f"{COLOR_RED}Err104 : Invalid surah number [Please enter a number between 1 and 114]{COLOR_RESET}")
            print("")

    return option, reciter, url, Nsurahint
