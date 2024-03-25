import itertools
import string
import time


def common_guess(word: str) -> str | None:
    with open("word.txt", "r") as file:
        common_words = file.read().splitlines()

    for i, match in enumerate(common_words, start=1):
        if word == match:
            print(f"Common matched: {match} (#{i})")
            return match
    return None


def brute_force(
    word: str, length: int, digits: bool = False, symbols: bool = False
) -> str | None:
    chars: str = string.ascii_lowercase
    if digits:
        chars += string.digits
    elif symbols:
        chars += string.punctuation

    attempts = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess = "".join(guess)
        if guess == word:
            print(f"{word} was craked in {attempts} guesses ")
            return guess


def main():
    print("Searching ...")
    password = "abcdu97"
    start = time.perf_counter()

    if common_match := common_guess(password):
        print(f"Common match: {common_match}")
    else:
        if cracked := brute_force(password, 7, True, True):
            print(f"Password: {cracked}")
        else:
            print("Password not found")
    end = time.perf_counter()
    print(round(end - start, 2), "seconds")


if __name__ == "__main__":
    main()
