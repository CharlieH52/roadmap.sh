from taskClass import Task
from datetime import date
import os
import json

workingPath = os.getcwd()
projectPath = os.path.join(workingPath, r'backend\001-Task-Tracker')
folderTask = os.path.join(projectPath,'tasks')
fileTasks = os.path.join(folderTask,'taskLib.json')

class TaskManager:
    def __init__(self):
        self.folder_task()
        self.task_lib_checker()

    def folder_task(self):
        if not os.path.exists(folderTask):
            try:
                os.mkdir(folderTask)
            except OSError as e:
                print(e)

    def task_lib_checker(self):
        if not os.path.exists(fileTasks):
            try:
                with open(fileTasks, "w") as file:
                    json.dump([], file)
            except OSError as e:
                print(e)

    def load_tasks(self):
        with open(fileTasks, "r") as file:
            task_list = json.load(file)
        return task_list

    def write_file(self, data_dict):
        with open(fileTasks, "w") as file:
            json.dump(data_dict, file, indent=4)

    def get_today_date(self):
        today = date.today()
        return today

    def generate_id(self):
        taskList = self.load_tasks()
        if not taskList:
            return 1
        max_id = max(task['id'] for task in taskList)
        return max_id + 1

    def add_task(self, fields):
        newTask = self.load_tasks()
        newTask.append(fields)
        self.write_file(newTask)

    def delete_task(self, id):
        list = self.load_tasks()
        for i in list:
            if i['id'] == id:
                list.pop(list.index(i))
                self.write_file(list)

    def update_task(self, id, data):
        taskList = self.load_tasks()
        for task in taskList:
            if task['id'] == int(id):
                for key, value in task.items():
                    if key in data:
                        task[key] = data[f'{key}']
        self.write_file(taskList)

    def catch_task(self, id):
        taskList = self.load_tasks()
        for task in taskList:
            if task['id'] == int(id):
                return task

    def list_tasks(self):
        tasks = self.load_tasks()
        if len(tasks) == 0:
            print('Task list is empty, add a new task!') 
        
        if len(tasks) > 0:
            for i in tasks:
                print(i)