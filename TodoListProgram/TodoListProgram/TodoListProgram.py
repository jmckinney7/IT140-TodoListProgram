# This program allows the user to create a simple to-do list based on 3 factors.
# The 3 factors are: (task name, due date, and priority)
# The user will be asked to input the number of tasks they want to create.
# From there, the user will be asked to input the task name, due date, and priority for each task.
# The program will then display the to-do list in ordered format.
# Lastly, the program will export the user's to-do list to a csv file.


# These are imports for the program
# csv allows the program to export the to-do list to a csv file
import csv
# datetime allows the program to get the current date and time
import datetime
# here I am importing the exit function from sys so I can exit the program
from sys import exit
# here I am importing my own module that handles the creation of the to-do list
from tasks import Task


# This function handles the exportation of the to-do list to a csv file
def exportTodoList(Tasks):
  # This handles any exceptions that the program may encounter when exporting
  try:
    # this opens the file in append mode
    with open(f"tasks-{str(datetime.date.today())}.csv", "a", newline="") as file:
      # This creates a writer object from the csv module and writes the Tasks in the file
      writer = csv.writer(file)
      writer.writerows(Tasks)
      # This closes the handle to the file
      file.close()
  except Exception as e:
    print(type(e), e)
    exit()
    
  # This prints this message to the console after the to-do list is exported
  print("\nTo-do list exported successfully!")


# This function handles the creation of the to-do list
def createTodoList(size):
  Tasks = []
  # This is a loop that is running until it reaches the range of size
  for Index in range(size):
    
    # I am creating a new instance of the Task class
    TodoList = Task()

    # I'm writing the task number on the console so the user knowns which task they are on
    print("Task", str(Index + 1) + ":")
    Tasks.append(TodoList.createTask())
    print()
  return Tasks


# This function handles displaying the to-do list on the console
def displayTodoList(Tasks):
  # This is a new instance of the Task class
  Todo = Task()
  # Here I am calling the method that displays the to-do list
  Todo.displayTodoList(Tasks)


# This is the main function of the program
def main():
  # This is me initializing 2 variables. One for number of tasks and the other for the to-do list
  NumberOfTasks = 0
  Tasks = ()

  # This is a infinite loop until the user inputs a number other than 0 or less
  while NumberOfTasks <= 0:
    # This handles the ValueError exception that occurs if a user doesn't input a number
    try:
      NumberOfTasks = int(input("How many tasks would you like to add?: "))
    except ValueError:
      print("Please enter a number for how many tasks you would like to add!\n")

  # This creates a to-do list based on the number of tasks the user inputted
  Tasks = tuple(createTodoList(NumberOfTasks))
  print("\nTo-do list has been created!")

  # When calling this function, it displays the to-do list on the console
  displayTodoList(Tasks)

  # When calling this function, it exports the to-do list to a csv file
  exportTodoList(Tasks)


# This is the main function of the program __name__ is a special variable
# It is assigned to the name of the current module
if __name__ == "__main__":
  # This calls the main function
  main()