import time
task= []
ended_tasks=[]

def main():
  while True:
    print( """ 
    1- Add new task
    2- Mark task as completed
    3- View incomplete tasks
    4- Viw completed tasks
    5- View all tasks
    6- Exit """)
    choices= input("please enter choice:")
  
    if choices == "1":
      add_task()
    elif choices == "2":
      mark_task()
    elif choices == "3":
      view_incomplete_tasks()
    elif choices == "4":
      view_completed_tasks()
    elif choices == "5":
      view_all_tasks()
    elif choices == "6":
      break
    else:
      print("please enter a valid number from 1 to 6")
  
#function that take the task
def add_task():
  tasks =input("please enter a new task:")
  task.append(tasks)
  print ("taks added successifully")
  time.sleep(2)


#function that mark task as completed
def mark_task():
  if task:
    view_incomplete_tasks()
    completed = input("enter the number of the function that you need to mark as completed: ")
    x= int(completed)
    x=x-1
    ended_tasks.append(task.pop(x))
    view_incomplete_tasks()
    
    print("Updated successfully")
  else: 
    print("No tasks to mark as completed")

#function that view all the taskt
def view_incomplete_tasks():
  if task:
    print("Your TO-DO List")
    for x in task:
      print(str(task.index(x)+1)+ "- "+ x + "💔✖")
      print("-------------------------------")
    time.sleep(1)
  else:
    print("No tasks incomplete to view")

#function to view complete tasks
def view_completed_tasks():
  if ended_tasks:
    print("Your completed tasks:")
    for x in ended_tasks:
      print(str(ended_tasks.index(x)+1)+ "- "+ x + "✔✔👌")
      print("-------------------------------")
    time.sleep(1)
  else:
    print("There is no completed tasks")

#function to view all tasks
def view_all_tasks():
  view_incomplete_tasks()
  print("         &")
  view_completed_tasks()


#call the main
""""__name__ is string vairable that return main if its called from the same file but it gives another name from another file so it won't run """
if __name__== "__main__":
  main()

