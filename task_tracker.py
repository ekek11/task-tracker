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

def main():
    tasks = load_tasks()
    
    while True:
            command = input("\nEnter command (add/list/quit): ")
            
            if command == "add":
                task_name = input("Task name: ")
                add_task(tasks, task_name)
            elif command == "list":
                list_tasks(tasks)
            elif command == "quit":
                print("Goodbye!")
                break
            else:
                print("Uknown command.  Try add, list or quit.")
                
main()

