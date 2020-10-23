# Copy_lab

This a wee script to copy the codeclan lab from the class notes folder to your codeclan_work folder in the correct week/day format.

  * Copy the current folder to your codeclan_work folder in the correct day/week format
  * Take any .md file and rename it readme.md
  * Initialise a git repository
  * Commit the initial files
  * Create a repository on GitHub
  * Link the two repositories
  * Push the commit to GitHub
  * Open VS Code in the correct folder

### I take no responsibilty if it all goes wrong.

## Pre-requisite:

We need the GitHub cli to be installed before we can create repositories automatically. To install and set this up follow the following:
1. Enter "brew install gh" in a terminal.
2. Authenticate to your GitHub account using "gh auth login" and follow the prompts.
3. Select the SSH option as your default protocol.

## Setup instructions:

1. Download zip/ clone repo to your machine.
2. Unzip if you need to.
3. In a terminal, navigate to where setup.sh directory is.
4. Enter "chmod +x setup.sh" in the terminal.
5. Enter "./setup.sh" in the terminal.

## Usage instructions

This assumes that your codeclan_work folder is on your Desktop.

There's no error checking on your input, but you can always delete it if you enter the wrong day/week etc.

1.  Navigate inside the directory you want to copy to your codeclan_work folder.  If you wanted to copy the folder "homework_lab", you need to be inside it.
2. Type "copy_lab" at the command prompt
3. It will ask you for a day, this should be between 1 and 5, with 1 being Monday. 5 will create a folder called weekend_homework.
4. It will ask you for the week, this should be a number between 1 and 16.
5. It will prompt for a repository name. Hit enter to accept the default (the current directory name)
