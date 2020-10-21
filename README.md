# Copy_lab

This a wee script to copy the codeclan lab from the class notes folder to your codeclan_work folder in the correct week/day format.  

It will also initialise a git repository, create an initial commit and, if given a remote repo, push to GitHub.

### I take no responsibilty if it all goes wrong.

## Setup instructions:

1. Download zip/ clone repo to your machine.
2. Unzip if you need to.
3. In a terminal, navigate to where setup.sh directory is.
4. Enter "chmod +x setup.sh" in the terminal.
5. Enter "./setup.sh" in the terminal.

## Usage instructions

This assumes that your codeclan_work folder is on your Desktop.

There's no error checking on your input, but you can always delete it if you eneter the wrong day/week etc.

1.  Navigate inside the directory you want to copy to your codeclan_work folder.  If you wanted to copy the folder "homework_lab", you need to be inside it.
2. Type "copy_lab" at the command prompt
3. It will ask you for a day, this should be wbetween 1 and 5, with 1 being Monday. 5 will create a folder called weekend_homework.
4. It will ask you for the week, this should be a number between 1 and 16.
5. It will ask you for a SSH link to a repository.  This should be copied from GitHub in the form of git@github.com etc.  Just leave it blank if you haven't created one yet.
6. It should copy the folder.
