#!/usr/bin/env python3

import json
import os
import requests
import sys
import subprocess


class MainProcess:
    '''Create repository on Github and Init/Push local repo with switch branch on develop'''

    GITHUB_TOKEN = "GITHUB_PRIVATE_TOKEN"
    GITHUB_URL = "https://api.github.com/user/repos"
    GITHUB_REPO_NAME = '{{cookiecutter.project_slug}}'
    GITHUB_CLONE_URL = ''

    def __init__(self, *args, **kwargs):
        try:
            self.private_token = os.environ[self.GITHUB_TOKEN]
        except KeyError:
            sys.exit(f"\nThe environment variable '{self.GITHUB_TOKEN}' is missing.\n Try to run before this: export GITHUB_PRIVATE_TOKEN=YOUR_GITHUB_TOKEN")

    def create_remote_repository(self, *args, **kwargs):
        try:
            headers = {"Authorization": f"token {self.private_token}"}
            data = {
                "name": self.GITHUB_REPO_NAME,
                "private": True,
            }
            github_repo = requests.post(self.GITHUB_URL, headers=headers, data=json.dumps(data))
            self.GITHUB_CLONE_URL = github_repo.json()['clone_url']
            print(f"\nRepository on Github was create succesfully!")
        except BaseException:
            sys.exit("The repository was not created.")

    def init_local_repository(self, *args, **kwargs):
        os.system(f"./scripts/git_init.sh {self.GITHUB_CLONE_URL}")
        print(f"\nRepository is initialized and create first commit!")

    def clean_files(self, *args, **kwargs):
        os.system(f"./scripts/clean_files.sh")
        print(f"\nCleaning completed!")


# if __name__ == "__main__":
#     main_process = MainProcess()
#     main_process.create_remote_repository()
#     main_process.init_local_repository()
#     main_process.clean_files()
