#! C:\\ProgramData\\Anaconda3 python
''' Tasks.py: This module contains the class object Tasks(), which holds all
the tasks added by user, and some methods to add, delete, etc.'''

__author__ = 'Abdulrahman Almulhim'
__cnetid__ = 'almulhim'
__date__ = '12/04/2025'
__title__ = 'Final Project'
__subtitle__ = 'Class Tasks()'

# import modules
import os
import pickle
from datetime import datetime
import task
import input_validator
# Declare global constants
PICKLE_NAME = "C:\\Users\\Abdul\\Scripts\\.todo.pickle"


# main function
class Tasks:
    '''Class containing the list of Task objects, it also contains methods to add 
    a new task, delete task, mark tasks as done, print list of tasks, print report
    
    Attributes:
                  - tasks - a list of `Task` objects.'''
   
    def __init__(self):
        '''Read pickled tasks file into a list'''
        # List of Task objects
        self.tasks = self.read_pickle()
    
    def read_pickle(self):
        '''Read the last saved tasks'''
        # Check if the pickle file already exist
        if os.path.exists(PICKLE_NAME):
            try:
                # Load pickle
                with open(PICKLE_NAME, "rb") as f:
                    return pickle.load(f)
            except Exception as e:
                print(f"Error reading pickle file: {e}")
        # if not pickle is availabe, create a new list
        else:
            return []

    def pickle_tasks(self):
        '''Save tasks list to a pickle'''
        try:
            # save to a pickle
            with open(PICKLE_NAME, "wb") as f:
                pickle.dump(self.tasks, f)
            print(f"Saved pickle to {PICKLE_NAME}")
        except Exception as e:
            print(f"Error saving pickle file: {e}")

    def list_uncompleted_tasks(self, uids = None):
        '''This method prints the uncompleted tasks sorted by due date then priority then name
        takes: uids (optionally for when we want to print specific ids, used with --query)
        returns: nothing'''
        self.calculate_tasks_age() # Calculate the age of each task 
        uncompleted_tasks = self.tasks # Initialize as all tasks
        if uids: # if some uids were passed to the function
            uncompleted_tasks = self.filter_function(uncompleted_tasks, 'uid', uids) # filter only the provided uids
        uncompleted_tasks = self.filter_function(uncompleted_tasks, 'incomplete') # filter only the uncompleted tasks
        uncompleted_tasks = self.sort_function(uncompleted_tasks) # sort the list of tasks

        print(f'{"ID":<4} {"Age":<4} {"Due Date":<10} {"Priority":<10} {"Task"}')
        print(f'{"-"*4:<4} {"-"*4:<4} {"-"*10:<10} {"-"*10:<10} {"-"*20}')
        for obj in uncompleted_tasks: # loop through the filtered and sorted tasks
            age = f'{obj.age}d' # save age as (number of days)d
            if obj.due: # if due date was passed
                due = f'{obj.due.month}/{obj.due.day}/{obj.due.year}' #MM/DD/YYYY
            else: # if due date was left empty
                due = ''
            print(f'{obj.uid:<4} {age:<4} {due:<10} {obj.priority:<10} {obj.name}')

    def calculate_tasks_age(self):
        '''This method calculates the age of all tasks
        returns: nothing'''
        for obj in self.tasks:
            obj.calc_age()
            
    def sort_function(self, task_list):
        '''This method sorts the task list by the due date if it exists then priority, then name
        takes: task_list which is a list of the tasks to be sorted
        returns: the sorted list'''
        tasks_sorted = sorted(task_list, key=lambda x: [x.due if x.due != None and x.due != '' else datetime.max, 
                                                        -x.priority, 
                                                        x.name])
        return tasks_sorted
    
    def filter_function(self, tasks_list, attribute_name, uids=None):
        '''This method filters the tasks_list to remove completed tasks, or to focus on specific uids
        takes: tasks_list, which is a list of all tasks to be filtered, attribute_name which is a flag 
        that dictates whcih kind of filtering is required.
        reutns: filtered tasks_list
        '''
        if attribute_name == 'incomplete': # if the flag was incompleted
            tasks_list = list(filter(lambda x: x.completed is None, tasks_list)) # filter out all completed tasks
        elif attribute_name == 'uid': # if the flag was uid
            tasks_list = list(filter(lambda x: x.uid in uids, tasks_list)) # filter out any uid not provided in uids list
        else:
            raise Exception
        return tasks_list
        
        
    def report(self):
        '''This method prints a full report of all created tasks
        takes: nothing
        returns: nothing'''
        self.calculate_tasks_age() # Calculate the age of each task 
        task_list = self.tasks # take all tasks
        task_list = self.sort_function(task_list) # sort tasks
        print(f'{"ID":<4} {"Age":<4} {"Due Date":<10} {"Priority":<10} {"Task":<20} {"Created":<28} {"Completed":<28}') # use of :<xx is to left align the printed items
        print(f'{"-"*4:<4} {"-"*4:<4} {"-"*10:<10} {"-"*10:<10} {"-"*20} {"-"*28} {"-"*28}') 
        for obj in task_list: # loop through task_list
            age = f'{obj.age}d' # save age as (number of days)d
            if obj.due: # if due date was passed
                due = f'{obj.due.month}/{obj.due.day}/{obj.due.year}'
            else: # if due date was not passed
                due = ''
            created = obj.created.strftime("%a %b %e %H:%M:%S %Z %Y") # convert date to this format (Fri Dec  5 23:34:04 CST 2025)
            if obj.completed:
                completed = obj.created.strftime("%a %b %e %H:%M:%S %Z %Y")
            else:
                completed = ''
            print(f'{obj.uid:<4} {age:<4} {due:<10} {obj.priority:<10} {obj.name:<20.20} {created} {completed}') #use of obj.name:<20.20 left aligns the task name, and prints only the first 20 characters of the task name

    def done(self, done_uid):
        '''This method marks specific tasks as done by filling the task attribute completed with the datetime of the time of execution
        takes: done_uid which the unique id of the task to be marked as done
        returns: nothing'''
        valid_uid = input_validator.validate_uid(done_uid, self.tasks) #validate the uid passed
        if valid_uid: #if valid
            for task_obj in self.tasks: # loop through the tasks to find the object
                if task_obj.uid == done_uid: # if the task object is found
                    task_obj.mark_done() 
                    print(f'Task {done_uid} marked completed')

    def query(self, terms):
        '''This method searches for tasks by the words passed and prints them as --list would do
        takes: terms: a list of words to be searched
        returns: nothing
        '''
        uids = [] # Initiate empty list that will hold the uid of the tasks that matched the search
        for task_obj in self.tasks: # loop through the tasks
            if task_obj.completed is None: # Only search the non completed tasks
                for term in terms: # loop through the passed words to be searched
                    if term.lower() in task_obj.name.lower(): # check if the therm matches any part of the task name, case insensitive
                        uids.append(task_obj.uid) # if found, append the uid of the task to uids
        if len(uids)>0: # if there are found tasks
            uids = list(set(uids))
            self.list_uncompleted_tasks(uids) #print the list of the specific uids found using the same method used for --list
        else:
            print('No results found')

    def add(self, task_name, task_due_date, task_priority):
        '''Thid method adds a new task object to the list of tasks
        takes: task_name: a string, task_due_date: a string in this format (MM/DD/YYYY), task_priority: integer 1, 2 or 3
        returns: nothing'''
        valid_name = input_validator.validate_task_name(task_name) # validate the passed name
        valid_priority = input_validator.validate_task_priority(task_priority) # validate the passed priority
        valid_due_date, task_due_date = input_validator.validate_task_due_date(task_due_date) # validate the passed due date
        if valid_name and valid_due_date and valid_priority: # if all input is valid
            task_uid = len(self.tasks) # generate a new uid which is just the number of the tasks
            new_task = task.Task(task_name, task_uid, task_priority, task_due_date) # create a new instance of the task object
            self.tasks.append(new_task) # append the object to the list of tasks
            print(f'Task {task_uid} added')
    
    def delete(self, delete_uid):
        '''This method deletes a task from the list of tasks
        takes: delete_uid: an integer of the uinque id of the task
        returns: nothing'''
        valid_uid = input_validator.validate_uid(delete_uid, self.tasks) # validate the delete_uid
        if valid_uid: 
            for task_obj in self.tasks: # loop through tasks
                if task_obj.uid == delete_uid: # check if the task uid matches the passed delete_uid
                    self.tasks.remove(task_obj) # remove task object from list of task objects
                    print(f'Task {delete_uid} deleted')