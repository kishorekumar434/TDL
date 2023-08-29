



task=[]
def add_task(task):
    print("\nCurrent task")
    title=input("Enter the task: ")
    description=input("Enter the Description: ")
    new_task={"title":title,
              "description":description,
              "completed": False}
    task.append(new_task)
    print("Task added successfully!")
    return task

def view_task(task):
    if not task:
        print("No task added!")
    else:
        for idx, task in enumerate(task,1):
            status="[X]" if task["completed"] else "[ ]"
            print("{}.{} {} - {}".format(idx,status,task["title"],task["description"]))

def mark_task(task):
    view_task(task)
    task_number=int(input("Enter number to mark completion: "))
    if 1<= task_number <= len(task):
        task[task_number-1]["completed"]=True
        print("Task marked completed!")
    else:
        print("Invalid Task number!")
    return task

def delete_task(task):
    view_task()
    task_number=int(input("Enter number to delete task: "))
    if 1<= task_number <= len(task):
        delete_task=task.pop(task_number-1)
        print("Your {} task deleted sucessfully!".formate(task["title"]))
    else:
        print("Invalid Task number!")
    return task
#add_task()
#print(task)   


while True:
    print("""\nwelcome to To-Do list\n 1: Add task \n 2: View task \n 3: Mark task completed \n 4: Delete task \n 5: Exit
    """)
    choice=int(input("Enter the number: "))
    if choice==1:
        task=add_task(task)
    elif choice==2:
        view_task(task)
    elif choice==3:
        mark_task(task)
    elif choice==4:
        delete_task(task)
    elif choice==5:
        break
    else:
        print("\n Thank you for using To-Do!")
