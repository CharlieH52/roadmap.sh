from responseManagerClass import ResponseManager
import os

def local_dir():
    pass

username = 'CharlieH52'

repository_name = 'roadmap.sh' 
template_name = 'Python'

event_url = f'https://api.github.com/users/{username}/events'
commit_url = f'https://api.github.com/repos/{username}/{repository_name}/commits'
gitignore_url = f'https://api.github.com/gitignore/templates/{template_name}'

while True:
    print('Please, type your GitHub user name:')
    username = input()
    rm = ResponseManager(username)

    print('Type the number of the ENDPOINT to consult:')
    print('1. Events\n',
          '2. Commit\n',
          '3. gitignore Templates\n'
          )
    option = input()

    if option == '1':
        print('The endpoint is:\n',
              f'{event_url}'
              )
        print('Type the name of new file to export the response:')
        newFile = input()
        
        # Make a human readable json file
        rm.data_catcher(newFile, event_url)


