def check_password(password):
    with open("password.txt", "r") as file:
        common_passwords = file.read().splitlines()

    for i, common_password in enumerate(common_passwords, start=1):
        if password == common_password:
            print(f"password: ❌ (# {i})")
            return
    print("password: ✅ unique!")


def main():
    password = input("Enter your password: ")
    check_password(password)


if __name__ == "__main__":
    main()
