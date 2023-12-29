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

class Settlement_CB(pygame.sprite.Sprite):
    def __init__(self,screen,color):
        super(Settlement_CB,self).__init__()
        x = 700
        y = 250
        pygame.draw.polygon(screen,color,[(x,y),(x,y-30),(x+20,y-50),(x+40,y-30),(x+40,y)])
        pygame.draw.polygon(screen,"black",[(x,y),(x,y-30),(x+20,y-50),(x+40,y-30),(x+40,y)],5)

class Road_CB(pygame.sprite.Sprite):
    def __init__(self,screen,color):
        super(Road_CB,self).__init__()
        first = (800,250)
        second = (850,300)
        pygame.draw.line(self.screen,color,first,second,5)

