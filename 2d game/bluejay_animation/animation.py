import pygame
pygame.init()
class jay:
    def __init__(self):
        self.image1 = pygame.image.load('bluejay-1.png')
        self.image2 = pygame.image.load('bluejay-2.png')
        self.image3 = pygame.image.load('bluejay-3.png')
        self.image4 = pygame.image.load('bluejay-4.png')
        self.image5 = pygame.image.load('bluejay-5.png')
        self.image6 = pygame.image.load('bluejay-6.png')
        self.state = 0
        self.im = pygame.image.load('icon.png')

Width, Height = 1360, 760
win = pygame.display.set_mode((Width, Height))
win.fill((0, 100, 250))
pygame.display.flip()
pygame.display.set_caption('animation')
pygame.display.set_icon(pygame.image.load('icon.png'))
def main():
    i = 0
    p = jay()
    p.state = 1
    p.image1 = pygame.transform.scale(p.image1, (p.image1.get_width()*10, p.image1.get_height()*10))    
    p.image2 = pygame.transform.scale(p.image2, (p.image2.get_width()*10, p.image2.get_height()*10))
    p.image3 = pygame.transform.scale(p.image3, (p.image3.get_width()*10, p.image3.get_height()*10))
    p.image4 = pygame.transform.scale(p.image4, (p.image4.get_width()*10, p.image4.get_height()*10))
    p.image5 = pygame.transform.scale(p.image5, (p.image5.get_width()*10, p.image5.get_height()*10))
    p.image6 = pygame.transform.scale(p.image6, (p.image6.get_width()*10, p.image6.get_height()*10))   
    run = True
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        clock.tick(14)
        if p.state == 1:
            p.im = p.image1
        elif p.state == 2:
            p.im = p.image2
        elif p.state == 3:
            p.im = p.image3
        elif p.state == 4:
            p.im = p.image4
        elif p.state == 5:
            p.im = p.image5
        elif p.state == 6:
            p.im = p.image6
        if p.state >6:
            p.state = 1
        else:
            p.state += 1
        win.fill((0, 100, 250))
        win.blit(p.im, (Width/2 - p.im.get_width()/2, Height/2 - p.im.get_height()/2))
        pygame.display.update()
    pygame.quit()


testboi = 'done'


if __name__ == '__main__':
    main()