import pygame
import PySimpleGUI as sg
import os

"""
    Demo of integrating PyGame with PySimpleGUI, the tkinter version
    A similar technique may be possible with WxPython
    To make it work on Linux, set SDL_VIDEODRIVER like
    specified in http://www.pygame.org/docs/ref/display.html, in the
    pygame.display.init() section.
"""
pre_layout = [[sg.Text("Enter width and height of your level")],
              [sg.Text("width:"),sg.Input(key="-WIDTH-")],
              [sg.Text("height:"),sg.Input(key="-HEIGHT-")],
              [sg.Button("Confirm")]]

# --------------------- PySimpleGUI window layout and creation --------------------


pre_window = sg.Window('Level Creator', pre_layout, finalize=True,resizable=False)

while True:

    event, values = pre_window.read()
    if event in (None, 'Exit'):
        break
    if event == "Confirm":
        width = values["-WIDTH-"]
        height = values["-HEIGHT-"]
        width = int(width)
        height = int(height)
        layout = [[sg.Text('Command Line')],
                  [sg.Input(key='-QUERY-', do_not_clear=True)],
                  [sg.Button('Add Solid')],
                  [sg.Graph((width, height), (0, 0), (width, height),
                            background_color='lightblue', key='-GRAPH-')],
                  [sg.Exit()]]
        window = sg.Window('Level Creator', layout, finalize=True,resizable=False)
        break
pre_window.close()
graph = window['-GRAPH-']

# -------------- Magic code to integrate PyGame with tkinter -------
embed = graph.TKCanvas
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
# change this to 'x11' to make it work on Linux
os.environ['SDL_VIDEODRIVER'] = 'windib'

# ----------------------------- PyGame Code -----------------------------

screen = pygame.display.set_mode((width,height))
screen.fill(pygame.Color(255, 255, 255))

pygame.display.init()
pygame.display.update()

while True:


    event, values = window.read(timeout=10)
    if event in (None, 'Exit'):
        window.close()
        break
    elif event == 'Add Solid':
        query = values['-QUERY-']
        if query == "solid":
            pass
        print("solid")
    elif event == 'Draw':
        pygame.draw.circle(screen, (0, 0, 0), (250, 250), 125)
    pygame.display.update()


window.close()
