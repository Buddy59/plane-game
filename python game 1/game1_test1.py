import pygame
pygame.init()
screen = pygame.display.set_mode((128, 128))
text = '10'
font = pygame.font.SysFont('Consolas', 30)
i=0
screen.fill((255, 255, 255))
screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
pygame.display.update()

while True:
    i+=1
    print(i)