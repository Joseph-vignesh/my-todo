todos = []

while True:
    user_action = input("type add, show or exit:")

    match user_action:
        case 'add':
            todo = input("enter a todo:")
            todos.append(todo)
        case 'show':
            for item in todos:
        case 'exit':
           break

print("Bye! Bye!
