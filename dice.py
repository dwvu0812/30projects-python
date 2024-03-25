import random


def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []

    for _ in range(amount):
        rolls.append(random.randint(1, 6))

    return rolls


def main():
    while True:
        try:
            user_input = input("Enter the number of dice to roll: ")

            if user_input.lower() == "exit":
                print("Thanks for playing!")
                break
            rolls = roll_dice(int(user_input))
            print(*rolls, sep=", ")
            rolls_sum = sum(rolls)
            print(f"In total, that's: {rolls_sum}")

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue


if __name__ == "__main__":
    main()
