#! C:\\ProgramData\\Anaconda3 python
''' todo.py: This module contains the main driver of the program'''

__author__ = 'Abdulrahman Almulhim'
__cnetid__ = 'almulhim'
__date__ = '12/04/2025'
__title__ = 'Final Project'
__subtitle__ = 'todo'

# import modules
import argparse
import tasks
# Declare global constants

# main function

def main():
    # parse agurments
    args = parse_arguments()   
    # Analyze commands
    add, delete, done, list_tasks, query, report = analyze_commands(args)
    # calculate the number of commands 
    total_commands = add + delete + done + list_tasks + query + report
    
    if total_commands>1:
        # program is designed to do 1 command at a time
        print('Please use only one command at a time --add, --delete, --done, --query, --list, --report')
    
    elif total_commands==1:
        # create an instance of the Tasks object
        all_tasks = tasks.Tasks() 
        
        # Add
        if add == 1:
            all_tasks.add(args.add, args.due, args.priority)
        # Delete
        elif delete == 1:
            all_tasks.delete(args.delete)
        # List
        elif list_tasks == 1:
            all_tasks.list_uncompleted_tasks()
        # Report
        elif report == 1:
            all_tasks.report()
        # Query    
        elif query == 1:
            all_tasks.query(args.query)
        # Done        
        elif done == 1:
            all_tasks.done(args.done)
        # Save pickle    
        all_tasks.pickle_tasks()
    
    else:
        # No command passed
        print('Please enter what you would like to do (--add, --done, --delete, --query, --list, --report')
            
        
def parse_arguments():
    '''This function parses the passed commands
    takes: nothing
    returns: args object'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--add', type=str, required=False, help='Add a new task, expects a string representing the task name')
    parser.add_argument('--due', type=str, required=False, help='Task due date in MM/DD/YYYY format')
    parser.add_argument('--priority', type=int, required=False, default=1, help='Task priority from 1 to 3, default is 1')
    parser.add_argument('--delete', type=int, required=False, help='Delete the task with the passed unique id')
    parser.add_argument('--list', action='store_const', const = True, required=False, default=None, help='Prints the incomplete tasks')
    parser.add_argument('--report', action='store_const', const = True, required=False, default=None, help='Prints out all tasks and details')
    parser.add_argument('--query', type=str, nargs='+', required=False, help='Searches tasks using the string words passed')
    parser.add_argument('--done', type=int, required=False, help='Marks the task with the passed unique id as done')
    
    args = parser.parse_args()
    return args

def analyze_commands(args):
    add = int(args.add!=None)
    delete = int(args.delete!=None)
    done = int(args.done!=None)
    list_tasks = int(args.list!=None) 
    query = int(args.query!=None)
    report = int(args.report!=None)
    return add, delete, done, list_tasks, query, report
    
    
    
# Boilerplate
if __name__ == '__main__':
    main() 
