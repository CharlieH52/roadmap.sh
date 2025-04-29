from taskManager import TaskManager
from taskClass import Task
from os import system

def clear():
    system('cls')

tm = TaskManager()

tm.folder_task()
tm.task_lib_checker()

while True:
    print('Task manager')
    print('What do you want to do?')
    print('1. Add task')
    print('2. Update task')
    print('3. Delete task')
    print('4. List tasks')
    print('Press the number of the option or e to exit')
    value = input()

    if int(value) == 1:
        clear()
        date = f'{tm.get_today_date()}'
        print('Type the name of your task:')
        title = input()
        print('The default state of your task is "Unstarted"')
        status = 'Unstarted'
        print('Type the description for your task:')
        message = input()
        taskObj = Task(title, date, status, message)
        task = taskObj.to_dict()
        tm.add_task(task)

    if int(value) == 2:
        pass

    if int(value) == 3:
        pass

    if int(value) == 4:
        clear()
        tm.list_tasks()

    if value == "E" or value == "e":
        break