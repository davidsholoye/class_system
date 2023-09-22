#As a user
#So that I can keep track of my tasks
#I want a program that I can add todo tasks to and see a list of them.

class Tracker():
    def __init__(self):
        self.todos = []
        

    def add(self, task):
        self.todos.append(task)
        if task == '':
            self.todos.pop()
            print("Can't add an empty task")
        else:
            print('Task has been added.')

    def list(self):
        return self.todos
    


#As a user
#I want to check if a text includes the string #TODO
#So that I can keep track of my tasks

def todo_checker(text):
    count = 0
    split_text = text.split()
    for i in split_text:
        if i == '#TODO':
            count += 1
    return f"{count} tasks left."

