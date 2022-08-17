import pygame
import csv
import os

class Tile():
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Tile_map():
    def __init__(self, filename):
        self.tile_size = 16
        self.cdata = filename
        self.start_x, self.start_y = 0, 0
        self.tiles = self.load_tiles()
        self.map_surf = pygame.Surface((self.map_w, self.map_h))
        self.map_surf.fill((0, 120, 250))
        self.load_map()

    def draw_map(self, surface):
        surface.blit(self.map_surf, (0,0))

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surf)

    def read_data(self):
        valmap = []
        with open(os.path.join(self.cdata), 'r') as red:
            data = csv.reader(red, delimiter=',')
            for row in data:
                valmap.append(list(row))
        return valmap
        
    def load_tiles(self):
        map = self.read_data()
        tiles = []
        x, y = 0, 0
        for row in map:
            x = 0
            for col in row:
                if col == '0':
                    tiles.append(Tile('test_img/grass.png', x * self.tile_size, y * self.tile_size))
                elif col == '1':
                    tiles.append(Tile('test_img/dirt.png', x * self.tile_size, y * self.tile_size))
                elif col == '2':
                    pass
                x += 1
            y += 1
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles
