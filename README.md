# Python practice

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Build Status](https://github.com/MianSubhan-Coder/Python/actions/workflows/ci.yml/badge.svg)](https://github.com/MianSubhan-Coder/Python/actions)
[![License](https://img.shields.io/badge/license-Unspecified-lightgrey.svg)]()

A small collection of beginner-friendly Python scripts and exercises by MianSubhan-Coder.

## Repository contents

- `caeser_cipher_encrypt.py`
  - Simple Caesar cipher implementation with a CLI prompt to encrypt or decrypt text by a numeric shift.
  - Usage: `python caeser_cipher_encrypt.py` — follow the prompts to enter text, shift, and action.

- `guess_number.py`
  - Number guessing game (CLI) that chooses a secret number between 1 and 100 and guides the player with higher/lower hints.
  - Usage: `python guess_number.py` — choose Start New Game from the menu.

- `game_snake_water.py`
  - GUI game (Snake / Water / Gun) implemented with Tkinter. First to 5 wins; includes a polished UI and score tracking.
  - Usage: `python game_snake_water.py` (requires a Python installation with tkinter available).

- `listening.py`
  - Small text-to-speech demo using `pyttsx3`. Prompts for text and speaks it aloud.
  - Usage: `python listening.py` (requires the `pyttsx3` package and a working audio setup).

- `my_pyjokes.py`
  - Prints a single joke using the `pyjokes` package.
  - Usage: `python my_pyjokes.py` (requires the `pyjokes` package).

- `main.py`
  - Minimal entrypoint that prints a greeting. Useful as a placeholder or to test Python installation.
  - Usage: `python main.py`.

- `system.py`
  - A larger utilities/UX module which includes banner, console formatting, and helper functions used for nicer CLI output. Inspect the file directly to see available helpers.

## Requirements

Most scripts run on Python 3.8+. Optional dependencies (install with pip):

```
pip install pyjokes pyttsx3
```

Tkinter is included with standard CPython installs on many platforms; on some Linux distributions you may need to install an OS package (e.g., `sudo apt install python3-tk`).

## How to run

1. Clone this repository:

```
git clone https://github.com/MianSubhan-Coder/Python.git
cd Python
```

2. Install optional dependencies if you plan to run `my_pyjokes.py` or `listening.py`.
3. Run any script with `python <script_name>.py`, for example:

```
python guess_number.py
python game_snake_water.py
```

## Contributing

Contributions and suggestions are welcome. If you'd like to add features or fixes:

- Open an issue describing the change you want to make.
- Create a branch, implement your change, and open a pull request.

## Notes

- This repository currently does not include a LICENSE file. If you intend to open-source this project, consider adding a LICENSE (for example, MIT or Apache-2.0).
- If you want, I can also add a simple requirements.txt, a CONTRIBUTING.md, or create a GitHub Actions workflow to run basic checks — tell me which and I will add them.
