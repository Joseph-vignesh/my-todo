import FreeSimpleGUI as sg
#from FreeSimpleGUI import Text

import function

import time

import os

if not os.path.exists("vic.txt"):
    with open("vic.txt", 'w')as file:
        pass


sg.theme("Black")
clock= sg.Text(" ", key="clock")
label = sg.Text("Type in ToDo")
input_box = sg.InputText(tooltip="Enter ToDo", key="todo")
add_button = sg.Button(key='add', image_source="add.png")
list_box = sg.Listbox(values=function.get_todos(), key="todos", enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button(image_source="complete.png", key="complete")
exit_button = sg.Button("Exit")

layout = [[clock], [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window("My To-Do App", layout=layout, font=('Times New Roman', 15))

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("  %d - %b -  %Y, %H %M %S"))



    print(event)
    print(values)

    match event:
        case "add":
            todos = function.get_todos()
            new_todo = values["todo"] + '\n'
            if new_todo:  # Only add non-empty todos
                todos.append(new_todo)
                function.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            else:
                sg.popup("Please enter a valid todo.")
        case "Edit":
            if values['todos']:  # Check if list is not empty
                todo_to_edit = values['todos'][0]
                new_todo = values["todo"].strip()
                if new_todo:  # Only edit to a non-empty todo
                    todos = function.get_todos()
                    if todo_to_edit in todos:
                        index = todos.index(todo_to_edit)
                        todos[index] = new_todo
                        function.write_todos(todos)
                        window["todos"].update(values=todos)
                        window["todo"].update(value="")
                    else:
                        sg.popup("Selected todo is not in the list.")
                else:
                    sg.popup("Please enter a valid todo.")
            else:
                sg.popup("Please select a todo to edit.")
        case "complete":
            if values['todos']:  # Check if list is not empty
                todo_to_complete = values['todos'][0]
                todos = function.get_todos()
                if todo_to_complete in todos:  # Ensure the item exists in the list
                    todos.remove(todo_to_complete)
                    function.write_todos(todos)
                    window["todos"].update(values=todos)
                    window["todo"].update(value="")
                else:
                    sg.popup("Selected todo is not in the list.")
            else:
                sg.popup("Please select a todo to complete.")
        case "todos":
            if values['todos']:  # Check if list is not empty
                window["todo"].update(value=values['todos'][0])
            else:
                sg.popup("Please select a todo.")
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
