import PySimpleGUI as sg
sg.theme()
layout = [
    [sg.Titlebar('Primeiro código')],
    [sg.Text('Meu primeiro FrameWork',text_color='black')],
    [sg.Text('Digite algo para realizar a busca'), sg.InputText(),sg.FileBrowse('Buscar')],
    [sg.Button('Ok'), sg.Button('Cancel'),sg.Button('Mais')]
]

window = sg.Window('Teste', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Mais':
        (sg.popup('Conhecendo o PySimpleGUI', 'Esse é o meu primeiro codigo'))
    print('You entered', values[0])