import random

# constants
MAX_GUESSES = 10
GUESS_DIGIT_NUM = 3


def main():
    while True:
        # secret numbers
        secret_num = get_secret_num(GUESS_DIGIT_NUM)
        num_of_tries = 1

        while num_of_tries <= MAX_GUESSES:
            guess = ""
            while not is_valid_guess(guess, GUESS_DIGIT_NUM):
                print(f"Enter Guess {num_of_tries}")
                guess = input("> ")
            num_of_tries += 1
            clues = get_clues(guess, secret_num)
            print(clues)

            if guess == secret_num:
                break
            if num_of_tries > MAX_GUESSES:
                print("you have exhausted your number of tries")
                print(f"the answer was {secret_num}")
        print("Do you want to play again? (yes or no)")
        ans = input("> ")
        if not ans.lower().startswith("y"):
            break
    print("Thanks for playing!!")


def get_secret_num(GUESS_DIGIT_NUM: int) -> str:
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
        guess_arr = [i for i in guess]
        # check if we have any repeating number
        for a, single_guess_A in enumerate(guess_arr):
            for single_guess_B in guess_arr[a + 1 :]:
                if single_guess_A == single_guess_B:
                    print("all digits should be unique")
                    return False
        return True
    return False


def get_clues(guess: str, secret_num: str) -> str:
    """compares the user input to the secret number and returns clues to get te answer right"""
    clues = []
    if guess == secret_num:
        return "You got it"
    else:
        for i in range(len(secret_num)):
            if guess[i] == secret_num[i]:
                clues.append("Fermi")
            elif guess[i] in secret_num:
                clues.append("Pico")
        clues.sort()

    if len(clues) == 0:
        return "Bagels"

    return " ".join(clues)


if __name__ == "__main__":
    main()
