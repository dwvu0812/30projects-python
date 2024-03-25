import os
import requests


def get_extension(url):
    extensions = [".jpg", ".jpeg", ".png", ".gif"]

    for ext in extensions:
        if ext in url:
            return ext


def download_image(url, name, folder: str = None):
    if ext := get_extension(url):
        if folder:
            image_name = f"{folder}/{name}{ext}"
        else:
            image_name = f"{name}{ext}"
    else:
        raise Exception("Invalid URL")

    if os.path.isfile(image_name):
        raise Exception(f"{image_name} already exists.")

    # download the image
    try:
        image_content: bytes = requests.get(url).content
        with open(image_name, "wb") as f:
            f.write(image_content)
            print(f"{image_name} downloaded successfully.")
    except Exception as e:
        print(f"Error downloading {image_name}: {e}")


if __name__ == "__main__":
    input_url = input("Enter the image URL: ")
    input_name = input("Enter the image name: ")
    print("Downloading...")
    download_image(input_url, input_name, "images")
