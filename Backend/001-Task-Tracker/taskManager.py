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
        pass

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

    def get_today_date(self):
        today = date.today()
        return today

    def add_task(self, fields):
        newTask = self.load_tasks()
        newTask.append(fields)
        with open(fileTasks, "w") as file:
            json.dump(newTask, file, indent=4)

    def delete_task(self):
        pass

    def update_task(self):
        pass

    def list_tasks(self):
        tasks = self.load_tasks()
        if len(tasks) == 0:
            print('No hay tareas para mostrar') 
        
        if len(tasks) > 0:
            for i in tasks:
                print(i)