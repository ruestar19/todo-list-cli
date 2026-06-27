import json

#load saved data in task_list from file
try:
    with open ('tasks.json') as f:
        task_list = json.load(f)
except FileNotFoundError:
    task_list = []
except json.JSONDecodeError as e:
    print('Invalid JSON data!')
    task_list = []

# ADD TASK

def add_task():
    while True:
        task = input('Add task: ').strip()
        if not task:
            print('Task cannot be empty!')
            continue
        task_data = {
            "title": task,
            "done": False
        }
        task_list.append(task_data)
        save_tasks()
        keep_going = input("Continue? (Y/N)").strip().upper()
        if keep_going == 'N':
            break

#DELETE TASK

def delete_task(index):
    if index<=0:
        print('Invalid number!')
        return
    if (index-1)<len(task_list):
        del task_list[index-1]
    else:
        print('Task does not exist!')
    save_tasks()

#EDIT TASK

def edit_task(index):
    if (index-1)<len(task_list):
        update_which = int(input('What do you want to update? 1. Task 2. Task Status '))
        if update_which == 1:
            task_list[index-1]["title"] = input('Update your task: ')
        elif update_which == 2:
            current_status = task_list[index-1]["done"]
            task_list[index-1]["done"] = not current_status
            print('Task status updated!')
    else:
        print('Task does not exist!')
    save_tasks()

#VIEW TASK

def view_task():
    print('\nTO-DO:')
    if not task_list:
        print('No tasks available.')
        return
    for t_num, task in enumerate (task_list, start=1):
        status = 'Done' if task["done"] else 'Not Done'
        print(f'{t_num}. {task["title"]} [{status}]')

#SAVE TASK

def save_tasks():
    with open ('tasks.json', 'w') as f:
        json.dump(task_list, f, indent=2)

#MAIN LOOP
while True:
    print("""
    1- Add Task
    2- Delete Task
    3- Edit Task
    4- View Tasks
    5- Exit
      """)
    
    try:
        num = int(input('Your choice:'))
    except Exception:
        print('Invalid choice!')
    else:
        if num==1:
            add_task()
        elif num==2:
            if task_list == []:
                print('Empty list, nothing to delete!')
                continue
            try:
                n = int(input('Choose task number to be deleted: '))
            except ValueError:
                print('Invalid input type!')
            delete_task(n)
        elif num==3:
            try:
                n = int(input('Choose task number for editing: '))
            except ValueError:
                print('Invalid input type!')
            edit_task(n)
        elif num==4:
            view_task()
        elif num==5:
            print('Exiting App...')
            break
