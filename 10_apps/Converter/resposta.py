import PySimpleGUI as sg

layout = [
    [
        sg.Input(key='-Input'),
        sg.Spin(['Km to mile,','Kg to pound','sec to min'], key='-unit-'),
        sg.Button('Convert',key='-Convert-')
    ],
    [sg.Text('Output',key='-Output-')]
          ]
window = sg.Window('Converter',layout).read()