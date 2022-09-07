import PySimpleGUI as sg

def get_binary(txt):
	binary = ' '.join(format(ord(i), 'b') for i in txt)
	return binary

layout = [
	[sg.Text('Enter text that you wnat to convert: ')],
	[sg.Input(key='-TEXT-')],
	[sg.Button('Convert', key='-CONVERT-')],
	[sg.Text('', key='-RESULT-', text_color='red', size=(27, 50))]
]

window = sg.Window('Binary converter', layout, size=(300,400), element_justification = 'center')

while True:
	event, value = window.read()

	if event == sg.WIN_CLOSED:
		break
	elif event == '-CONVERT-':
		txt = value['-TEXT-']
		binary = get_binary(txt)
		window['-RESULT-'].update(binary)
		print(binary)


window.close()
