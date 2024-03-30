import random

# constants
MAX_GUESSES = 10
GUESS_DIGIT_NUM = 3

def main() -> None:
    while True:
        # secret numbers
        secretNum = get_secretNum(GUESS_DIGIT_NUM)
        num_of_tries = 1

        while num_of_tries <= MAX_GUESSES:
            guess = ""
            while not is_valid_guess(guess, GUESS_DIGIT_NUM):
                print(f"Enter Guess {num_of_tries}")
                guess = input("> ")
            num_of_tries += 1
            clues = get_clues(guess, secretNum)
            print(clues)

            if guess == secretNum:
                break
            if num_of_tries > MAX_GUESSES:
                print("you have exhausted your number of tries")
                print(f"the answer was {secretNum}")
        print("Do you want to play again? (yes or no)")
        ans = input("> ")
        if not ans.lower().startswith("y"):
            break
    print("Thanks for playing!!")


def get_secretNum(GUESS_DIGIT_NUM: int) -> str:
    """Returns a string of 3 random numbers without repetition"""
    nums = list("0123456789")
    random.shuffle(nums)
    res = ""
    for i in range(GUESS_DIGIT_NUM):
        res += nums[i]
    return res


def is_valid_guess(guess: str, GUESS_DIGIT_NUM: int) -> bool:
    """checks it a guess is valid or not"""
    if len(guess) == GUESS_DIGIT_NUM and guess.isdigit():
        if guess[0] == guess[1] or guess[0] == guess[2] or guess[1] == guess[2]:
            print("all digits should be unique")
            return False
        return True
    return False


def get_clues(guess: str, secretNum: str) -> str:
    """compares the user input to the secret number and returns clues to get te answer right"""
    clues = []
    if guess == secretNum:
        return "You got it"
    else:
        for i in range(len(secretNum)):
            if guess[i] == secretNum[i]:
                clues.append("Fermi")
            elif guess[i] in secretNum:
                clues.append("Pico")
        clues.sort()

    if len(clues) == 0:
        return "Bagels"

    return " ".join(clues)


if __name__ == "__main__":
    main()
