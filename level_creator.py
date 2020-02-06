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

COLORS = {"green":(0,255,0),"blue":(0,0,255),"red":(255,0,0),"white":(255,255,255),"gray":(100,100,100),"black":(0,0,0),"aqua":(91,196,228)}

class Solid_rect():
    def __init__(self, width, height, pos, color=COLORS["gray"]):
        self.width = width
        self.height = height
        self.pos = pos
        self.color = color
        self.fixcolor = color
        self.selected = False
        self.create_image()
        
        
        
    
    def update(self):
        if self.selected == True:
            self.image.blit(self.overlay,(0,0))
        else:
            self.image.blit(self.image,(0,0))
            
    def create_image(self):
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(self.color)
        self.overlay = pygame.Surface((self.width,self.height))
        #unsichtbare Farbe schwarz 0,0,0
        self.overlay.set_colorkey((0,0,0))
        self.overlay.convert_alpha()
        self.overlay.set_alpha(100)
        self.overlay.fill(COLORS["aqua"])

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
solids = []
selected = []
alls = []
alls += solids
clock = pygame.time.Clock()


running = True
while running:
    # ========= pysimplegui ============
    event, values = window.read(timeout=10)
    if event in (None, 'Exit'):
        window.close()
        break
    elif event == 'Add Solid':
        query = values['-QUERY-']
        if query == "":
            newsolid = Solid_rect(100,100,[0,0])
            solids.append(newsolid)
            print("solid")
    
    
    
    # ========== pygame ==========    
    

    
    # --------------- mouse ------------------
    mouse = pygame.mouse
    mousepos = mouse.get_pos()
    left, middle, right = mouse.get_pressed()
    for obj in solids:
        if oldleft and not left and mousepos[0] >= obj.pos[0] and mousepos[0] <= obj.pos[0]+obj.width and mousepos[1] >= obj.pos[1] and mousepos[1] <= obj.pos[1]+obj.height:    
            obj.selected = True
            selected.append(obj)
        
        obj.update()
        
    oldleft, oldmiddle, oldright = left, middle, right
    # ----------------------------------------
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
                
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        for obj in selected:
            if pressed_keys[pygame.K_LSHIFT]:
                obj.width += 2
                obj.create_image()
            else:
                obj.pos[0] += 2
    if pressed_keys[pygame.K_UP]:
        for obj in selected:
            if pressed_keys[pygame.K_LSHIFT]:
                obj.height -= 2
                obj.create_image()
            else:
                obj.pos[1] -= 2
    if pressed_keys[pygame.K_DOWN]:
        for obj in selected:
            if pressed_keys[pygame.K_LSHIFT]:
                obj.height += 2
                obj.create_image()
            else:
                obj.pos[1] += 2
    if pressed_keys[pygame.K_LEFT]:
        for obj in selected:
            if pressed_keys[pygame.K_LSHIFT]:
                obj.width -= 2
                obj.create_image()
            else:
                obj.pos[0] -= 2
    
    
    
    screen.fill(COLORS["white"])
    for solid in solids:
        screen.blit(solid.image,solid.pos)
    pygame.display.update()


window.close()
