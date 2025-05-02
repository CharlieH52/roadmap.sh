import os
import urllib
import urllib.request
import urllib.error
import json

workingPath = os.getcwd()
projectPath = os.path.join(workingPath, r'Backend\002-GitHub-Activity')
localStorage = os.path.join(projectPath, 'localstorage')
 
class ResponseManager:
    def __init__(self, username, repository = None):
        self.username = username
        self.repository = repository

    def save_response(self, fileName, ref, response):
        fileOut = os.path.join(localStorage,f'{fileName}-{ref}.json')
        try:
            with open(fileOut, "w") as file:
                json.dump(response, file, indent=4)
        except OSError as e:
            print(e)

    def data_catcher(self, url):
        req = urllib.request.Request(url, headers={"User-Agent": "PythonApp"})
        try:
            with urllib.request.urlopen(req) as response:
                data = response.read()
                response =  json.loads(data)
            return response

        except urllib.error.HTTPError as e:
            print(e)

        except urllib.error.URLError as e:
            print(e)

    def get_commit_info(self):
        commit_url = f'https://api.github.com/repos/{self.username}/{self.repository}/commits'
        return self.data_catcher(url=commit_url)

    def get_user_activity(self):
        event_url = f'https://api.github.com/users/{self.username}/events'
        return self.data_catcher(url=event_url)