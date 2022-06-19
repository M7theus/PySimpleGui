import PySimpleGUI as sg

layout = [[sg.Text('Conversor', enable_events = True)],[sg.Spin(['Metros (m)','Centímetros (cm)','Quilómetros (km)'])],
          [sg.Button('Converter',size=(15,1)) ,sg.Input('Digite o valor',size=(70,10))]
          ]


window = sg.Window('Converter',layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
window.close()