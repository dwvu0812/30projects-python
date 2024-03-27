import os


def sort_files(source_path: str):
    """Sorts files based on a given path"""

    # Recursively walk through all the directories and files in the source path
    for root_dir, sub_dir, filenames in os.walk(source_path):
        print(root_dir, " ------ ", sub_dir, " ------- ", filenames)


sort_files("sample")
