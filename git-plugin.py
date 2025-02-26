#!/usr/bin/env python3
import click
import os
import subprocess
from prompt_toolkit import PromptSession

# The walk_dir function goes through the provided directory and determeins if there is a .git directory, returning either true of false.
def walk_dir(walk_dir):
	for filename in os.listdir(walk_dir):
		filepath = os.path.join(walk_dir, filename)
		if os.path.isdir(walk_dir) == True:
			if os.path.isdir(filepath) and filename == ".git":
				return True
	return False

# Using the subprocess library, to create sub processes that run the git commands with the given repository.
def run_git_commands(repository):
	session = PromptSession()

	subprocess.run(["git", "add", "."], cwd=repository)

	# Check for changes before committing
	result = subprocess.run(["git", "status", "--porcelain"], cwd=repository, capture_output=True, text=True)
	if result.stdout:
		commit_message = session.prompt("Enter commit message: ")
		subprocess.run(["git", "commit", "-m", commit_message], cwd=repository)
	else:
		print("No changes to commit.")
	subprocess.run(["git", "pull"], cwd=repository)
	subprocess.run(["git", "push"], cwd=repository)
	subprocess.run(["git", "push", "--tags"], cwd=repository)

# Run is the main function that will take in the parameters on program start, and will walk through the dir to find the repo.
# If found, it will then run the git commands on that repo.
@click.command()
@click.option('-d', '--dir', default=".", type=str, help="Target path to scan")
def run(dir):
	is_git = walk_dir(dir)
	if is_git is True:
		run_git_commands(dir)

if __name__ == '__main__':
	run()