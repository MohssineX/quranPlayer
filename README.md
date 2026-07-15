# quranPlayer

![Python](https://img.shields.io/badge/python-3-blue) ![License: GPL](https://img.shields.io/badge/license-GPL-blue)

A command-line tool for streaming or downloading Quran recitations in Arabic, with a choice of fifteen reciters.

## Description

quranPlayer is an interactive terminal application written in Python. It lets the user pick a reciter and a surah number, then either stream the audio directly through the speakers or download it as an MP3 file to the local machine. Audio streaming is handled by the `miniaudio` library, and files are fetched from `mp3quran.net` servers using `urllib`. The interface is menu-driven and uses colored terminal output.

## Features

- Stream a chosen surah online without saving it to disk
- Download a chosen surah as an MP3 file to the script's directory
- Choose from fifteen reciters, including Abdul Basit Abdus Samad, Mishary Rashid Alafasy, and Abdul Rahman Al-Sudais
- Select any surah by its number (1 to 114)
- Restart the session or quit after each playback or download
- Colored terminal output using ANSI escape codes, with automatic enabling on Windows
- Input validation with descriptive error messages for invalid options, non-numeric input, out-of-range surah numbers, and network failures

## Requirements

- Python 3
- An internet connection, for both streaming and downloading

## Installation

Clone the repository and install its dependencies:

```bash
git clone https://github.com/MohssineX/quranPlayer.git
cd quranPlayer
pip install -r requirements.txt
```

The only dependency is the `miniaudio` library, used for decoding and playing the streamed MP3 audio.

## Usage

Run the script from the project directory:

```bash
python quranPlayer.py
```

The program then guides the user through a series of prompts in the terminal to select an action, a reciter, and a surah.

## How it works

1. Press Enter to start.
2. Choose whether to listen to the Quran online or download an audio file.
3. Choose one of the fifteen available reciters.
4. Enter the surah number (1 to 114).
5. The program either streams the audio through `miniaudio.PlaybackDevice`, or downloads it in chunks and saves it as `quranPlayerR<reciter>S<surah>.mp3` next to the script.
6. After playback or download finishes, choose to restart (`r`) or quit (`q`).

## Troubleshooting

| Code | Meaning |
|---|---|
| `err001` | The entered reciter number does not exist |
| `err002` | The entered surah number is not a valid integer |
| `err003` | The entered surah number is outside the 1-114 range |
| `err004` | Could not reach the audio server; check the internet connection |
| `err005` | The restart/quit choice was neither `r` nor `q` |

## License

This project is licensed under the GPL license. See the [LICENSE](LICENSE) file in the repository for the exact version and full terms.

## Acknowledgments

Audio files are served by [mp3quran.net](https://mp3quran.net).
