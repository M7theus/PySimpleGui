import PySimpleGUI as sg 

layout = [
    [sg.Text('Programa')],
    [sg.Text('Digite algo: '),sg.Inputext()]
    [sg.Button('Avançar')]
]

window = sg.Window('Desafio 01',layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break