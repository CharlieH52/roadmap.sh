from ResponseManClass import ResponseManager

while True:
    print('Please, type your GitHub user name:')
    username = input()
    rm = ResponseManager(username)

    print(
        'Type the number of the ENDPOINT to consult:\n',
        '1. Events\n',
        '2. Commit\n'
        )
    option = input()

    if option == '1':
        res = rm.get_user_activity()
        rm.save_response(username, 'Activity', res)

    if option == '2':
        print('Type the name of your repository:')
        rm.repository = input()
        res = rm.get_commit_info()
        rm.save_response(username, f'Commits-{rm.repository}', res)
        

