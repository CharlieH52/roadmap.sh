
class Task:
    def __init__(self, title, date, status, message):
        self.title = title
        self.date = date 
        self.status = status
        self.message = message 

    def to_dict(self):
        task_dict = {
            'title': self.title,
            'date': self.date,
            'status': self.status,
            'message': self.message
        }
        return task_dict