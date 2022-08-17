import pygame

pygame.init()
Width, Height = 600, 600
win = pygame.display.set_mode((Width, Height))
win.fill((0,255,255))
pygame.display.flip()
run = True
birb = pygame.image.load('crow_fly_12fps.gif')
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    win.blit(birb, (Width/3, Height/2))
    pygame.display.update()
