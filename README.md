To be able to run the application from anywhere on you pc, do the following.

0- Ensure shebang line is acurate
1- Create a new folder (Scripts) under the user's home directory
2- Place all code files and pickle inside it
3- Create a .txt file with the following content:
@echo off
python "%~dp0todo.py" %*
4- Rename it todo.bat and place it in the new Scripts folder
5- Add folder to PATH using environment variables
6- Run application from anywhere as this format: 
	- todo --add "Task"
	- todo --report
	- etc.