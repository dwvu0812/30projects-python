from random import choice


def run_game():
    word: str = choice(["apple", "secret", "banana"])

    user_name: str = input("Enter your name: ")
    print(f"Welcome to hangman, {user_name}!")

    guessed: str = ""
    tries: int = 3

    while tries > 0:
        blanks: int = 0
        for char in word:
            if char in guessed:
                print(char, end=" ")
            else:
                print("_", end=" ")
                blanks += 1

        if blanks == 0:
            print("\nYou win!")
            break

        guess = input("\nGuess a letter: ")
        guessed += guess

        if guess not in word:
            tries -= 1
            print(f"Wrong! You have {tries} tries left.")


if __name__ == "__main__":
    run_game()
