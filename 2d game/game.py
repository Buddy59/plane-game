import logging
import subprocess
import sys

try:
    import pygame
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pygame'])
    import pygame
try:
    import pygame_gui
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pygame-textinput'])
    import pygame_gui

Width, Height =(1280, 720)

def start(w, h):
    global Width, Height 
    Width, Height = w, h
    global win
    win = pygame.display.set_mode((Width, Height))
    main_menu()

logging.basicConfig(level = logging.INFO)
from Levels import level_0
win = pygame.display.set_mode((Width, Height))

fps = 60
pygame.init()
pygame.display.set_caption('Crowpy')
pygame.display.set_icon(pygame.image.load('icon.png'))
font = pygame.font.SysFont('Noto Sans Mono', 50)
font1 = pygame.font.SysFont('Noto Sans Mono', 20)
Width, Height =(1280, 720)
win = 0

volume = (0.5)
over = pygame.mixer.Sound('sound/mover.wav')
over.set_volume(volume)
click = pygame.mixer.Sound('sound/click.wav')
click.set_volume(volume)
def option_menu():
    ui = pygame_gui.UIManager((Width, Height))
    clock = pygame.time.Clock()
    color =(50,20,50)
    run = True
    while run:
        tik = clock.tick(fps)
        win.fill(color)
        for p in pygame.event.get():
            if p.type == pygame.QUIT:
                run = False
                sys.exit()

            ui.process_events(p)
        ui.update(tik)
        ui.draw_ui(win)
        pygame.display.update()

#below is level menu, above is option menu

def level_menu():
    ui = pygame_gui.UIManager((Width, Height))
    clock = pygame.time.Clock()
    color =(50,20,50)
    lvlbut = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50,50), (75, 25)), text='Level0', manager=ui)
    run = True
    while run:
        tis = clock.tick(fps)
        win.fill(color)

        for p in pygame.event.get():
            if p.type == pygame.QUIT:
                run = False
                sys.exit()
            if p.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
            if p.type == pygame_gui.UI_BUTTON_PRESSED:
                if p.ui_element == lvlbut:
                    logging.info('test')
                    level_0.start(Width, Height)
                    run = False
            ui.process_events(p)

        ui.update(tis)
        ui.draw_ui(win)

        pygame.display.update()

#below is starting menu, above is level menu
def main_menu():
    clock = pygame.time.Clock()
    color =(50,20,50)
    run = True
    ui = pygame_gui.UIManager((Width, Height))
    lvlbut = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((Width/2-50, Height/2-25), (125, 75)), text='Levels', manager=ui)
    optbut = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((Width/2-50, Height/2+75), (125, 75)), text='Options', manager=ui)
    while run:
        tis = clock.tick(fps)
        win.fill(color)
        
        for p in pygame.event.get():
            if p.type == pygame.QUIT:
                run = False
                sys.exit()
            if p.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
            if p.type == pygame_gui.UI_BUTTON_PRESSED:
                if p.ui_element == lvlbut:
                    logging.info('level menu')
                    level_menu()
                    lvlbut.remove()
                    run = False
                if p.ui_element == optbut:
                    logging.info('option menu')
                    option_menu()
                    run = False
            ui.process_events(p)
        ui.update(tis)
        ui.draw_ui(win)
        pygame.display.update()
            
if __name__ == '__main__':
    start(Width, Height)



