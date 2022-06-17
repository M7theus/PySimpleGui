import PySimpleGUI as sg

layout = [
    [sg.Text('Text',enable_events = True, key ='-Text-'),sg.Spin(['item 1','item 2'])],
    [sg.Button('Button',key = '-Button1-')],
    [sg.Input(key = '-Input-')],
    [sg.Text('Test'), sg.Button('Test Button', key= '-Button2-')]
]

window = sg.Window('Converter',layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    if event == '-Button1-':
        window['-Text-'].update(values['-Input-'])
        
    if event == '-Text-':
        print('Text was pressed')
window.close()