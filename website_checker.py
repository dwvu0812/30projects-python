import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus


def get_websites(csv_path: str) -> list[str]:
    websites = []
    with open(csv_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if "https://" not in row[1]:
                websites.append(f"https://{row[1]}")
            else:
                websites.append(row[1])

    return websites


# print(get_websites("websites.csv"))


def get_user_agent() -> str:
    ua = UserAgent()
    return ua.chrome


# print(get_user_agent())


def get_status_description(status_code: int) -> str:
    for status in HTTPStatus:
        if status.value == status_code:
            description: str = f"({status} {status.name}) {status.description}"
            return description

    return "Status code not found"


def check_website(website: str, user_agent):
    try:
        code: int = requests.get(
            website, headers={"User-Agent": user_agent}
        ).status_code
        print(website, get_status_description(code))
    except Exception:
        print(f"Could not get information from website: {website}")


def main():
    sites = get_websites("websites.csv")
    user_agent = get_user_agent()
    for site in sites:
        check_website(site, user_agent)


if __name__ == "__main__":
    main()
