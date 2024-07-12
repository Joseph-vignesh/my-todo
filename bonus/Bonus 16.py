import FreeSimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress")
input_1 = sg.Input(tooltip = "select files")
button1 = sg.FilesBrowse("Browse",key="files")

label2 = sg.Text("Select the destination")
input_2 = sg.Input(tooltip = "select your file path")
button2 = sg.FolderBrowse("Browse",key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color = "green")

window = sg.Window("File compression",
                   layout=[[label1, input_1, button1],
                          [label2, input_2, button2],
                           [compress_button, output_label]],
                            font=('Times New Roman', 15))
while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="compression completed")



window.close()