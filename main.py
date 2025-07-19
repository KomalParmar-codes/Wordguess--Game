def play_game():
  import random

# Step 1: Creating a word bank 
  word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi','aura','stranger things']
  word = random.choice(word_bank)

# Step 2: Setup Game State
  guessedWord = [' ' if char == ' ' else '_' for char in word]
  hangman_art = ['''                    +----------+
                    |          |
                               |
                               |
                               |
                               |
                               | ''',
                '''                     +----------+
                    |          |
                    o          | 
                               |
                               |
                               |
                               | ''',
                '''                      +----------+
                    |          |
                    o          | 
                    |          |
                               |
                               |
                               |   ''',
                '''                      +----------+
                    |          |
                    o          | 
                   /|          |
                               |
                               |
                               | ''',
                '''                       +----------+
                    |          |
                    o          | 
                   /|\         |
                               |
                               |
                               |  ''',
                '''                        +----------+
                    |          |
                    o          | 
                   /|\         |
                    |          |
                               |
                               |  ''',
                '''                         +----------+
                    |          |
                    o          | 
                   /|\         |
                   /|          |
                               |
                               |  ''',
                '''                          +----------+
                    |          |
                    o          | 
                   /|\         |
                   /|\         |
                               |
                               |  '''            ]

  max_attempts = len(hangman_art)-1
  attempts = max_attempts

# Step 3: Game Loop 
  print("🎮 Welcome to the Word Guess Game! 🎮")
  print("Guess the word, one letter at a time!")

  while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord))
    print(hangman_art[max_attempts-attempts])
    guess = input('Guess a letter: ').lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter only a single letter.")
        continue

    if guess in guessedWord:
        print("⚠️ You already guessed that letter!")
        continue

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('✅ Great guess!')
    else:
        attempts -= 1
        print('❌ Wrong guess! Attempts left: ' + str(attempts))

    if '_' not in guessedWord:
        print('\n🎉 Congratulations!! You guessed the word: ' + word)
        break

# Step 4: End Game 
  if attempts == 0 and '_' in guessedWord:
    print('\n😢 You\'ve run out of attempts! The word was: ' + word)

while True:
    play_game()
    again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
    if again != 'yes':
        print("\n👋 Thanks for playing! See you again!")
        break
