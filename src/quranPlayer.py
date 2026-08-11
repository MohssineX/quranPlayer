# mimi is a nice cat 

# github : https://github.com/MohssineX

# Copyright (C) 2026 Mohssine <https://github.com/MohssineX>

# import libraries

try :

    import miniaudio
    import sys
    import os
    import urllib.request

    # color variables

    color_green = "\033[32m"
    color_yellow = "\033[33m"
    color_red = "\033[31m"
    color_reset = "\033[0m"

    # Enable ANSI escape codes on Windows (not needed on Linux/Mac)

    if sys.platform == "win32" :

        os.system("")

    running = True

    while running :

        print("\033c", end="")

        print(f"""{color_green} 

                 ██████╗ ██╗   ██╗██████╗  █████╗ ███╗   ██╗
                ██╔═══██╗██║   ██║██╔══██╗██╔══██╗████╗  ██║
                ██║   ██║██║   ██║██████╔╝███████║██╔██╗ ██║
                ██║▄▄ ██║██║   ██║██╔══██╗██╔══██║██║╚██╗██║
                ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║ ╚████║
                 ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ 

                                                                {color_reset}""")

        print(f"{color_yellow}Welcome to the quranPlayer app{color_reset}")
        print("")

        input("Press the Enter button to start using the quranPlayer : ")
        print("")

        while True :

            print("Choose what you want quranPlayer to do.")
            print("")

            print("[1] Listen to the Quran online")
            print("[2] Download audio file")
            print("")

            option = input("Enter option number : ") 
            print("")

            if option == "1" :

                break

            elif option == "2" :

                break

            else :

                print(f"{color_red}Err101 : Invalid option [Please choose 1 or 2]{color_reset}")
                print("")

        print("Quran Reciters : ")
        print("")
        print(f"{color_yellow}╭─────────────────────────────────────────────────────────────────╮{color_reset}")
        print(f"{color_yellow}│{color_green} [1] Abdul Basit Abdus Samad    │ [16] Ali Jaber                 {color_yellow}│{color_reset}")
        print(f"{color_yellow}│{color_green} [2] Mahmoud Khalil Al-Husary   │ [17] Bandar Baleela            {color_yellow}│{color_reset}")
        print(f"{color_yellow}│{color_green} [3] Mohamed Siddiq Al-Minshawi │ [18] Khalid Al-Jalil           {color_yellow}│{color_reset}")
        print(f"{color_yellow}│{color_green} [4] Mishary Rashid Alafasy     │ [19] Abdullah Basfar           {color_yellow}│{color_reset}")
        print(f"{color_yellow}│{color_green} [5] Maher Al-Muaiqly           │ [20] Salah Bukhatir            {color_yellow}│{color_reset}")
        print(f"{color_yellow}│{color_green} [6] Yasser Al-Dosari           │ [21] Abdul Mohsen Al-Qasim     {color_yellow}│{color_reset}")
        print(f"{color_yellow}│{color_green} [7] Saad Al-Ghamdi             │ [22] Abdullah Al-Juhany        {color_yellow}│{color_reset}")
        print(f"{color_yellow}│{color_green} [8] Saud Al-Shuraim            │ [23] Salah Al-Budair           {color_yellow}│{color_reset}")
        print(f"{color_yellow}│{color_green} [9] Ahmed Al-Ajmi              │ [24] Hani Al-Rifai             {color_yellow}│{color_reset}")
        print(f"{color_yellow}│{color_green} [10] Abdul Rahman Al-Sudais    │ [25] Mohamed Gibril            {color_yellow}│{color_reset}")
        print(f"{color_yellow}│{color_green} [11] Abu Bakr Al-Shatri        │ [26] Mahmoud Ali Al-Banna      {color_yellow}│{color_reset}")
        print(f"{color_yellow}│{color_green} [12] Muhammad Ayyoub           │ [27] Mustafa Ismail            {color_yellow}│{color_reset}")
        print(f"{color_yellow}│{color_green} [13] Nasser Al-Qatami          │ [28] Abdul Bari Al-Thubaity    {color_yellow}│{color_reset}")
        print(f"{color_yellow}│{color_green} [14] Ali Al-Hudhaifi           │ [29] Wadee Al-Yamani           {color_yellow}│{color_reset}")
        print(f"{color_yellow}│{color_green} [15] Khalifa Al-Tunaiji        │ [30] Khalid Al-Qahtani         {color_yellow}│{color_reset}")
        print(f"{color_yellow}╰─────────────────────────────────────────────────────────────────╯{color_reset}")
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

                url = "https://server7.mp3quran.net/s_gmd/"
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

            elif reciter == "11" :

                url = "https://server11.mp3quran.net/shatri/"
                break

            elif reciter == "12" :

                url = "https://server8.mp3quran.net/ayyub/"
                break

            elif reciter == "13" :

                url = "https://server6.mp3quran.net/qtm/"
                break

            elif reciter == "14" :

                url = "https://server9.mp3quran.net/hthfi/"
                break

            elif reciter == "15" :

                url = "https://server12.mp3quran.net/tnjy/"
                break

            elif reciter == "16" :

                url = "https://server11.mp3quran.net/a_jbr/"
                break

            elif reciter == "17" :

                url = "https://server6.mp3quran.net/balilah/"
                break

            elif reciter == "18" :

                url = "https://server10.mp3quran.net/jleel/"
                break

            elif reciter == "19" :

                url = "https://server6.mp3quran.net/bsfr/"
                break

            elif reciter == "20" :

                url = "https://server8.mp3quran.net/bu_khtr/"
                break

            elif reciter == "21" :

                url = "https://server8.mp3quran.net/qasm/"
                break

            elif reciter == "22" :

                url = "https://server13.mp3quran.net/jhn/"
                break

            elif reciter == "23" :

                url = "https://server6.mp3quran.net/s_bud/"
                break

            elif reciter == "24" :

                url = "https://server8.mp3quran.net/hani/"
                break

            elif reciter == "25" :

                url = "https://server8.mp3quran.net/jbrl/"
                break

            elif reciter == "26" :

                url = "https://server8.mp3quran.net/bna/"
                break

            elif reciter == "27" :

                url = "https://server8.mp3quran.net/mustafa/"
                break

            elif reciter == "28" :

                url = "https://server6.mp3quran.net/thubti/"
                break

            elif reciter == "29" :

                url = "https://server6.mp3quran.net/wdee3/"
                break

            elif reciter == "30" :

                url = "https://server10.mp3quran.net/qht/"
                break

            else :

                print(f"{color_red}Err102 : Invalid reciter number [Please enter a number from 1 to 30]{color_reset}")
                print("")

        while True :

            while True : 

                try :

                    Nsurah = int(input("Enter the number of the surah in the Quran : "))
                    print("")
                    break

                except ValueError :

                    print("")
                    print(f"{color_red}Err103 : Invalid input [Please enter a number only]{color_reset}")
                    print("")


            if 1 <= Nsurah <= 114 :

                Nsurahint = f"{Nsurah:03}"
                break
            
            else :

                print(f"{color_red}Err104 : Invalid surah number [Please enter a number between 1 and 114]{color_reset}")
                print("")

        while True :

            if option == "1" :

                    try:
                        
                        class MP3Source(miniaudio.StreamableSource) :

                            def __init__(self, url) :
                                self.response = urllib.request.urlopen(url)

                            def read(self, num_bytes) :
                                return self.response.read(num_bytes)

                        source = MP3Source(f"{url}{Nsurahint}.mp3")
                        stream = miniaudio.stream_any(source, miniaudio.FileFormat.MP3)

                        break

                    except Exception  :

                        input(f"{color_red}Err201 : Streaming failed [Check your internet or Wi-Fi connection and try again]{color_reset}")
                        print("")
                        
            else :

                try :

                    script_path = os.path.dirname(os.path.abspath(__file__))


                    file_path = os.path.join(script_path, f"quranPlayerR{reciter}S{Nsurahint}.mp3")

                    print("An audio file is being downloaded...")
                    print("")

                    with urllib.request.urlopen(f"{url}{Nsurahint}.mp3") as response :

                        with open(file_path, "wb") as file :

                            while True :

                                chunk = response.read(65536)

                                if not chunk :

                                    break

                                file.write(chunk)

                    print(f"{color_yellow}A file was downloaded to {file_path}{color_reset}")
                    print("")
                    print(f"{color_yellow}Thank you for using quranPlayer!{color_reset}")
                    print("")
                    user_action = input(f"{color_green}Type 'r' to restart or 'q' to quit : {color_reset}")
                    break

                except Exception :

                        input(f"{color_red}Err202 : Download failed [Check your internet connection, available disk space, and folder write permissions]{color_reset}")
                        print("")


        if option == "1" :
            
            with miniaudio.PlaybackDevice() as device :

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
                        print(f"{color_red}Err105 : Invalid choice [Please enter 'r' to restart or 'q' to quit]{color_reset}")
                        print("")
                        user_action = input(f"{color_green}Type 'r' to restart or 'q' to quit : {color_reset}")
            
except KeyboardInterrupt :

        print("")
        print("")
        print(f"{color_yellow}Thank you for using quranPlayer!{color_reset}")
