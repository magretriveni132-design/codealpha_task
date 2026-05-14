import random

# Words list
words = ["python", "apple", "chair", "table", "mouse"]

# Random word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

display_word = ["_"] * len(word)

# Hangman stages (visual)
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

print("🎮 Welcome to Hangman Game!")

while True:

    # 🔴 LOSE CHECK (TOP PE HI)
    if incorrect_guesses >= max_attempts:
        print(hangman_stages[incorrect_guesses])
        print("\n💀 You LOST! The word was:", word)
        break

    # 🟢 WIN CHECK (TOP PE HI)
    if "_" not in display_word:
        print("\n🎉 You WIN! The word was:", word)
        break

    print(hangman_stages[incorrect_guesses])
    print("Word:", " ".join(display_word))
    print("Attempts left:", max_attempts - incorrect_guesses)
    print("Guessed letters:", ", ".join(guessed_letters))

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Enter only ONE letter!")
        continue

    if guess in guessed_letters:
        print("⚠️ Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("❌ Wrong!")
        incorrect_guesses += 1

        # 🔴 LOSE CHECK
        if incorrect_guesses >= max_attempts:
            print(hangman_stages[incorrect_guesses])
            print("\n💀 You LOST! The word was:", word)
            break