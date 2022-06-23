import PySimpleGUI as sg

layout = [
    [
        sg.Input(key='-Input'),
        sg.Spin(['Km to mile,','Kg to pound','sec to min'], key='-unit-'),
        sg.Button('Convert',key='-Convert-')
    ],
    [sg.Text('Output',key='-Output-')]
          ]
window = sg.Window('Converter',layout)

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-CONVERT-':
        input_values = values['-INPUT-']
        if input_values.isnumeric():
            match values['-UNITS-']:
                case 'Km to mile':
                    output = round(float(input_value)*0.6214,2)
                    output_string = f'{input_values} km are {output} miles.'
                case 'Kg to pound':
                    output = round(float(input_value)*2.20452,2)
                    output_string = f'{input_value} kg are {output} pounds'
                case 'sec to min':
                    output = round(float(input_value) /60,2)
                    output_string = f'{input_value} seconds are {output} minutes'
            window['-OUTPUT-'].update(output_string)

window.close()