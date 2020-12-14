import PySimpleGUI as sg

sg.LOOK_AND_FEEL_TABLE['CalcTheme'] = {'BUTTON': ('white','#F2F5FF'),
                                       'BACKGROUND': '#30362F'
                                    }

sg.set_options(background_color="#30362F", button_color=('black', '#F2F5FF'), border_width=1, icon='calc_icon.ico')
layout = [[sg.Text("0", size=(12,0), key='DISPLAY', justification='r', background_color="#010001", text_color='#FF1B1C', font="Digital-7 33")],
         [sg.Button("C", font=("Arial", 18, "bold"), size=(3,1)), sg.Button("CE", font=("Arial", 18, "bold"), size=(3,1)), sg.Button("%", font=("Arial", 18, "bold"), size=(3,1)), sg.Button("÷", font=("Arial", 18, "bold"), size=(3,1))],
         [sg.Button("7", font=("Arial", 18, "bold"), size=(3,1)), sg.Button("8", font=("Arial", 18, "bold"), size=(3,1)), sg.Button("9", font=("Arial", 18, "bold"), size=(3,1)), sg.Button("x", font=("Arial", 18, "bold"), size=(3,1))],
         [sg.Button("4", font=("Arial", 18, "bold"), size=(3,1)), sg.Button("5", font=("Arial", 18, "bold"), size=(3,1)), sg.Button("6", font=("Arial", 18, "bold"), size=(3,1)), sg.Button("-", font=("Arial", 18, "bold"), size=(3,1))],
         [sg.Button("1", font=("Arial", 18, "bold"), size=(3,1)), sg.Button("2", font=("Arial", 18, "bold"), size=(3,1)), sg.Button("3", font=("Arial", 18, "bold"), size=(3,1)), sg.Button("+", font=("Arial", 18, "bold"), size=(3,1))],
         [sg.Button("0", font=("Arial", 18, "bold"), size=(3,1)), sg.Button(".", font=("Arial", 18, "bold"), size=(3,1)), sg.Button("=", focus=True, button_color=('black', '#C75000'), font=("Arial", 18, "bold"), size=(7,1))]]

window = sg.Window("Calculator", layout, return_keyboard_events=True)

display = ''
equal = ''
answer = ''
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'C' or event == 'CE':
        equal = ''
        window.FindElement('DISPLAY').update(equal)
    elif event in '0123456789+-.':
        equal += event
        window['DISPLAY'].update(equal)
    elif event == 'x':
        equal += '*'
        window.FindElement('DISPLAY').update(equal)
    elif event == '÷':
        equal += '/'
        window.FindElement('DISPLAY').update(equal)
    elif event == '%': 
        equal += '%'
        window.FindElement('DISPLAY').update(equal)
        for operation in equal:
            if operation in '+-':
                new_equal = equal.split(operation)
                equal = [new_equal[0] + operation + new_equal[1].replace('%', '*0.01*') + new_equal[0] for operation in equal if operation in '+-']
                equal = equal[0]
            elif operation in '%*/':
                equal = equal.replace('%', '*0.01')
    
    # elif len(equal) > 11:
    #     equal = 'ERROR'
    #     window.FindElement('DISPLAY').update(equal)
    # elif event not in equal:
    #     equal = 'ERROR'
    #     window.FindElement('DISPLAY').update(equal)
    elif event == '=':
        answer = str(eval(equal))
        window.FindElement('DISPLAY').update(answer)

window.close()