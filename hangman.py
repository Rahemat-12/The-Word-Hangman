import random

# List of words for the game
word_list = ["rossum", "hangman", "challanges", "programming", "console", "computer"]

def play_hangman():
# Randomly choose a word from the list
    word = random.choice(word_list)
    guessed_word = ["_" for _ in word]
    guessed_letters = set()
    tries = 6

    print("Let's play Hangman!")

    while tries > 0:
        print("Word: ", " ".join(guessed_word))
        print(f"Tries left: {tries}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        # Get a valid guess from the player
        while True:
            guess = input("Enter a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                break
            print("Invalid input. Please enter a single letter.")

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            if "_" not in guessed_word:
                print(f"Congratulations! You guessed the word : {word}")
                break
        else:
            tries -= 1
            if tries == 0:
                print(f"Game over! The word was: {word}")
                break

while True:
    play_hangman()
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again in ('y', 'n'):
            break
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")
    if play_again == 'n':
        break
