#! python3

import PySimpleGUI as sg
import pyautogui

layoutMouse = sg.Frame('Mouse Location', [
    [sg.Text('', size=(10, 1), font='Helvetica 20', justification='center', key='_MousePositionX_')],
    [sg.Text('', size=(10, 1), font='Helvetica 20', justification='center', key='_MousePositionY_')]
])
layoutKB = sg.Frame('Keyboard History', [
    [sg.Text('Last key pressed:', size=(15,1), font='Helvetica 20', justification='center')],
    [sg.Text('', font='Helvetica 20', size=(15,1), justification='center', key='_KBHistory_')]
])

layout = [
    [layoutMouse, layoutKB],
    [sg.Button('Move to Center', key = '_btnCenter_', size=(15,3)), sg.Exit(size=(15,3))]
]

window = sg.Window('mouseKBtracker.py by JZ', return_keyboard_events=True, use_default_focus=False).Layout(layout)
x1, y1 = pyautogui.size()

while True:
    event, values = window.ReadNonBlocking()

    if event == '_btnCenter_':
        pyautogui.moveTo(x1/2, y1/2)
    elif event == 'Exit' or values is None:
        break

    x, y = pyautogui.position()
    MouseUpdateX = window.FindElement('_MousePositionX_').Update('X: {}'.format(str(x).rjust(4)))
    MouseUpdateY = window.FindElement('_MousePositionY_').Update('Y: {}'.format(str(y).rjust(4)))
    KBUpdate = window.FindElement('_KBHistory_').Update(event)