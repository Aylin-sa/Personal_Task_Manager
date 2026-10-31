from tasks import show_tasks, save_tasks, load_tasks
from dotenv import load_dotenv 
import os 

load_dotenv()


name = input("enter your name: ")
print("welcome", name)
admin_mod = input("do you want t enter admin mod? yes/no: ")
if admin_mod == "yes":
    password = input("enter admin password : ")
    if password == os.getenv("admin_pass"):
        print("admin mod activated")
    else:
        print("wrong password")
tasks = load_tasks()
count = int(input("how many tasks do you want to add? : "))

for i in range(count):
    task = input("enter a task: ")
    tasks.append(task)

show_tasks(tasks)
save_tasks(tasks)
load_tasks()
