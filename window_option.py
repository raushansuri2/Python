import PySimpleGUI as sg

label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")

label2 = sg.Text("How many State is USA?")
label2_option1 = sg.Radio("25", group_id="question1")
label2_option2 = sg.Radio("50", group_id="question1")
label2_option3 = sg.Radio("49", group_id="question1")
label2_option4 = sg.Radio("51", group_id="question1")

window = sg.Window("File Compressor",
                   layout=[
                           [ [label], [option1, option2, option3, option4]],
                            [ [label2], [label2_option1], [label2_option2], [label2_option3], [label2_option4]]
                          ])

window.read()
window.close()