import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def add_task(tasks, task_name):
    tasks.append(task_name)
    save_tasks(tasks)
    print(f"Added: {task_name}")

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
            
def complete_task(tasks, task_number):
    try:
        index = task_number - 1
        if index < 0:
            print("Invalid task number.")
            return
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Completed: {removed}")
    except IndexError:
        print("Task not found.")

def main():
    tasks = load_tasks()
    
    while True:
            command = input("\nEnter command (add/list/quit): ")
            
            if command == "add":
                task_name = input("Task name: ")
                add_task(tasks, task_name)
            elif command == "list":
                list_tasks(tasks)
            elif command == "done":
                list_tasks(tasks)
                task_number = input("Task number to complete: ")
                complete_task(tasks, int(task_number))
            elif command == "quit":
                print("Goodbye!")
                break
            else:
                print("Uknown command.  Try add, list, done, or quit.")
                
main()

