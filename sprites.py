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
        first = (825,250)
        second = (875,200)
        b_first = (822,253)
        b_second = (878,197)
        pygame.draw.line(screen,"Black",b_first,b_second,10)
        pygame.draw.line(screen,color,first,second,6)

class Development_CB(pygame.sprite.Sprite):
    def __init__(self,screen,afford):
        super(Development_CB,self).__init__()
        x= 1100
        y = 200
        w = 50
        h = 65
        if not afford:
            pygame.draw.rect(screen,"black",[(x-3,y-3),(w+6,h+6)])
            pygame.draw.rect(screen,"gray15",[(x,y),(w,h)])
            return
        pygame.draw.rect(screen,"black",[(x-3,y-3),(w+6,h+6)])
        pygame.draw.rect(screen,"gray80",[(x,y),(w,h)])
        rect = pygame.draw.circle(screen,"red",(x+w//2,y+h//2),20)
        pygame.draw.circle(screen,"yellow",(x+w//2,y+h//2),15)
        pygame.draw.circle(screen,"gray80",(x+w//2,y+h//2),5)
        rect.y +=10
        rect.height -=10
        rect = pygame.draw.arc(screen,"blue",rect,3.14,0,6)
        rect.width -=12
        rect.x += 6
        rect.height -=5
        pygame.draw.rect(screen,"blue",rect)

class End_Turn_Button(pygame.sprite.Sprite):
    def __init__(self,front_end,screen):
        super(End_Turn_Button,self).__init__()
        self.name = "end_turn"
        x = 1100 
        y = 625
        w = 150
        h = 70
        self.rect = pygame.draw.rect(screen,"black",[(x,y),(w,h)])
        font = pygame.font.SysFont(None, 48)
        img = font.render("End Turn",True,"white")
        screen.blit(img,(x+5,y+18))
        front_end.turn_sprites.add(self)
