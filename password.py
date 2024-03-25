import string
import secrets


def generate_password(length: int, contain_symbol: bool, contain_upper: bool) -> str:
    combination = string.ascii_lowercase + string.digits

    if contain_symbol:
        combination += string.punctuation
    if contain_upper:
        combination += string.ascii_uppercase

    combinationLength = len(combination)
    newPassword: str = ""

    for _ in range(length):
        newPassword += combination[secrets.randbelow(combinationLength)]

    return newPassword


if __name__ == "__main__":
    print(generate_password(10, True, True))
    print(generate_password(10, False, True))
    print(generate_password(10, True, False))
    print(generate_password(10, False, False))
