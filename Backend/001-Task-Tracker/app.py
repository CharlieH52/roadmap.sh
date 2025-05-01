from taskManager import TaskManager
from taskClass import Task
from os import system

def clear():
    system('cls')

tm = TaskManager()

while True:
    print('Task manager')
    print('What do you want to do?')
    print('1. Add task')
    print('2. Update task')
    print('3. Delete task')
    print('4. List tasks')
    print('Press the number of the option or e to exit')
    value = input()

    if value == '1':
        clear()
        id = tm.generate_id()
        addDate = f'{tm.get_today_date()}'
        print('Type the name of your task:')
        title = input()
        print('The default state of your task is "Unstarted"')
        status = 'Unstarted'
        print('Type the description for your task:')
        description = input()
        taskObj = Task(id=id, title=title, addDate=addDate, status=status, description=description)
        task = taskObj.to_dict()
        tm.add_task(task)

    if value == '2':
        clear()
        print('Type the id for update the task:')
        idTask = input()
        newDate = f'{tm.get_today_date()}'
        data = tm.catch_task(idTask)
        while True:
            clear()
            print('This is the information of your task:\n',
                  f'ID: {data["id"]}\n',
                  f'Add date: {data["addDate"]}\n',
                  f'Title: {data["title"]}, Status: {data["status"]}\n',
                  f'Description: {data["description"]}\n'
                  f'Last update: {data["upDate"]}\n'
                  )
            print('Chose the option to edit:\n',
                  '1. Rename title\n',
                  '2. Change status\n',
                  '3. Edit description\n',
                  'S. Save the changes\n',
                  'Type e or E to cancel'
                  )
            option = input()

            if option == '1':
                print('Type the new title for your task:')
                title = input()
                data['title'] = title

            if option == '2':
                while True:
                    clear()
                    print('Type the number of the option.\n',
                        'Change the status for your task:\n',
                        '1. ToDo\n',
                        '2. Started\n',
                        '3. Done\n'
                        'e or E to exit.'
                        )
                    status = input()
                    if status == '1':
                        data['status'] = 'ToDo'
                        break
                    
                    if status == '2':
                        data['status'] = 'Started'
                        break

                    if status == '3':
                        data['status'] = 'Done'
                        break

                    if status == 'e' or status == 'E':
                        break

            if option == '3':
                print('Type a new description for your task:')
                description = input()
                data['description'] = description

            if option == 's' or option == 'S':
                data['upDate'] = newDate
                tm.update_task(idTask, data)
                break
            
            if option == 'e' or option == 'E':
                break

    if value == '3':
        clear()
        print('Type the ID of the task to delete.')
        taskID = int(input())
        tm.delete_task(taskID)
        print('Task has been deleted.')

    if value == '4':
        clear()
        tm.list_tasks()

    if value == "E" or value == "e":
        break