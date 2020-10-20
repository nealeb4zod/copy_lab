from distutils.dir_util import copy_tree
from git import Repo
import os
import webbrowser

week = input("What week is it? (1 - 16) ")
day = input("What day is it? (1, 2, 3, 4, 5) ")
url = input("SSH link to repository (leave blank if no link): ")

two_digit_week = f"{int(week):02d}"

cc_work_folder = "/Users/needs_replaced/Desktop/codeclan_work/"
directory_to_copy = os.getcwd()
directory_name = os.path.basename(directory_to_copy)

if day == "5":
    destination_directory = f"{cc_work_folder}week_{two_digit_week}/weekend_homework"
else:
    destination_directory = f"{cc_work_folder}week_{two_digit_week}/day_{day}"
new_path = f"{destination_directory}/{directory_name}"
copy_tree(directory_to_copy, new_path)

repo = Repo.init(new_path)
repo.git.add("--all")
repo.git.commit("-m", '"Initial commit"', "--no-verify")

if not url:
    webbrowser.open("https://github.com/new", new=2)
else:
    origin = repo.create_remote("origin", url)
    repo.create_head("main")
    repo.git.push("--set-upstream", "origin", "main")
