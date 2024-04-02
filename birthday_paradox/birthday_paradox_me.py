import datetime
import random

MONTHS = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
)


def main() -> None:
    print("Enter the number of peaople in the room", end="")
    while True:
        num_b = input("> ")
        if num_b.isdecimal() and (0 < int(num_b) <= 100):
            break
    birthdays = get_birthdays(int(num_b))
    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(", ", end=" ")
        month_name = MONTHS[birthday.month - 1]
        date_text = f"{month_name} {birthday.day}"
        print(date_text, end="")

    print()
    print()

    match = get_match(birthdays)

    print("in this simulation there are ", end="")
    if match is not None:
        match_month = MONTHS[match.month - 1].lower()
        date_text = f"{match_month} {match.day}"
        print(f"multiple people habve a birthday on {date_text}")
    else:
        print("no matching birthdays")

    print()

    print("Generating", num_b, "random birthdays 100,000 times...")
    input("Press Enter to begin...")

    print("Let's run another 100,000 simulations, ")
    sin_match = 0
    for i in range(100_000):
        if i % 10_000 == 0:
            print(i, " simulations run...")
        birthdays = get_birthdays(int(num_b))
        if get_match(birthdays) is not None:
            sin_match = sin_match + 1
    print("100,000 simulations run.")

    probability = round(sin_match / 100_000 * 100, 2)
    print(f"Out of 100,000 simulations of {num_b} people, there was a")
    print(f"matching birthday in that group {sin_match} times. This means")
    print(f"that {num_b} peaople hava a {probability}% chance of")
    print("having a maching birthday in their group.")
    print("That's probably more than you would think!")


def get_birthdays(num_of_birthdays: int) -> list[datetime.date]:
    """Returns a list of random dates in a year"""
    birthdays = []

    for i in range(num_of_birthdays):
        start_of_year = datetime.date(2001, 1, 1)

        random_number_of_days = datetime.timedelta(random.randint(0, 366))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)

    return birthdays


def get_match(birthdays: list[datetime.date]):
    """Finds who has the same birthday as you"""
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthday_A in enumerate(birthdays):
        for birthday_B in birthdays[a + 1 :]:
            if birthday_A == birthday_B:
                return birthday_A


main()
