from distutils.dir_util import copy_tree
from git import Repo
import os
import webbrowser
import shutil

cc_work_folder = "/Users/needs_replaced/Desktop/codeclan_work/"


def get_day():
    day = input("What day is it? (1, 2, 3, 4, 5) ")
    return day


def get_two_digit_week():
    week = input("What week is it? (1 - 16) ")
    two_digit_week = f"{int(week):02d}"
    return two_digit_week


def get_cwd():
    directory_to_copy = os.getcwd()
    return directory_to_copy


def get_current_directory_name(directory_to_copy):
    directory_name = os.path.basename(directory_to_copy)
    return directory_name


def get_path_to_copy_to(day, two_digit_week, directory_name):
    if day == "5":
        destination_directory = (
            f"{cc_work_folder}week_{two_digit_week}/weekend_homework"
        )
    else:
        destination_directory = f"{cc_work_folder}week_{two_digit_week}/day_{day}"
    copy_to_path = f"{destination_directory}/{directory_name}"

    return copy_to_path


def get_repo_name(day, two_digit_week, directory_name):
    repo_name = f"week_{two_digit_week}_day_{day}_{directory_name}"


def copy_folder(directory_to_copy, copy_to_path):
    copy_tree(directory_to_copy, copy_to_path)


def make_readme(directory):
    os.chdir(directory)
    for file in os.listdir(directory):
        if file.endswith(".md"):
            os.rename(file, "readme.md")


def init_repo(copy_to_path):
    repo = Repo.init(copy_to_path)
    repo.git.add("--all")
    repo.git.commit("-m", "Initial commit", "--no-verify")
    return repo


def create_gh_repo(copy_to_path):
    os.chdir(copy_to_path)
    create_command = f"gh repo create --public -y"
    os.system(create_command)
    repo = Repo(copy_to_path)
    repo.heads.master.rename("main")
    repo.git.push("--set-upstream", "origin", "main")


def open_code(path):
    os.chdir(path)
    os.system("code .")


def main():

    day = get_day()
    week = get_two_digit_week()
    directory_name = get_current_directory_name(get_cwd())
    source = get_cwd()
    destination = get_path_to_copy_to(day, week, directory_name)

    copy_folder(source, destination)
    make_readme(destination)
    init_repo(destination)
    create_gh_repo(destination)
    open_code(destination)


if __name__ == "__main__":
    main()