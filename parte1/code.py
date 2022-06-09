import PySimpleGUI as sg
sg.theme()
layout = [
    [sg.Text('Some text on Row 1')],
    [sg.Text('Enter something on Row 2'), sg.InputText(),sg.FileBrowse('Buscar')],
    [sg.Button('Ok'), sg.Button('Cancel'),sg.Button('Teste')]
]

window = sg.Window('Teste', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Teste':
        (sg.popup('Conhecendo o PySimpleGUI', 'Esse é o meu primeiro codigo'))
        (sg.POPUP_BUTTONS_YES_NO)
    print('You entered', values[0])