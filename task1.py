from flask import Flask
from mongoengine import connect,Document,StringField,DictField


app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {
    "db": "To-do list",
    "host": "127.0.0.1",
}
connect(host=app.config["MONGODB_SETTINGS"]["host"])

class Task(Document):
    # name=StringField()
    tasks=DictField()


def add_task():
    print("\nCurrent task")
    title=input("Enter the task: ")
    description=input("Enter the Description: ")
    new_task={"title":title,
              "description":description,
              "completed": False}
    Task(tasks=new_task).save()
    print("Task added successfully!")

def view_task():
    if task:=Task.objects():
        for idx,col in enumerate(task,1) :
            to_do=col.tasks   #{i:j  for i,j in col.tasks.items() }
            status="[X]" if to_do["completed"] else "[ ]"
            print("{}.{} {} - {}".format(idx,status,to_do["title"],to_do["description"]))
    else:
        print("No task added!")

def mark_task():
    view_task()
    count=Task.objects.count()
    task_number=int(input("Enter number to mark completion: "))
    task=Task.objects.skip(task_number-1).limit(1).first()
    if task and 1<= task_number <= count:
        task.tasks["completed"]=True
        task.save()
        print("Task marked completed!")
    else:
        print("Invalid Task number!")

def unmark_task():
    view_task()
    count=Task.objects.count()
    task_number=int(input("Enter number to unmark completion: "))
    task= Task.objects.skip(task_number-1).limit(1).first()
    if task and 1<= task_number <= count:
        if task.tasks["completed"] == False:
            print("Task status is already unmark!")
        else:
            task.tasks["completed"]=False
            task.save()
            print("Task marked as incomplete")
    else:
        print("Invalid task number!")
def delete_task():
    view_task()
    count=Task.objects.count()
    task_number=int(input("Enter number to delete task: "))
    task=Task.objects.skip(task_number-1).limit(1).first()
    print(task.tasks)
    if 1<= task_number <= count:
        task.delete()
        print("Your {} task deleted sucessfully!".format(task.tasks["title"]))
    else:
        print("Invalid Task number!")
    


while True:
    print("""\nwelcome to To-Do list\n 1: Add task \n 2: View task \n 3: Mark task completed \n 4: Unmark task complete \n 5: Delete task \n 6: Exit
    """)
    try:
        choice=int(input("Enter the number: "))
        if choice==1:
            add_task()
        elif choice==2:
            view_task()
        elif choice==3:
            mark_task()
        elif choice==4:
            unmark_task()
        elif choice==5:
            delete_task()
        elif choice==6:
            print("\nThank you for using To-Do!")
            break
        else:
            print("\nNot a good choice.!")
    except ValueError as e:
        print("Not good choice..!")
    except NameError as e:
        print("Not good choice...!")
    
    
        

