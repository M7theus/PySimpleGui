import PySimpleGUI as sg

layout = [[sg.Text('Conversor',enable_events = True),sg.Spin(['Metros (m)','Centímetros (cm)','Quilómetros (km)'],size = (20,10),key='Lista')],
          [sg.Button('Converter',size=(15,1), key='Botão') ,sg.Input(size=(50,10),pad=10,border_width=2,tooltip='Digite o valor',key='Conversor')]
          ]


window = sg.Window('Converter',layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    if event == 'Botão':
        if values == 'Lista':
            if 'Lista'[0]:
                print('Teste lista')

window.close()