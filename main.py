import time
task= []

#function that take the task
def add_task():
  tasks =input("please enter a new task:")
  task.append(tasks)
  print ("taks added successifully")
  time.sleep(2)


#function that mark task as completed
def mark_task():
  view_task()
  completed = input("enter the number of the function that you need to mark as completed: ")
  x= int(completed)
  x=x-1
  print(x)
  task.pop(x)
  view_task()
  print("Updated successfully")


#function that view all the taskt
def view_task():
  print("Your TO-DO List")
  for x in task:
    print(str(task.index(x)+1)+ "- "+ x)
  time.sleep(1)





while True:
  print( """ 
	1- add new task
	2- task completed
	3- view tasks
	4- quite """)
  choices= input("please enter choice:")

  if choices == "1":
    add_task()
  elif choices == "2":
    mark_task()
  elif choices == "3":
    view_task()
  elif choices == "4":
    break
  else:
    print("please enter a valid number from 1 to 4")

