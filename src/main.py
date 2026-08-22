# mimi is a nice cat 

# github : https://github.com/MohssineX

# Copyright (C) 2026 Mohssine <https://github.com/MohssineX>

# import basic libraries

import sys
import signal

# Exit the application when pressing Ctrl+C.

def handle_interrupt(sig, frame) :

    print("")
    print("")
    print("\033[33mThank you for using TilawaPlayer!\033[0m")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

# Import the rest of the libraries

import os
import config as cfg
from config import COLOR_GREEN, COLOR_RED, COLOR_YELLOW, COLOR_RESET
import logo
import miniaudio
import urllib.request

# Enable ANSI escape codes on Windows (not needed on Linux/Mac)

if sys.platform == "win32" :

    os.system("")

running = True

while running :

    print("\033c", end="")

    print(f"{cfg.COLOR_GREEN}{logo.logo}{cfg.COLOR_RESET}")

    print(f"{COLOR_YELLOW}Welcome to the {cfg.appName} app{COLOR_RESET}")
    print("")

    input(f"Press the Enter button to start using the {cfg.appName} : ")
    print("")

    while True :

        print(f"Choose what you want {cfg.appName} to do.")
        print("")

        print("[1] Listen to the Quran online")
        print("[2] Download audio file")
        print("")

        option = input("Enter option number : ") 
        print("")

        if option == "1" or option == "2" :

            break

        else :

            print(f"{COLOR_RED}Err101 : Invalid option [Please choose 1 or 2]{COLOR_RESET}")
            print("")

    print("Quran Reciters : ")

    print(cfg.reciters)

    while True :

        reciter = input("Enter your preferred reciter number : ")
        print("")

        if reciter in cfg.reciters_urls :

            url = cfg.reciters_urls[reciter]
            break

        else :

            print(f"{COLOR_RED}Err102 : Invalid reciter number [Please enter a number from 1 to 30]{COLOR_RESET}")
            print("")

    while True :

        while True : 

            try :

                Nsurah = int(input("Enter the number of the surah in the Quran : "))
                print("")
                break

            except ValueError :

                print("")
                print(f"{COLOR_RED}Err103 : Invalid input [Please enter a number only]{COLOR_RESET}")
                print("")

        if 1 <= Nsurah <= 114 :

            Nsurahint = f"{Nsurah:03}"
            break
        
        else :

            print(f"{COLOR_RED}Err104 : Invalid surah number [Please enter a number between 1 and 114]{COLOR_RESET}")
            print("")

    while True :

        if option == "1" :

                try:
                    
                    class MP3Source(miniaudio.StreamableSource) :

                        def __init__(self, url) :

                            self.response = urllib.request.urlopen(url, timeout=cfg.timeoutCfg)
                            self.error_occurred = False

                        def read(self, num_bytes) :

                            try :

                                return self.response.read(num_bytes)

                            except Exception :

                                if not self.error_occurred :

                                    print("")
                                    print("")
                                    print(f"{COLOR_RED}Err203 : Unexpected disconnection [Please restart {cfg.appName}]{COLOR_RESET}", flush=True)
                                    print("")
                                    print(f"{COLOR_GREEN}Type 'r' to restart or 'q' to quit : {COLOR_RESET}", end="", flush=True)

                                self.error_occurred = True
                                return b""
                                
                    source = MP3Source(f"{url}{Nsurahint}.mp3")
                    stream = miniaudio.stream_any(source, miniaudio.FileFormat.MP3)

                    with miniaudio.PlaybackDevice() as device :

                        device.start(stream)
                        print("The Quran is playing")
                        print("")
                        
                        print(f"{COLOR_YELLOW}Thank you for using quranPlayer!{COLOR_RESET}")
                        print("")

                        user_action = input(f"{COLOR_GREEN}Type 'r' to restart or 'q' to quit : {COLOR_RESET}")
                        break

                except Exception :

                    input(f"{COLOR_RED}Err201 : Streaming failed [Check your internet or Wi-Fi connection and try again]>>>{COLOR_RESET}")
                    print("")
                        
        else :

            try :

                script_path = os.path.dirname(os.path.abspath(__file__))

                file_path = os.path.join(script_path, f"TilawaPlayerR{reciter}S{Nsurahint}.mp3")

                print("An audio file is being downloaded...")

                with urllib.request.urlopen(f"{url}{Nsurahint}.mp3", timeout=cfg.timeoutCfg) as response :

                    with open(file_path, "wb") as file :

                        while True :

                            chunk = response.read(cfg.chunkDownload)

                            if not chunk :

                                break

                            file.write(chunk)

                print("")
                print(f"{COLOR_YELLOW}A file was downloaded to {file_path}{COLOR_RESET}")
                print("")
                print(f"{COLOR_YELLOW}Thank you for using TilawaPlayer!{COLOR_RESET}")
                print("")

                user_action = input(f"{COLOR_GREEN}Type 'r' to restart or 'q' to quit : {COLOR_RESET}")
                break

            except Exception :

                print("")
                input(f"{COLOR_RED}Err202 : Download failed [Check your internet connection, available disk space, and folder write permissions]>>>{COLOR_RESET}")
                print("")

    while True :
                
        if user_action == "q" :

            print("")
            print(f"{COLOR_YELLOW}goodbye{COLOR_RESET}")
            running = False
            break

        elif user_action == "r" :

            print("\033c" , end="")

            running = True
            break

        else :

            print("")
            print(f"{COLOR_RED}Err105 : Invalid choice [Please enter 'r' to restart or 'q' to quit]{COLOR_RESET}")
            print("")
            user_action = input(f"{COLOR_GREEN}Type 'r' to restart or 'q' to quit : {COLOR_RESET}")


