# prompt="enter a todo:"
# todo1 = input(prompt)
# todo2 = input(prompt)
# todo3 = input(prompt)
#
# todos = [todo1, todo2, todo3,"hello"]
# print (todos)
# print(type(todos))
import FreeSimpleGUI as sg
import function

label = sg.Text("Type in ToDo")
input_box = sg.InputText(tooltip="Enter ToDo", key="todo")
list_box = sg.Listbox(values=function.get_todos(), key="todos", enable_events=True, size=[45, 10])

# Replace Add and Complete buttons with Image elements
add_image = sg.Image(filename='add.png', key='Add')
complete_image = sg.Image(filename='complete.png', key='Complete')

exit_button = sg.Button("Exit")

layout = [[label],
          [input_box, add_image],
          [list_box],
          [complete_image],
          [exit_button]]

window = sg.Window("My To-Do App", layout=layout, font=('Times New Roman', 15))

while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

    if event == "Add":
        new_todo = values["todo"].strip()
        if new_todo:
            todos = function.get_todos()
            todos.append(new_todo)
            function.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        else:
            sg.popup("Please enter a valid todo.")

    if event == "Complete":
        if values['todos']:
            todo_to_complete = values['todos'][0]
            todos = function.get_todos()
            todos.remove(todo_to_complete)
            function.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        else:
            sg.popup("Please select a todo to complete.")

window.close()
