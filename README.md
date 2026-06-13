# 🎯 Hangman Word Guessing Game

A interactive CLI-based **Hangman Word Guessing Game** written in Python. Test your vocabulary skills across three levels of difficulty and track your wins and losses with the built-in scoreboard!

---

## 🚀 Features

- **🎮 Dynamic Difficulty Levels**: Choose between `Easy`, `Medium`, and `Hard` words.
- **🎨 Interactive ASCII Graphics**: Visual hangman representation updating dynamically with each incorrect guess.
- **🏆 Live Scoreboard**: Tracks your total wins and losses throughout the session.
- **⚠️ Smart Input Validation**: Prevents duplicate guesses, multi-character entries, and invalid (non-alphabetic) characters.
- **🔁 Endless Play**: Option to replay instantly after a win or loss without losing your scoreboard status.

---

## 🛠️ Requirements

- **Python 3.6+** (No external dependencies required, uses standard libraries)

---

## 🕹️ How to Play

1. Run the game in your terminal (see instructions below).
2. Choose your preferred difficulty:
   - **Easy**: 3-letter words (e.g., *cat*, *sun*)
   - **Medium**: 5-letter words (e.g., *apple*, *chair*)
   - **Hard**: 6-letter words (e.g., *python*, *wizard*)
3. Guess one letter at a time to reveal the hidden word.
4. You start with **6 lives**. Each incorrect guess costs you a life and builds the hangman.
5. Win the game by guessing all the letters before running out of lives!

---

## 💻 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/KomalParmar-codes/Wordguess--Game.git
cd Wordguess--Game
```

### 2. Run the game
```bash
python main.py
```

---

## 📸 Sample Gameplay

```text
=============================================
🎯 WELCOME TO THE WORD GUESS HANGMAN GAME 🎯
=============================================
Choose difficulty: easy / medium / hard
>> medium

 Let's start! Guess the word letter by letter.

     ------
     |    |
     |    
     |    
     |    
     |
    =========

Word:  _ _ _ _ _
Guessed letters:
Your guess: a

 Good guess!
...
```

---

## 📂 Project Structure

```text
├── .gitignore         # Ignores system and environment cache files
├── README.md          # Project documentation (this file)
└── main.py            # Main game source code
```

---


