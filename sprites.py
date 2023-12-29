import pygame

class Lumber_RC(pygame.sprite.Sprite):
    def __init__(self):
        super(Lumber_RC, self).__init__()
        self.surf = pygame.transform.scale_by(pygame.image.load("imgs/lumber.png").convert(),.125)
        self.rect = self.surf.get_rect()
class Brick_RC(pygame.sprite.Sprite):
    def __init__(self):
        super(Brick_RC, self).__init__()
        self.surf = pygame.transform.scale_by(pygame.image.load("imgs/brick.png").convert(),.125)
        self.rect = self.surf.get_rect()
class Ore_RC(pygame.sprite.Sprite):
    def __init__(self):
        super(Ore_RC, self).__init__()
        self.surf = pygame.transform.scale_by(pygame.image.load("imgs/ore.png").convert(),.125)
        self.rect = self.surf.get_rect()
class Grain_RC(pygame.sprite.Sprite):
    def __init__(self):
        super(Grain_RC, self).__init__()
        self.surf = pygame.transform.scale_by(pygame.image.load("imgs/grain.png").convert(),.15)
        self.rect = self.surf.get_rect()
class Wool_RC(pygame.sprite.Sprite):
    def __init__(self):
        super(Wool_RC, self).__init__()
        self.surf = pygame.transform.scale_by(pygame.image.load("imgs/sheep.png").convert(),.25)
        self.rect = self.surf.get_rect()
