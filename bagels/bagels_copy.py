"""
Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-python-projects
A version of this game is featured in the book "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle
"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(
        f"""
        Bagels, a deductive logic game.
        By Al Sweigart al@inventwithpython.com

        I am thinking of a {NUM_DIGITS}-digit number with no repeated digits. Try to guess what it is. Here are some clues:
        When I say:     That means:
        Pico            One digit is correct but in the wrong position.
        Fermi           One digit is correct and in the right position.
        Bagels          No digit is correct.

        For example, if the secret number was 248 and your guess was 843, the
        clues would be Fermi Pico.
    """
    )

    while True:
        secretNum = getSingleNum()
        print("I have thought up a number.")
        print(f" You have {MAX_GUESSES} guesses to get it.")

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numGuesses}")
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("You ran out od guesses.")
                print(f"The answer was {secretNum}")

        print("Do you want to play again? (yes or no) ")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing")


def getSingleNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list("0123456789")
    random.shuffle(numbers)
    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    73. and secret number pair."""
    if guess == secretNum:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)


if __name__ == "__main__":
    main()
