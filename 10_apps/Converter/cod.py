import PySimpleGUI as sg

layout = [[sg.Text('Conversor',enable_events = True)],
           [sg.Text('De:'),sg.Spin(['Metros (m)','Centímetros (cm)','Milímetros (mm)'],enable_events=True,size = (20,2),key='lista'),sg.Text('Para:'),sg.Spin(['Metros (m)','Centímetros (cm)','Milímetros (mm)'],enable_events=True,size = (20,2), key = 'lista2')],
          [sg.Button('Converter',size=(15,1), key='Botão') ,sg.Input(size=(50,10),pad=10,border_width=2,tooltip='Digite o valor', enable_events=True, key='input')],
          [sg.Text('Resultado: '),sg.Text('',enable_events = True, key='troca')]
          ]


window = sg.Window('Converter',layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
        
    if event == 'Botão':
        if values['lista'] == 'Metros (m)':
            if values['lista2'] == 'Centímetros (cm)':
                window['troca'].update(float(values["input"])*100)
                
            if values['lista2'] == 'Milímetros (mm)':
                print(f'{float(values["input"])*1000:.1f} Milímetros')
            elif values['lista'] == values['lista2']:
                print('Por favor, mude um dos elementos selecionados')
        elif values['lista'] == 'Centímetros (cm)':
            print('Outro teste')
        elif values['lista'] == 'Quilometros (km)':
            print('Teste')
            
window.close()