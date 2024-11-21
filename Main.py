import random
from Words import get_words
from Displayer import show_execute, display_current_state

def squash():
    word_list = get_words()
    word = random.choice(word_list)
    guessed_letters = set()
    tries = 6
    game_over = False
    print("Welcome to the game!")

    while not game_over:
        print(show_execute(tries))
        print(f"Word: {display_current_state(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue
        if guess in guessed_letters:
            print("You have already guessed that letter!")
            continue
        guessed_letters.add(guess)
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry the {guess} is not in the word.")
            tries -= 1

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You have guess the word '{word}'")
            game_over = True

        if tries == 0:
            print(show_execute(tries))
            print(f"Game Over! The word was: '{word}'")
            game_over = True

if __name__ == "__main__":
    squash()
