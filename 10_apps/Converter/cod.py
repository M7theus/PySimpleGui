import PySimpleGUI as sg

layout = [
    [sg.Text('Text'),sg.Spin(['item 1','item 2'])],
    [sg.Button('Button')],
    [sg.Input()]
]

sg.Window('Converter',layout).read()