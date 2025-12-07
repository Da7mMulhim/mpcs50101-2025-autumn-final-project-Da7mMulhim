#! C:\\ProgramData\\Anaconda3 python
''' validator.py: This module contains helper functions used to validate user input'''

__author__ = 'Abdulrahman Almulhim'
__cnetid__ = 'almulhim'
__date__ = '12/04/2025'
__title__ = 'Final Project'
__subtitle__ = 'module validator'

# import modules
from datetime import datetime
# Declare global constants

# main function
def validate_task_name(task_name):
    '''This funcion validates if the task_name is indeed a non empty string
    takes: task_name: any data type, but should be a non empty string to be marked as valid
    returns: valid: boolean variable, True when task_name is a non empty string, and False ortherwise '''
    valid = False
    if isinstance(task_name, str): # if task_name is string
        if len(task_name) > 0: # if not empty string
            valid = True       
        else:
            print('Task name should have at least 1 character')
    else:
        print('Task name should be a string')
    return valid

def validate_task_priority(task_priority):
    '''This function validates the passed task priority if it is 1, 2 or 3
    takes: task_priority: any data type, but should be 1, 2 or 3 to be valid
    returns: valid: bolean variable, True when task_priority can be converted to an integer and is 1,2 or 3, FAlse otherwise'''
    valid = False
    try:
        task_priority = int(task_priority) # convert to int
        if task_priority in [1,2,3]: # check it is either 1, 2 or 3
            valid = True
        else:
            print('Enter priority as an integer 1, 2 or 3')
    except:
        print('Enter priority as an integer 1, 2 or 3')
    return valid

def validate_task_due_date(due_date):
    '''This function validates a date of its in this format MM/DD/YYYY
    takes:   - due_date: any data type or None, but should be a string in this format MM/DD/YYYY to be markes as valid
    returns: - valid: boolean variable, True when string mathces the expected format, False otherwise. 
             - due_date_datetime: either None, or the due_date converted to datetime'''
    due_date_datetime = due_date # intialize as the same due_date for when it is None
    valid = False
    if isinstance(due_date_datetime, str): # if has a string value
        try:
            due_date_datetime = datetime.strptime(due_date_datetime, "%m/%d/%Y") # convert string to datetime
            valid = True
        except ValueError:
            print('Enter task due date in the string format: MM/DD/YYYY')
    elif due_date_datetime is None: # if None
        valid = True
    else:
        print('Enter task due date in the string format: MM/DD/YYYY')
    return valid, due_date_datetime

def validate_uid(uid, task_list):
    '''The function validates that the uid exists in the list of tasks
    takes: - uid: the uid to be checked, should be an integer
           - task_list: the task list to check against 
    returns: - valid: a bolean variable, True when  uid exist, False otherwise'''
    valid_uids = [x.uid for x in task_list] #Extract uids of all the task to a list using comprehension list
    if uid in valid_uids: 
        valid_uid = True
    else:
        print('Enter an existing unique ID.')
        valid_uid = False
    return valid_uid
    