# git-plugin-python
A simple git plugin utilizing python to automate the git pull, and git push commands on discovered repos.

#### Setting up required libraries:
1.Run "pip install click" to install the click package as this project utilizes it.

#### Setting up git plugin on Linux environment:
1. Create an executable with the same name as the project with "cp git-plugin.py git-plugin"
2. Provide the executable with the correct permissions "chmod a+x ./git-plugin"
3. Move the executable to $PATH to run it without needing to provide the path, "sudo mv ./git-plugin /usr/bin/git-plugin"

#### Running the project:
1. Add and commit files for your git repo.
2. 
    a) Run the git-plugin.py file with "python3 git-plugin.py --dir your-repo-path" </br>
    b) (IF you followed the setup for Linux) Run the script in a command line with "git plugin --dir your-repo-path"

#### Reference:
https://joshburns-xyz.vercel.app/posts/build-your-own-git-plugin
