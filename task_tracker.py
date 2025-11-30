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

def main():
    while True:
            command = input("\nEnter command (add/list/quit): ")
            
            if command == "add":
                task_name = input("Task name: ")
                add_task(task_name)
            elif command == "list":
                list_tasks()
            elif command == "quit":
                print("Goodbye!")
                break
            else:
                print("Uknown command.  Try add, list or quit.")
                
main()

