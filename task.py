#! C:\\ProgramData\\Anaconda3 python
''' Task.py: This module contains the class object Task(), which is used to 
create a new task and saves its metadata'''

__author__ = 'Abdulrahman Almulhim'
__cnetid__ = 'almulhim'
__date__ = '12/04/2025'
__title__ = 'Final Project'
__subtitle__ = 'Class Task()'

# import modules
from datetime import datetime
# Declare global constants

# main function
class Task:
    '''Representation of a task
      
       Attributes:
                  - created - date - automatically generated at time of creating an instance
                  - completed - date - initially it is None until it is marked as done, at which point it will be overwritted with the date it is marked as done
                  - name - string - mandatory field, represents the name of the task
                  - uid - number - unique id
                  - priority - int - value of 1, 2, or 3 where 3 is the highest priority
                  - due date - date, this is optional, either it holds a date or None
                  - age - number in days - starts as None, then it is overwritten by the number of days since the task was created before printing the report or list
    '''
    def __init__(self, name, uid, priority, due):
        self.created = datetime.now()
        self.completed = None
        self.name = name
        self.uid = uid
        self.priority = priority
        self.due = due
        self.age = None
        
    def mark_done(self):
        '''This method marks a task object as done by filling the completed attribute with the datetime of the execuation'''
        self.completed = datetime.now()
        
    def calc_age(self):
        '''This method calculates the age of the task at the time of execution in days'''
        self.age = (datetime.now() - self.created).days
        
    