import FreeSimpleGUI as sg
from converters import convert

sg.theme("Black")
feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
output_label = sg.Text(key="output")
exit_button = sg.Button("Exit")

window = sg.Window("Converter",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, output_label, exit_button]])

while True:
    event, values = window.read()
    match event:
        case "Convert":  # Corrected here
            try:
                feet = float(values["feet"])
                inches = float(values["inches"])
                result = convert(feet, inches)
                window["output"].update(value=f"{result} m", text_color="white")
            except ValueError:
                sg.popup("Please provide valid numerical data")
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
