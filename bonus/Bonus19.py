import FreeSimpleGUI as sg


sg.theme("Black")

label1 = sg.Text("Select archive")
input1 = sg.Input()
button1 = sg.FileBrowse("choose", key="archive")

label2 = sg.Text("Select directory")
input2 = sg.Input()
button2 = sg.FolderBrowse("choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(" ", key="output", text_color="green")

layout = [[label1,input1, button1],[label2,input2, button2],[extract_button, output_label]]

window = sg.Window("Archive Extractor",
                   layout=layout)

window.read()
window.close()