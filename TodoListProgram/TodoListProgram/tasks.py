# The Task class holds all the functionality for creating a to-do list
class Task:
  # The __init__ method initializes all the attributes for creating a to-do list
  def __init__(self):
    self.TaskName = ""
    self.DueDate = ""
    self.Priority = ""
    self.TaskNameCreated = self.DueDateCreated = self.PriorityCreated = False

  
  # The inputTask method handles the user input for the task name when creating a list
  def inputTask(self):
    """ returns the task name of the task """
    # This loop will run until the user inputs a valid task name
    while self.TaskName.__len__() <= 0:
      self.TaskName = input("What is the task: ")
      # If the task name is empty, the user is asked to input a task name again
      if self.TaskName.__len__() <= 0:
        print("Please enter a valid task name!\n")
    self.TaskNameCreated = True
    return self.TaskName

  
  # The isValidDate method handles checking whether the user inputted a valid date
  def isValidDate(self):
    """ returns True if all characters defined in condition are digits """
    # This condition checks if each character in the date except '/' is a number
    if (self.DueDate[0].isdigit() and self.DueDate[1].isdigit() 
        and self.DueDate[3].isdigit() and self.DueDate[4].isdigit() 
        and self.DueDate[6].isdigit() and self.DueDate[7].isdigit() 
        and self.DueDate[8].isdigit() and self.DueDate[9].isdigit()):
      return True
    return False

  
  # The inputDueDate method handles the user input for the due date when creating a list
  def inputDueDate(self):
    """ returns the due date of the task """
    # This loop will run until the user inputs a valid date
    while not self.DueDateCreated:
      # This handles the IndexError exception that may occur
      try:
        self.DueDate = input("What is the due date [MM/DD/YYYY]: ")
        # This condition checks if the user inputted a valid date
        if (self.DueDate[2] == '/' and self.DueDate[5] == '/' 
            and len(self.DueDate) == 10 and self.isValidDate()):
          self.DueDateCreated = True
          return self.DueDate
        else:
            print("Please enter the date in the format MM/DD/YYYY!\n")
      except IndexError:
        print("Date MUST be in the format MM/DD/YYYY!\n")

  
  # The inputPriority method handles the user input for the priority when creating a list
  def inputPriority(self):
    """ returns the priority of the task """
    # This loop will run until the user inputs a valid priority
    while not self.PriorityCreated:
      self.Priority = input("What is the priority [High, Medium, Low]: ")
      # This condition checks if the user inputted a valid priority
      if(self.Priority.lower() != "high" and self.Priority.lower() != "medium" 
         and self.Priority.lower() != "low"):
        print("Please enter a valid priority!\n")
      else:
        self.PriorityCreated = True
        break
    return self.Priority

  
  # The createTask method handles creating a to-do list
  def createTask(self):
    """ returns a list containing the task name, due date, and priority """
    # This creates an instance of a List variable
    self.Task = []
    # This appends or adds to the list by calling each function for the creation of the list
    self.Task.append(self.inputTask())
    self.Task.append(self.inputDueDate())
    self.Task.append(self.inputPriority())
    return self.Task

  
  # The displayTodoList method handles displaying the to-do list on the console
  def displayTodoList(self, Tasks):
    """ Prints the to-do list in a formatted way """
    # This is a loop that is running until it reaches the length of Tasks
    for Index in range(len(Tasks)):
      print(str(Index + 1) + ":", Tasks[Index][0], Tasks[Index][1], Tasks[Index][2])