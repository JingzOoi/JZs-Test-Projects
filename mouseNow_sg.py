#! python3

import PySimpleGUI as sg
import pyautogui

layout = [
            [sg.Text('Mouse position: ')],
            [sg.Text('', size=(15,1), font='Helvetica 20', justification='center', key='_text_')],
            [sg.Exit(), sg.Button('Move To Center', key='_btnCenter_')]
         ]

window = sg.Window('MouseNow.py').Layout(layout)
x1, y1 = pyautogui.size()

while True:
    event, values = window.ReadNonBlocking()

    if event == '_btnCenter_':
        pyautogui.moveTo(x1/2, y1/2)
    elif event == 'Exit' or values is None:
        break

    x, y = pyautogui.position()
    win = window.FindElement('_text_').Update('X: {} | Y: {}'.format(str(x).rjust(4),str(y).rjust(4)))