import random


HANGMAN_PICS = [
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    =========
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / 
     |
    =========
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |    
     |
    =========
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |    
     |
    =========
    """,
    """
     ------
     |    |
     |    O
     |    |
     |    
     |
    =========
    """,
    """
     ------
     |    |
     |    O
     |    
     |    
     |
    =========
    """,
    """
     ------
     |    |
     |    
     |    
     |    
     |
    =========
    """
]

# Word lists by difficulty
WORDS = {
    "easy": ["cat", "dog", "bat", "pen", "sun"],
    "medium": ["apple", "house", "train", "chair", "zebra"],
    "hard": ["python", "planet", "wizard", "jungle", "oxygen"]
}

# Scoreboard
wins = 0
losses = 0

def get_word(difficulty):
    return random.choice(WORDS[difficulty]).upper()

def display_hangman(lives):
    print(HANGMAN_PICS[6 - lives])

def play_game():
    global wins, losses

    print("Choose difficulty: easy / medium / hard")
    while True:
        difficulty = input(">> ").strip().lower()
        if difficulty in WORDS:
            break
        else:
            print(" Invalid difficulty. Try again.")

    word = get_word(difficulty)
    guessed = ["_"] * len(word)
    guessed_letters = set()
    lives = 6
    print("\n Let's start! Guess the word letter by letter.")

    while lives > 0:
        display_hangman(lives)
        print("\nWord: ", " ".join(guessed))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        guess = input("Your guess: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Enter a single alphabet only.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(" Good guess!")
            for i, ch in enumerate(word):
                if ch == guess:
                    guessed[i] = guess
            if "_" not in guessed:
                print("🎉 YOU WIN! The word was:", word)
                wins += 1
                break
        else:
            print("❌ Wrong guess!")
            lives -= 1

    if lives == 0:
        display_hangman(lives)
        print("💀 You lost! The word was:", word)
        losses += 1

def show_scoreboard():
    print("\n🏆 SCOREBOARD")
    print("Wins:   ", wins)
    print("Losses: ", losses)

def main():
    print("="*45)
    print("🎯 WELCOME TO THE WORD GUESS HANGMAN GAME 🎯")
    print("="*45)

    while True:
        play_game()
        show_scoreboard()

        again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()
