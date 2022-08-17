import pygame
try: 
    import level_0
except:
    from Levels import level_0
fps = 60
clock = pygame.time.Clock()
pygame.init()
font = pygame.font.SysFont('Noto Sans Mono', 50)
font1 = pygame.font.SysFont('Noto Sans Mono', 20)
Width, Height =(1280, 720)

def start(w, h):
    global Width, Height 
    Width, Height = w, h
    global win
    win = pygame.display.set_mode((Width, Height))
    sreen(0)

win = pygame.display.set_mode((Width, Height), pygame.RESIZABLE)
w1, h1 = pygame.display.get_window_size()
if w1 >= 1280:
    Width = w1
if h1 >= 720:
    Height = h1
pygame.mixer.init()
over = pygame.mixer.Sound('sound/mover.wav')
over.set_volume(0.3)
click = pygame.mixer.Sound('sound/click.wav')
click.set_volume(0.5)
buttons = []

def upbutn(some):
    i = 0
    o = 0
    for e in buttons:
        x, y = pygame.mouse.get_pos()
        if e.x<x<e.x+e.w:
            if e.y<y<e.y+e.h:
                color = e.colorhov
                i += 1
            else: 
                color = e.color
                o += 1
        else: 
            color = e.color
            o += 1
        pygame.draw.rect(win, color, (e.x, e.y, e.w, e.h))
        if e.n == 1:
            text = font.render(e.text, True, e.textc)
        if e.n == 2:
            text = font1.render(e.text, True, e.textc)
        win.blit(text, (e.x+((e.w-text.get_width())/2),e.y+((e.h-text.get_height())/2)))

    if i > 0:
        if o > 0 & o < 1:   
            if some != 1:
                over.play()
                some = 1
        else:
            some = 0
    else:
        some = 0
             
    return some
        
        
        

def butn(x,y,w,h,r,g,b,text,c,n, f):
    e = buton()
    e.x = x
    e.y = y
    e.w = w
    e.h = h
    e.color = (r,g,b)
    e.colorhov = (r-50,g-50,b-50)
    e.text = text
    e.textc = c
    e.n = n
    e.f = f
    buttons.append(e)

class buton:
    def init(self):
        self.x
        self.y
        self.w
        self.h
        self.color
        self.colorhov
        self.text
        self.textc
        self.n
        self.f = 0
        

def sreen(text):
    butn(Width/2-150, Height/2 - 50, 300, 100, 255, 255, 255, 'Retry', (0,0,0), 1, 1)
    butn(Width/2-150, Height/2 + 75, 300, 100, 255, 255, 255, 'Quit', (0,0,0), 1, 2)
    run = True
    some = 0
    while run:
        clock.tick(fps)
        win.fill((0,0,0))
        some = upbutn(some)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
                quit
            if e.type == pygame.MOUSEBUTTONDOWN:
                for e in buttons:
                    x, y = pygame.mouse.get_pos()
                    if e.x<x<e.x+e.w:
                        if e.y<y<e.y+e.h:
                            click.play()
                            if e.f == 1:
                                retry(text)
                                run = False
                                quit
                            elif e.f == 2:
                                run = False
                                quit
        pygame.display.update()


def retry(level):
    if level == 0:
        level_0.level()


if __name__ == '__main__':
    start(1280, 720)
