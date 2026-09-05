# mimi is a nice cat 

# github : https://github.com/MohssineX

# Copyright (C) 2026 Mohssine <https://github.com/MohssineX>

# main.py

# import basic libraries

import sys
import os
import signal

if sys.platform == "win32": # Enable ANSI escape codes on Windows (not needed on Linux/Mac)
    os.system("")

# Exit the application when pressing Ctrl+C.

def handle_interrupt(sig, frame):
    print("\n")
    print("\033[33mThank you for using TilawaPlayer!\033[0m")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

# Import the rest of the libraries

from config import COLOR_GREEN, COLOR_RED, COLOR_YELLOW, COLOR_RESET
import config as cfg
import logo
import input_handler
import player
import downloader

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s"
)
running = True

while running:
    print("\033c", end="")

    print(f"{COLOR_GREEN}{logo.logo}{COLOR_RESET}")

    print(f"{COLOR_YELLOW}Welcome to the {cfg.appName} app{COLOR_RESET}")
    print("")

    input(f"Press the Enter button to start using the {cfg.appName} : ")
    print("")

# input_handler.get_user_input() | هده دالة المسؤولة عن معالجة مدخلات و متغيرات التي ستحتفظ بقيم مستخرجة منها
    option, reciter, url, Nsurahint = input_handler.get_user_input()

    logging.info(f"option = {option}")
    logging.info(f"reciter = {reciter}")
    logging.info(f"url = {url}")
    logging.info(f"Nsurahint = {Nsurahint}")
    while True:
        if option == "1":
                try:
                    user_action = player.play_surah(url, Nsurahint)
                    break

                except Exception:
                    logging.exception("Err201 : Streaming failed [Check your internet or Wi-Fi connection and try again]")
                    input(f"{COLOR_RED}Err201 : Streaming failed [Check your internet or Wi-Fi connection and try again]>>>{COLOR_RESET}")
                    print("")
        
        else:
            try:
                user_action = downloader.download_surah(url, reciter, Nsurahint)
                break

            except Exception:
                print("")
                logging.exception("Err202 : Download failed [Check your internet connection, available disk space, and folder write permissions]")
                input(f"{COLOR_RED}Err202 : Download failed [Check your internet connection, available disk space, and folder write permissions]>>>{COLOR_RESET}")
                print("")

    while True:
        
        if user_action == "q":
            print("")
            print(f"{COLOR_YELLOW}goodbye{COLOR_RESET}")
            logging.info(f"Exit : (q)")
            running = False
            break

        elif user_action == "r":
            print("\033c" , end="")
            running = True
            break

        else:
            print("")
            print(f"{COLOR_RED}Err105 : Invalid choice [Please enter 'r' to restart or 'q' to quit]{COLOR_RESET}")
            print("")
            user_action = input(f"{COLOR_GREEN}Type 'r' to restart or 'q' to quit : {COLOR_RESET}")
            

