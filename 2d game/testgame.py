import pygame
import test as t
win = pygame.display.set_mode((1280, 720))
class player():
    def __init__(self, x, y, surface):
        self.state = 0
        self.max_vel = 6
        self.glide = False
        self.left = False
        self.jump = False
        self.img = pygame.image.load('icon.png')
        self.rec = self.img.get_rect()
        self.rec.x, self.rec.y = x, y
        self.dx, self.dy = 0, 0
        self.bounds = surface.get_size()
        self.jumpav = False
        self.ground = False

    def movex(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.left = True
            if self.rec.x + self.rec.w < self.bounds[0]:
                if self.dx < self.max_vel:
                    self.dx += 1
        elif keys[pygame.K_a]:
            self.left = False
            if self.rec.x > 0:
                if self.dx > -self.max_vel:
                    self.dx -= 1
        elif keys[pygame.K_d] != True and keys[pygame.K_a] != True:
            self.dx = 0
        if self.rec.x + self.rec.w > self.bounds[0]:
            self.dx = 0
            self.rec.x = self.bounds[0] - self.rec.w
        elif self.rec.x < 0:
            self.rec.x = 0
            self.dx = 0
        
    def movey(self):
        if self.dy < self.max_vel:
            self.dy += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.max_vel = 2
            self.state = 3
            if self.dy > 2:
                self.dy = 2
            self.glide = True
        else:
            self.max_vel = 4
            self.glide = False

    def sprite_update(self):
        if self.state == 0:
            self.img = pygame.image.load('icon.png')
        elif self.state == 1:
            self.img = pygame.image.load('img/crow_fall_1.png')
        elif self.state == 2:
            self.img = pygame.image.load('img/crow_fall_2.png')
        elif self.state == 3:
            self.img = pygame.transform.rotate(pygame.image.load('img/crow_glide.png'), 2)
        if self.left == False:
            img = pygame.transform.flip(self.img, True, False)
            self.img = img
    

    def collision(self, tiles):
        self.jumpav = False
        self.max_vel = 6
        keys = pygame.key.get_pressed()
        l, r, t, b = self.rec.left, self.rec.right, self.rec.top, self.rec.bottom
        x = self.rec.x + self.rec.w/2
        y = self.rec.y + self.rec.h/2
        for tile in tiles:
            if tile.rect.collidepoint(l, y):
                if self.dx < 0:
                    self.dx = 0
            elif tile.rect.collidepoint(r, y):
                if self.dx > 0:
                    self.dx = 0
            if tile.rect.collidepoint(x, t):
                if self.dy < 0:
                    self.dy = 2
            elif tile.rect.collidepoint(x, b):
                if self.dy > 0:
                    self.dy = 0
                    self.state = 0
                if self.dy == 0:
                    if keys[pygame.K_w]:
                        self.dy -=10 
                        self.state = 1

    def update(self, tiles, surface):
        self.movex()
        self.movey()
        self.collision(tiles)
        if self.dy > 0 and self.glide == False:
            self.state = 2
        self.rec.x += self.dx
        self.rec.y += self.dy
        self.sprite_update()
        surface.blit(self.img, (self.rec.x, self.rec.y))



def game_loop(filename):
    run = True
    clock = pygame.time.Clock()
    pan = t.Tile_map(filename)
    pal = player(pan.start_x, pan.start_y, win)
    while run:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              run = False
            if event.type == pygame.KEYDOWN:
                pal.jump = True
    
        pan.draw_map(win)
        pal.update(pan.tiles, win)
        pygame.display.update()
        clock.tick(60)

game_loop('test_img/test.csv')

