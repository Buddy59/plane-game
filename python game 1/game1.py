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

TIME = 0

Width, Height = 900, 500
win = pygame.display.set_mode((Width, Height))
#above is window items and imports/below is death screen
quit_img = pygame.image.load('quit.png')
retry_img = pygame.image.load('retry.png')



def death():
    quit_rect = pygame.Rect(Width/2-quit_img.get_width()/2, Height-quit_img.get_height()*1.5, quit_img.get_width(), quit_img.get_height())
    retry_rect = pygame.Rect(Width/2-retry_img.get_width()/2, Height/2-retry_img.get_height()/2+5, retry_img.get_width(), retry_img.get_height())
    win.fill((0, 100, 250))
    run = True
    clock = pygame.time.Clock()
    THIME = str(TIME)
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
objects_spaceing = 105
font = pygame.font.SysFont('Consolas', 30)
funky = 0
def clouds ():
    if funky == 1:
        run = False
    i = random.randint(1, 3)
    if i == 1:
        cloud = pygame.image.load("clouds/cloud_1.png")
    if i == 2:
        cloud = pygame.image.load("clouds/cloud_2.png")
    if i == 3:
        cloud = pygame.image.load("clouds/ cloud_3.png")
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
    



def draw_win(pal, text):
    win.fill((0, 100, 250))
    update_objects(pal)
    win.blit(Plane_Image, (pal.x, pal.y))
    win.blit(font.render(text, True, (0, 0, 0)), (0, 0))
    pygame.display.update()

def collision(pal):
        if pal.collidelist(objects_rect) >= 0:
            return False
        else:
            return True

def game():
    text = '0 Sec'
    pal = pygame.Rect(100, 100, 70, 93)
    clock = pygame.time.Clock()
    run = True
    tim = 1
    Score = 1
    i = 0
    time = 0
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    while run:
        if difficulty == 1:
            lim = 50
        clock.tick(FPS)
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
        run = collision(pal)
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

