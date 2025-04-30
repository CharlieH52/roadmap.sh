import os
import urllib
import urllib.request
import urllib.error
import json

workingPath = os.getcwd()
projectPath = os.path.join(workingPath, r'Backend\002-GitHub-Activity')
localStorage = os.path.join(projectPath, 'localstorage')

class ResponseManager:
    def __init__(self, username):
        self.username = username

    def make_new_file(self, name, data):
        fileOut = os.path.join(localStorage,f'{name}.json')
        with open(fileOut, "w") as file:
            json.dump(data, file, indent=4)

    def data_catcher(self, fileName, url):
        req = urllib.request.Request(url, headers={"User-Agent": "PythonApp"})
        try:
            with urllib.request.urlopen(req) as response:
                data = response.read()
                output =  json.loads(data)
                self.make_new_file(fileName, output)

        except urllib.error.HTTPError as e:
            print(e)

        except urllib.error.URLError as e:
            print(e)

    def read_information(self):
        
        pass