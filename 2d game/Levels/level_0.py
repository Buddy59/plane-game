import pygame
try:
    import death_screen
except:
    from Levels import death_screen
fps = 60
clock = pygame.time.Clock()
pygame.init()
font = pygame.font.SysFont('Noto Sans Mono', 50)
font1 = pygame.font.SysFont('Noto Sans Mono', 20)
Width, Height = (1280, 720)
win = 0
def start(w, h):
    global Width, Height
    Width = w 
    Height = h
    global win
    win = pygame.display.set_mode((Width, Height), pygame.RESIZABLE)
    level()


buttons = []
bl = []
pygame.mixer.init()
jump_sound = pygame.mixer.Sound('sound/jump.wav')
jump_sound.set_volume(0.3)
glide_sound = pygame.mixer.Sound('sound/glidestart.wav')
glide_sound.set_volume(0.3)
land = pygame.mixer.Sound('sound/land.wav')
land.set_volume(0.3)
def butn(x,y,w,h,r,g,b):
    e = buton()
    e.x = x
    e.y = y
    e.w = w
    e.h = h
    e.rect = pygame.Rect(x, y, w, h)
    e.color = (r,g,b)
    bl.append(e.rect)
    buttons.append(e)

class buton:
    def init(self):
        self.x
        self.y
        self.rect
        self.w
        self.h
        self.color

class player():
    def init(self):
        self.img = 0
        self.iimg = 0
        self.fimg1 = 0
        self.fimg2 = 0
        self.x = 0
        self.y = 0
        self.state = 1
        self.gimg = 0

        
def pl():
    e = player()
    e.iimg = pygame.image.load('icon.png')
    e.fimg1 = pygame.image.load('img/crow_fall_1.png')
    e.fimg2 = pygame.image.load('img/crow_fall_2.png')
    e.gimg = pygame.transform.rotate(pygame.image.load('img/crow_fall_1.png'), -15)
    e.img = e.iimg
    e.x = 50
    e.y = 180
    e.state = 1
    return e

def colsion(playrec):
    top, bot, lef, rig = 0, 0, 0, 0
    tri,tle,ble,bri = 0,0,0,0
    for x in bl:
        if x.collidepoint(playrec.x+playrec.width/2,playrec.top):
            top = 1
        if x.collidepoint(playrec.left, playrec.y+playrec.h/2):
            lef = 1
        if x.collidepoint(playrec.right, playrec.y+playrec.h/2):
            rig = 1
        if x.collidepoint(playrec.x+playrec.w/2, playrec.bottom):
            bot = 1
        if x.collidepoint(playrec.bottomright):
            bot = 1
        if x.collidepoint(playrec.bottomleft):
            bot = 1
    return lef, rig, top, bot
        
        


def level():
    butn(50, 200, 100, 10, 0, 0, 0)
    butn(150, 170, 10, 40, 0, 0, 0)
    butn(100, 400, 100, 10, 0, 0, 0)
    butn(220, 200, 100, 10, 0,0,0,)
    butn(200, 300, 100, 10,0,0,0)
    butn(200, 100, 100, 10, 0, 0, 0)
    butn(Width - 200, 400, 200, 10,0,0,0)
    play = pl()
    quif = False
    vel = 1
    hvel = 0
    o = 0
    p = 0
    run = True
    while run:
        clock.tick(fps)
        win.fill((255,255,255))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
                quif = True
        if play.y > Height + play.img.get_height():
            run = False
        for b in buttons:
            pygame.draw.rect(win, b.color, (b.x, b.y, b.w, b.h))
            playrec = pygame.Rect(play.x, play.y, play.img.get_width(), play.img.get_height())
        keys = pygame.key.get_pressed()
        cleft, cright, cup, cdown = colsion(playrec)
        if cdown > 0:
            vel = 0
            play.state = 1
            p += 1
            if keys[pygame.K_w]:
                jump_sound.play()
                vel -=10    
        elif vel < 0:
            p = 0 
            vel += 1/2
        elif vel >= 0 and vel < 5: 
            p = 0
            vel += 1/4
        if keys[pygame.K_SPACE] and vel > 0:
            vel = 3/4
            play.state = 4
            o = 1
        else:
            o = 0
        if o == 1:
            glide_sound.play()
        if keys[pygame.K_a] & keys[pygame.K_d]:
            hvel = 0
        elif keys[pygame.K_a]:
            hvel = -2
        elif keys[pygame.K_d]:
            hvel = 2
        elif not keys[pygame.K_a] and not keys[pygame.K_d]:
            hvel = 0
        if cright > 0:
            if hvel > 0:
                hvel = 0
        if cleft > 0:
            if hvel < 0:
                hvel = 0
        if cup > 0:
            if vel < 0:
                vel = 0
        if vel > 1:
            play.state = 3
        elif vel < 0:
            play.state = 2
        if play.state == 1:
            play.img = play.iimg
        elif play.state == 2:
            play.img = play.fimg1
        elif play.state == 3:
            play.img = play.fimg2
        elif play.state == 4:
            play.img = play.gimg
        if play.x <= 0:
            if hvel < 0 :
                hvel = 0
        if play.x + play.img.get_width() >= Width:
            if hvel > 0:
                hvel = 0
        if play.y <= 0:
            if vel < 0:
                vel = 0
        play.y += vel
        play.x += hvel
        if p == 1:
            land.play()
        win.blit(play.img, (play.x, play.y))
        pygame.display.update()
    if quif == False:
        death_screen.start(Width, Height)

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
                some = 1
        else:
            some = 0
    else:
        some = 0
             
    return some

if __name__ == '__main__':
    start(1280, 720)
