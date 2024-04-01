"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, math, simulation"""

import datetime, random

def get_birthdays(number_of_birthdays):
    """Returns a list of number random date objects of birthdays"""
    birthdays = []
    for i in range(number_of_birthdays):
        start_of_year = datetime.date(2001, 1, 1)

        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays

def get_match(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthdays list"""
    if len(birthdays) == len(set(birthdays)):
        return None
    
    for a, birthday_A in enumerate(birthdays):
        for birthday_B in birthdays[a + 1 :]:
            if birthday_A == birthday_B:
                return birthday_A

print("""
Birthday Paradox, by Al Sweigart al@inventwithpython.com

The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.
(It's not actually a paradox, it's just a surprising result.)
""")

MONTHS = ('Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Sep', 'Oct', 'Nov', 'Dec',)
while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        num_b_days = int(response)
        break
print()

print(f'Here are {num_b_days}, birthdays: ')
birthdays = get_birthdays(num_b_days)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(", ", end="")

    month_name = MONTHS[birthday.month - 1]
    date_text = f'{month_name} {birthday.day}'
    print(date_text, end="")
    
print()
print()

match = get_match(birthdays)

print("In this simulation, ", end="")
if match != None:
    monothName = MONTHS[match.month - 1]
    date_text = f"{month_name} {match.day}"
    print(f"multiple people habve a birthday on {date_text}")
else:
    print("there are no matching birthdays.")
print()

print('Generating', num_b_days, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print("Let's run another 100,000 simulations, ")
sin_match = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, " simulations run...")
    birthdays = get_birthdays(num_b_days)
    if get_match(birthdays) != None:
        sin_match = sin_match + 1
print('100,000 simulations run.')

probability = round(sin_match / 100_000 * 100, 2)
print(f"Out of 100,000 simulations of {num_b_days} people, there was a")
print(f"matching birthday in that group {sin_match} times. This means")
print(f"that {num_b_days} peaople hava a {probability}% chance of")
print("having a maching birthday in their group.")
print("That's probably more than you would think!")

# print(get_birthdays(2))