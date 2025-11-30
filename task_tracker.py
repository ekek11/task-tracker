tasks = []

def add_task(task_name):
    tasks.append(task_name)
    print(f"Added: {task_name}")

def list_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

#Test it out
add_task("Learn Python")
add_task("Build something cool")
list_tasks()
