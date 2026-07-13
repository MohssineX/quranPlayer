# mimi is a nice cat 

# github : https://github.com/MohssineX

# Copyright (C) 2026 Mohssine <https://github.com/MohssineX>

# import libraries

import miniaudio
import sys

# color variables

color_green = "\033[32m"
color_yellow = "\033[33m"
color_red = "\033[31m"
color_reset = "\033[0m"


# Enable ANSI escape codes on Windows (not needed on Linux/Mac)

if sys.platform == "win32":
    import os
    os.system("")

running = True


try :

    while running :

        print("\033c", end="")



        print(f"{color_yellow}Welcome to the quranPlayer app{color_reset}")
        print("")

        input("Press the Enter button to start using the Quran player : ")
        print("")

        print("Quran Reciters : ")
        print("")
        print(f"{color_green}1 / Abdul Basit Abdus Samad{color_reset}")
        print(f"{color_green}2 / Mahmoud Khalil Al-Husary{color_reset}")
        print(f"{color_green}3 / Mohamed Siddiq Al-Minshawi{color_reset}")
        print(f"{color_green}4 / Mishary Rashid Alafasy{color_reset}")
        print(f"{color_green}5 / Maher Al-Muaiqly{color_reset}")
        print(f"{color_green}6 / Yasser Al-Dosari{color_reset}")
        print(f"{color_green}7 / Saad Al-Ghamdi{color_reset}")
        print(f"{color_green}8 / Saud Al-Shuraim{color_reset}")
        print(f"{color_green}9 / Ahmed Al-Ajmi{color_reset}")
        print(f"{color_green}10 / Abdul Rahman Al-Sudais{color_reset}")
        print("")



        while True :

            reciter = input("Enter your preferred reciter number : ")
            print("")

            if reciter == "1" :

                url = "https://server7.mp3quran.net/basit/"
                break

            elif reciter == "2" :

                url = "https://server13.mp3quran.net/husr/"
                break

            elif reciter == "3" :

                url = "https://server10.mp3quran.net/minsh/"
                break

            elif reciter == "4" :

                url = "https://server8.mp3quran.net/afs/"
                break

            elif reciter == "5" :

                url = "https://server12.mp3quran.net/maher/"
                break

            elif reciter == "6" :

                url = "https://server11.mp3quran.net/yasser/"
                break

            elif reciter == "7" :

                url = "https://server6.mp3quran.net/ghamdi/"
                break

            elif reciter == "8" :

                url =  "https://server7.mp3quran.net/shur/"
                break

            elif reciter == "9" :

                url =  "https://server10.mp3quran.net/ajm/"
                break

            elif reciter == "10" :

                url = "https://server11.mp3quran.net/sds/"
                break

            else :

                print(f"{color_red}err001 : There is no reciter with this number :( Please try again {color_reset}")
                print("")

        while True :

            while True : 

                try :

                    Nsurah = int(input("Enter the number of the surah in the Quran : "))
                    print("")
                    break

                except ValueError :

                    print("")
                    print(f"{color_red}err002 : Please enter a number, not a letter or symbol :( {color_reset}")
                    print("")


            if 1 <= Nsurah <= 114 :

                Nsurahint = f"{Nsurah:03}"
                break
            
            else :

                print(f"{color_red}err003 : Incorrect Surah number :( Please try again {color_reset}")
                print("")

        while True :

            try:

                source = miniaudio.IceCastClient(f"{url}{Nsurahint}.mp3")
                stream = miniaudio.stream_any(source, source.audio_format)

                break


            except Exception  :

                input(f"{color_red}err004 : Please check your internet or Wi-Fi connection :({color_reset}")
                print("")

        with miniaudio.PlaybackDevice() as device:
            device.start(stream)
            print("The Quran is playing")
            print("")
            print(f"{color_yellow}Thank you for using quranPlayer!{color_reset}")
            print("")
            user_action = input(f"{color_green}Type 'r' to restart or 'q' to quit : {color_reset}")

        

        while True :
                    
            
                    if user_action == "q" :
                        print()
                        print(f"{color_yellow}goodbye{color_reset}")
                        running = False
                        break
            
            
            
                    elif user_action == "r" :
                        print("\033c" , end="")
            
                        running = True
                        break
            
                    else :
                        print("")
                        print(f"{color_red}err005 : Choice is not ('r' or 'q') please try again :( {color_reset}")
                        print("")
                        user_action = input(f"{color_green}Type 'r' to restart or 'q' to quit : {color_reset}")
            

except KeyboardInterrupt :

        print("")
        print("")
        print(f"{color_yellow}Thank you for using quranPlayer!{color_reset}")
