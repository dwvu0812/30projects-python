# def get_input(word: str) -> str:
#     user_input: str = input(f"Enter {word}: ")
#     return user_input


# a = get_input("name")

# print(type(a))

from random import randint

lower_num, upper_num = 1, 10
random_num = randint(lower_num, upper_num)

print(f"Guess a number between {lower_num} and {upper_num}:")

while True:
    try:
        user_guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number")
        continue

    if user_guess == random_num:
        print("You guessed correctly!")
        break
    elif user_guess < random_num:
        print("Guess higher")
    else:
        print("Guess lower")
