# 🎮 Tic-Tac-Toe

## 📚 Table of Contents

- [🎮 Tic-Tac-Toe](#-tic-tac-toe)
- [📚 Table of Contents](#-table-of-contents)
- [📝 Project Summary](#-project-summary)
- [▶️ Usage](#️-usage)
- [🧩 Modular Structure](#-modular-structure)
- [📁 Folder Structure](#-folder-structure)
- [🧱 Breakdown of Components](#-breakdown-of-components)
- [🧠 Game Logic](#-game-logic)
- [🚀 Future Features](#-future-features)

## 📝 Project Summary

A classic Tic Tac Toe game implemented in Python.
This is my **first ever Python project**, designed to be a beginner-friendly introduction to python as a language and scripting with it.

Players take turns placing their symbols (X or O) on a 3x3 grid, aiming to align three in a row-horizontally, vertically, or diagonally. The game runs in the command line and includes full input validation, clean user prompts, and clear win/draw detection.

This project was a great way to practice:
- Python basics and control flow
- Writing modular, maintainable code
- Validating user input
- Building a simple but complete CLI app

> 🎯 Ideal for beginners looking to solidify their understanding of Python and build something fun!

## ▶️ Usage

### Requirements
- Python 3.12 or higher installed on your system

Clone the repository (if you haven't already)

```bash
git clone https://github.com/IbsYoussef/Tic-Tac-Toe.git
cd Tic-Tac-Toe
```

### Run the Game

```bash
python main.py
```

You'll be greeted with a welcome message, asked to choose your symbol (X or O), and shown a position guide to help place your moves. Take turns with another player and try to win!

## 🧩 Modular Structure

This project follows a modular design approach to keep the code clean, maintainable, and easy to understand. Each file is responsible for a specific aspect of the game's logic or display. 

## 📁 Folder Structure

```bash
.
├── README.md
├── game_logic
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── display.cpython-312.pyc
│   │   ├── place_mark.cpython-312.pyc
│   │   ├── user_choice.cpython-312.pyc
│   │   └── win_check.cpython-312.pyc
│   ├── display.py
│   ├── place_mark.py
│   ├── user_choice.py
│   └── win_check.py
└── main.py
```

## 🧱 Breakdown of Components

- **`main.py`**:
    Controls the game loop, manages player turns, and ties all modules together.

- **`display.py`**:
    - `initialise_board()` creates an empty 3x3 board.
    - `display_board()` prints the current board in a clean format.
    - `showPositionGuide()` gives a numbered guide to help players place their mark.

- **`user_choice`**:
    Ensures the player inputs a valid position (1–9) and that the chosen cell isn't already occupied.

- **`place_mark.py`**:
    Handles placing a player's symbol (X or O) on the board at the selected position.

- **`win_check.py`**:
    Contains the core logic for:
     - Checking all possible win conditions (rows, columns, diagonals)
     - Detecting draws when the board is full
     - Reporting whether the game is over

This structure keeps each piece of logic self-contained, which makes it easier to read, test, and update in the future. 

## 🧠 Game Logic

The core gameplay revolves around a loop where players take turns marking positions on a 3x3 grid. Here is how logic flow works:

1. **Board Setup**
    The board is represented as a list of 9 elements (`[' ', ' ', ..., ' ']`)
    - `initialise_board()` creates the empty board
    - `display_board()` shows the current board state after every move.

2. **Player Input**
    - Players are prompted to select a position from 1-9
    - `user_choice()` ensures the input is a digit, within range, and not already taken.

3. **Placing Marks**
    - The player's symbol (`X` or `O`) is placed on the chosen position using `place_mark()`.

4. **Checking for Game Over**
    After every turn, `check_game_over()` is called to determine if the game should end. It checks:
    - Win condition (`check_win()`) — rows, columns, and diagonals
    - Draw condition (`check_draw()`) — full board with no winner

5. **Switching Players**
    If the game isn't over, the current player is switched, and the loop continues.

6. **End Game Output**
    Once a win or draw is detected, a message is displayed declaring the result.

This cycle continues until a win or draw ends the game.

## 🚀 Future Features

Here are a few ideas I'm considering for expanding the project in the future:

- **🔁 Replay Option**
    Allow players to restart the game without restarting the program.

- **🤖 Simple AI opponent**
    Add a computer-controlled opponent for solo play, starting with random moves or basic strategy.

- **📊 Score tracking**
    Keep track of wins, losses, and draws across multiple games in a session. 

- **🎨 Improved Interface**
    Enhance the display with better formatting or even create a GUI using `tkinter` or `pygame`.

- **🧪 Unit Tests**
    Add tests coverage to individual modules like `win_check.py` to ensure stability with future changes.

- **🌐 Web version**
    Rebuild the game as a web app using Flask or frontend framework like React for practice.

Contributions or suggestions are always welcome!