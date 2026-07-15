# 📖 quranPlayer

A lightweight terminal Quran player that streams or downloads Quran recitations directly from MP3Quran servers.

## Features

* Listen to Quran recitations directly from the terminal
* Download Quran recitations as MP3 files
* Supports multiple famous Quran reciters
* Select any Surah from 1 to 114
* Automatic Surah number formatting (`001.mp3` → `114.mp3`)
* Colorized terminal interface
* Input validation and error handling
* Internet streaming and downloading from MP3Quran servers
* Works on Linux and Windows

## Supported Reciters

* Abdul Basit Abdus Samad
* Mahmoud Khalil Al-Husary
* Mohamed Siddiq Al-Minshawi
* Mishary Rashid Alafasy
* Maher Al-Muaiqly
* Yasser Al-Dosari
* Saad Al-Ghamdi
* Saud Al-Shuraim
* Ahmed Al-Ajmi
* Abdul Rahman Al-Sudais
* Abu Bakr Al-Shatri
* Muhammad Ayyoub
* Nasser Al-Qatami
* Ali Al-Hudhaifi
* Khalifa Al-Tunaiji

## Requirements

* Python 3.x
* miniaudio

## Installation

```bash
git clone https://github.com/MohssineX/quranPlayer.git
cd quranPlayer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install miniaudio
```

## Usage

Run the program:

```bash
python quranPlayer.py
```

If your system uses `python3`:

```bash
python3 quranPlayer.py
```

## Running as an Executable

On Unix-like systems, you can make the script executable and run it directly:

```bash
chmod +x quranPlayer.py
./quranPlayer.py
```

This works because the script includes:

```python
#!/usr/bin/env python3
```

## How It Works

1. Start the program
2. Choose whether to listen online or download an audio file
3. Select your preferred Quran reciter
4. Enter a Surah number (1–114)
5. The application connects to MP3Quran servers
6. The selected Surah is streamed or downloaded
7. Choose to restart the application or quit

## Error Codes

| Code   | Description                                                            |
| ------ | ---------------------------------------------------------------------- |
| err001 | Invalid reciter number                                                 |
| err002 | Invalid input (numbers only)                                           |
| err003 | Invalid Surah number (must be between 1 and 114)                       |
| err004 | Unable to connect to the audio stream (check your internet connection) |
| err005 | Invalid choice (must be `r` or `q`)                                    |

---

## License

This project is licensed under the **[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)**

---

## Acknowledgments

Quran audio streams are provided by the MP3Quran network.

---

## 🐱 Special Thanks

A special thanks to mimi — the legendary, the great, the gentle cat.

---

### If you like it, give it a star :)
