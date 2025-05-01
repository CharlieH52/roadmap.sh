
class Task:
    def __init__(self, id, title, status, description, addDate=None, upDate=None):
        self.id = id
        self.title = title
        self.status = status
        self.description = description
        self.addDate = addDate
        self.upDate = upDate 

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'status': self.status,
            'description': self.description,
            'addDate': self.addDate,
            'upDate': self.upDate
        }