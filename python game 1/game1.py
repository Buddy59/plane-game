import sys
import subprocess
try:
    import pygame
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pygame'])
    import pygame
pygame.init()
import os
try:
    import numpy as np
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'numpy'])
    import numpy as np
import random


Width, Height = 1360, 650
win = pygame.display.set_mode((Width, Height))
#above is window items and imports/below is death screen
quit_img = pygame.image.load('quit.png')
retry_img = pygame.image.load('retry.png')
pygame.display.set_caption('Plane Game')
pygame.display.set_icon(pygame.image.load('game assets crow/icon.png'))

def death():
    quit_rect = pygame.Rect(Width/2-quit_img.get_width()/2, Height/2-quit_img.get_height()/4+100, quit_img.get_width(), quit_img.get_height())
    retry_rect = pygame.Rect(Width/2-retry_img.get_width()/2, Height/2-retry_img.get_height()/2+5, retry_img.get_width(), retry_img.get_height())
    win.fill((0, 100, 250))
    run = True
    clock = pygame.time.Clock()
    THIME = str(time)
    text = 'You survived ' + THIME + ' Seconds'
    font = pygame.font.SysFont('Consolas', 30)
    while run:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                X, Y = pygame.mouse.get_pos()
                if quit_rect.x < X < quit_rect.x + quit_rect.width:
                    if quit_rect.y < Y < quit_rect.y + quit_rect.height:
                        run = False
                        pygame.quit()
                        quit()
                if retry_rect.x < X < retry_rect.x + retry_rect.width:
                    if retry_rect.y < Y < retry_rect.y + retry_rect.height:
                        run = False
                        retry()
        win.blit(retry_img, (retry_rect.x, retry_rect.y))
        win.blit(quit_img, (quit_rect.x, quit_rect.y))
        win.blit(font.render(text, True, (0,0,0)), (Width/2 - 200, Height/2 - 100))
        pygame.display.update()
    
def retry():
    win.fill((0, 100, 250))
    pygame.display.update()
    while len(objects_rect) > 0:
        objects_rect.pop()
    while len(objects_surf) > 0:
        objects_surf.pop()
    while len(birb_list) > 0:
        birb_list.pop()
    game()
#below is game, above is death screen
obtime = 4000
difficulty = 1
control_method = 0
FPS = 60
vel = 5
Plane_Image=pygame.image.load('pixilart-drawing.png')
objects_surf = []
objects_rect = []
birb_list = []
bird_rect_list = []
objects_spaceing = 105
font = pygame.font.SysFont('Consolas', 30)
funky = 0
def clouds ():
    if funky == 1:
        run = False
    i = random.randint(1, 3)
    if i == 1:
        cloud = pygame.transform.scale(pygame.image.load("clouds/cloud_1.png"), (400, 200))
    if i == 2:
        cloud = pygame.transform.scale(pygame.image.load("clouds/cloud_2.png"), (400, 200))
    if i == 3:
        cloud = pygame.transform.scale(pygame.image.load("clouds/ cloud_3.png"), (400, 200))
    
    x = Width
    y = random.randint(0, Height - cloud.get_height())
    win.blit(cloud, (x, y))
    lonjor = pygame.Rect(x, y, cloud.get_width(), cloud.get_height())
    objects_surf.append(cloud)
    objects_rect.append(lonjor)
    i+=1

def update_objects(pal):
    i = 0
    for cloud in objects_surf:
        hog = objects_rect[i]
        if hog.x > 0 - hog.width:
            hog.x -= vel
        elif hog.x <= 0 - hog.width:
            objects_surf.pop(i)
            objects_rect.pop(i)
        win.blit(cloud, (hog.x, hog.y))
        i += 1
    for en in birb_list:
        en.rect.x -= vel
    
class crow:
    def __init__(self):
        self.image1 = pygame.transform.flip(pygame.image.load('game assets crow/crow_fly_strip1.png'), True, False)
        self.image2 = pygame.transform.flip(pygame.image.load('game assets crow/crow_fly_strip2.png'), True, False)
        self.image3 = pygame.transform.flip(pygame.image.load('game assets crow/crow_fly_strip3.png'), True, False)
        self.image4 = pygame.transform.flip(pygame.image.load('game assets crow/crow_fly_strip4.png'), True, False)
        self.image5 = pygame.transform.flip(pygame.image.load('game assets crow/crow_fly_strip5.png'), True, False)
        self.image6 = pygame.transform.flip(pygame.image.load('game assets crow/crow_fly_strip6.png'), True, False)
        self.state = 1
        self.y = random.randint(0, Height-self.image1.get_height())
        self.rect = pygame.Rect(Width, self.y, self.image1.get_width(), self.image1.get_height())
        self.im = self.image1
        self.type = 0
class bluejay:
    def __init__(self):
        self.image1 = pygame.transform.flip(pygame.image.load('game assets crow/bluejay-1.png'), True, False)            
        self.image2 = pygame.transform.flip(pygame.image.load('game assets crow/bluejay-2.png'), True, False)        
        self.image3 = pygame.transform.flip(pygame.image.load('game assets crow/bluejay-3.png'), True, False)        
        self.image4 = pygame.transform.flip(pygame.image.load('game assets crow/bluejay-4.png'), True, False)        
        self.image5 = pygame.transform.flip(pygame.image.load('game assets crow/bluejay-5.png'), True, False)        
        self.image6 = pygame.transform.flip(pygame.image.load('game assets crow/bluejay-6.png'), True, False)        

def enemy():
    cranc = random.randint(0, 1)
    en_ob = crow()
    y = random.randint(0, Height-en_ob.im.get_height())
    en_re = en_ob.rect
    if cranc == 0:
        win.blit(en_ob.im, (en_re.x, en_re.y))
        en_ob.state == 0
    elif cranc == 1:
        win.blit(bluejay().image1, (en_re.x, en_re.y))
        en_ob.state = 7
        en_ob.type = 1
    birb_list.append(en_ob)
    

def draw_win(pal, text):
    win.fill((0, 100, 250))
    update_objects(pal)
    win.blit(Plane_Image, (pal.x, pal.y))
    win.blit(font.render(text, True, (0, 0, 0)), (0, 0))
    for en in birb_list:
        win.blit(en.im, (en.rect.x, en.rect.y))
    pygame.display.update()

def recre(um, en):
    re = pygame.Rect(en.rect.x, en.rect.y, um.get_width(), um.get_height())
    return re

def birb_update(pal):
    for en in birb_list:
        if en.rect.x < 0 - en.rect.width:
            birb_list.pop(0)
        elif en.state == 1:
            en.rect = pygame.Rect(en.rect.x, en.rect.y, en.image1.get_width(), en.image1.get_height())
            en.im = crow().image1    
        elif en.state == 2:
            en.rect = pygame.Rect(en.rect.x, en.rect.y, en.image2.get_width(), en.image2.get_height())
            en.im = crow().image2
        elif en.state == 3:
            en.rect = pygame.Rect(en.rect.x, en.rect.y, en.image3.get_width(), en.image3.get_height())
            en.im = crow().image3
        elif en.state == 4:
            en.rect = pygame.Rect(en.rect.x, en.rect.y, en.image4.get_width(), en.image4.get_height())
            en.im = crow().image4
        elif en.state == 5:
            en.rect = pygame.Rect(en.rect.x, en.rect.y, en.image5.get_width(), en.image5.get_height())
            en.im = crow().image5
        elif en.state == 6:
            en.rect = pygame.Rect(en.rect.x, en.rect.y, en.image6.get_width(), en.image6.get_height())
            en.im = crow().image6
        elif en.state == 7:
            en.rect = recre(bluejay().image1, en)
            en.im = bluejay().image1
        elif en.state == 8:
            en.rect = recre(bluejay().image2, en)
            en.im = bluejay().image2
        elif en.state == 9:
            en.rect = recre(bluejay().image3, en)
            en.im = bluejay().image3
        elif en.state == 10:
            en.rect = recre(bluejay().image4, en)
            en.im = bluejay().image4
        elif en.state == 11:
            en.rect = recre(bluejay().image5, en)
            en.im = bluejay().image5
        elif en.state == 12:
            en.rect = recre(bluejay().image6, en)
            en.im = bluejay().image6
        en.state += 1  
        if en.type == 0: 
            if en.state > 6:
                en.state = 1
        elif en.type == 1:
            if en.state > 12:
                en.state = 7

def collision(pal):
    x = 0
    if birb_list.__len__() > 0:
        for en in birb_list:
            if en.rect.colliderect(pal):
                x += 1
            else:
                x += 0
        if x > 0:
            return False
        else:
            return True
    
    return True
    

def game():
    text = '0 Sec'
    pal = pygame.Rect(100, 100, 70, 93)
    clock = pygame.time.Clock()
    run = True
    tim = 1
    co = 0
    Score = 1
    i = 0
    pafne = 0
    hah = 0
    lim = 200
    global time
    time = 0
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    while run:
        if difficulty == 1:
            pafne = 75
        clock.tick(FPS)
        run = collision(pal)
        if hah < pafne:
            hah+=1
        elif hah == pafne:
            hah=0
            enemy()
        if i < lim: 
            i+=1
        else:
            clouds()
            i=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()
            if event.type == pygame.USEREVENT:
                time += 1
                text = str(time) + ' Sec'

        tim += 1
        if tim == 60:
            Score += 1
            tim = 1
        limit = 5
        if co < limit:
            co += 1
        elif co == limit:
            birb_update(pal)
            co = 0
        keys_pressed = pygame.key.get_pressed()
        #wasd
        if control_method == 0:
            if keys_pressed[pygame.K_a]:
                if pal.x >= 0:
                    pal.x -= vel
            if keys_pressed[pygame.K_d]:
             if pal.x <= win.get_width() - pal.width:
                 pal.x += vel
            if keys_pressed[pygame.K_s]:
                if pal.y <= win.get_height() - pal.height:
                    pal.y += vel
            if keys_pressed[pygame.K_w]:
                if pal.y >= 0:
                    pal.y -= vel
        #arrows
        if control_method == 1:
            if keys_pressed[pygame.K_LEFT]:
                if pal.x >= 0:
                    pal.x -= vel
            if keys_pressed[pygame.K_RIGHT]:
                if pal.x <= win.get_width() - pal.width:
                    pal.x += vel
            if keys_pressed[pygame.K_DOWN]:
                if pal.y <= win.get_height() - pal.height:
                    pal.y += vel
            if keys_pressed[pygame.K_UP]:
                if pal.y >= 0:
                    pal.y -= vel

        draw_win(pal, text)
    TIME = time
    death()
    
## above this line is gameplay, below is menu
start_button = pygame.image.load('start.png')

def draw_win1():
    win.fill((0, 100, 250))
    x = win.get_width()/2 - start_button.get_width()/2
    y = win.get_height()/2 - start_button.get_height()/2
    win.blit(start_button, (x, y))
    pygame.display.update()


def main():
    start = pygame.Rect(Width/2 - start_button.get_width()/2, Height/2 - start_button.get_height()/2, start_button.get_width(), start_button.get_height())
    run = True
    like = pygame.time.Clock()
    while run:
        like.tick(FPS)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if start.x < x < start.x + start_button.get_width(): 
                    if start.y < y < start.y + start_button.get_height():
                        run = False
        draw_win1()

    game()

if __name__ == "__main__":
    main()

