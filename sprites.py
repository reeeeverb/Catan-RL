import pygame

class Terrain_Tile(pygame.sprite.Sprite):
    def __init__(self, screen, terrain,x,y,index,number):
        super(Terrain_Tile, self).__init__()
        font = pygame.font.SysFont(None, 48)
        self.index = index
        terrain_to_color = {"Mountains":"gray","Hills":"0xB22222","Forest":"0x023020","Fields":"0xcac407","Pasture":"0x5adc14","Desert":"navajowhite"}
        color = terrain_to_color[terrain]
        pygame.draw.polygon(screen,color,[(x,y),(x-50,y-25),(x-50,y-75),(x,y-100),(x+50,y-75),(x+50,y-25)])
        self.rect = pygame.draw.polygon(screen,"black",[(x,y),(x-50,y-25),(x-50,y-75),(x,y-100),(x+50,y-75),(x+50,y-25)],4)
        img = font.render(str(number),True,"aqua")
        screen.blit(img,(x-10,y-65))

class Dice(pygame.sprite.Sprite):
    def __init__(self, board, screen, roll, offset=0):
        super(Dice, self).__init__()
        if roll == 1:
            self.surf = pygame.transform.scale_by(pygame.image.load("imgs/dice/one.png").convert(),.125)
        if roll == 2:
            self.surf = pygame.transform.scale_by(pygame.image.load("imgs/dice/two.png").convert(),.125)
        if roll == 3:
            self.surf = pygame.transform.scale_by(pygame.image.load("imgs/dice/three.png").convert(),.125)
        if roll == 4:
            self.surf = pygame.transform.scale_by(pygame.image.load("imgs/dice/four.png").convert(),.125)
        if roll == 5:
            self.surf = pygame.transform.scale_by(pygame.image.load("imgs/dice/five.png").convert(),.125)
        if roll == 6:
            self.surf = pygame.transform.scale_by(pygame.image.load("imgs/dice/six.png").convert(),.125)
        screen.blit(self.surf,(offset,0))

class Steal_From(pygame.sprite.Sprite):
    def __init__(self, board, screen, stealable):
        super(Steal_From, self).__init__()
        font = pygame.font.SysFont(None, 32)
        img = font.render("Who would you like to steal from?",True,"black")
        screen.blit(img,(110,500))
        offset = 0
        for people in stealable:
            label = Person_Label(screen,people,offset)
            board.steal_sprites.add(label)
            offset += 200

class Person_Label(pygame.sprite.Sprite):
    def __init__(self,screen,person,offset):
        super(Person_Label, self).__init__()
        self.person = person
        font = pygame.font.SysFont(None, 42)
        img = font.render(person.name,True,"black")
        screen.blit(img,(110+offset,600))
        self.rect = pygame.Rect(110+offset,600,175,25)

class Lumber_Trade(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, lumber_count):
        super(Lumber_Trade, self).__init__()
        self.name = "Lumber trade"
        font = pygame.font.SysFont(None, 30)
        self.surf = pygame.transform.scale_by(pygame.image.load("imgs/lumber.png").convert(),.05)
        screen.blit(self.surf,(x,y))
        img = font.render(str(lumber_count),True,"black")
        screen.blit(img,(x+50,y+10))
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width += 10

class Brick_Trade(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, brick_count):
        super(Brick_Trade, self).__init__()
        self.name = "Brick trade"
        font = pygame.font.SysFont(None, 30)
        self.surf = pygame.transform.scale_by(pygame.image.load("imgs/brick.png").convert(),.07)
        screen.blit(self.surf,(x,y-5))
        img = font.render(str(brick_count),True,"black")
        screen.blit(img,(x+50,y+10))
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width += 10

class Ore_Trade(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, ore_count):
        super(Ore_Trade, self).__init__()
        self.name = "Ore trade"
        font = pygame.font.SysFont(None, 30)
        self.surf = pygame.transform.scale_by(pygame.image.load("imgs/ore.png").convert(),.07)
        screen.blit(self.surf,(x-10,y))
        img = font.render(str(ore_count),True,"black")
        screen.blit(img,(x+50,y+15))
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width += 10

class Grain_Trade(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, grain_count):
        super(Grain_Trade, self).__init__()
        self.name = "Grain trade"
        font = pygame.font.SysFont(None, 30)
        self.surf = pygame.transform.scale_by(pygame.image.load("imgs/grain.png").convert(),.08)
        screen.blit(self.surf,(x-5,y-5))
        img = font.render(str(grain_count),True,"black")
        screen.blit(img,(x+50,y+15))
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width += 10

class Wool_Trade(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, wool_count):
        super(Wool_Trade, self).__init__()
        self.name = "Wool trade"
        font = pygame.font.SysFont(None, 30)
        self.surf = pygame.transform.scale_by(pygame.image.load("imgs/sheep.png").convert(),.15)
        screen.blit(self.surf,(x+10,y+10))
        img = font.render(str(wool_count),True,"black")
        screen.blit(img,(x+50,y+15))
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width += 10

class Trade_Label(pygame.sprite.Sprite):
    def __init__(self, screen, name, offset,selected=False):
        super(Trade_Label, self).__init__()
        self.name = name + " trade " +"label"
        x = 970
        y = 425
        font = pygame.font.SysFont(None, 30)
        if selected:
            img = font.render(name,True,"blue")
        else:
            img = font.render(name,True,"black")
        screen.blit(img,(x+offset,y))
        self.rect = pygame.Rect(x+offset,y,100,25)

class Lumber_RC(pygame.sprite.Sprite):
    def __init__(self, screen, lumber_count):
        super(Lumber_RC, self).__init__()
        self.name = "lumber"
        font = pygame.font.SysFont(None, 48)
        self.surf = pygame.transform.scale_by(pygame.image.load("imgs/lumber.png").convert(),.125)
        screen.blit(self.surf,(590,30))
        img = font.render(str(lumber_count),True,"black")
        screen.blit(img,(705,60))
        self.rect = self.surf.get_rect()
        self.rect.x = 600
        self.rect.y = 30
        self.rect.width += 50

class Brick_RC(pygame.sprite.Sprite):
    def __init__(self,screen,brick_count):
        super(Brick_RC, self).__init__()
        font = pygame.font.SysFont(None, 48)
        self.name = "brick"
        self.surf = pygame.transform.scale_by(pygame.image.load("imgs/brick.png").convert(),.125)
        self.rect = self.surf.get_rect()
        screen.blit(self.surf,(750,30))
        img = font.render(str(brick_count),True,"black")
        screen.blit(img,(840,60))
        self.rect = self.surf.get_rect()
        self.rect.x = 750
        self.rect.y = 30
        self.rect.width += 20

class Ore_RC(pygame.sprite.Sprite):
    def __init__(self,screen,ore_count):
        font = pygame.font.SysFont(None, 48)
        self.name = "ore"
        super(Ore_RC, self).__init__()
        self.surf = pygame.transform.scale_by(pygame.image.load("imgs/ore.png").convert(),.125)
        self.rect = self.surf.get_rect()
        screen.blit(self.surf,(875,30))
        img = font.render(str(ore_count),True,"black")
        screen.blit(img,(980,60))
        self.rect = self.surf.get_rect()
        self.rect.x = 875
        self.rect.y = 30
        self.rect.width += 20

class Grain_RC(pygame.sprite.Sprite):
    def __init__(self, screen, grain_count):
        super(Grain_RC, self).__init__()
        font = pygame.font.SysFont(None, 48)
        self.name = "grain"
        self.surf = pygame.transform.scale_by(pygame.image.load("imgs/grain.png").convert(),.15)
        self.rect = self.surf.get_rect()
        screen.blit(self.surf,(1000,15))
        img = font.render(str(grain_count),True,"black")
        screen.blit(img,(1100,60))
        self.rect = self.surf.get_rect()
        self.rect.x = 1000
        self.rect.y = 15
        self.rect.width += 20

class Wool_RC(pygame.sprite.Sprite):
    def __init__(self, screen, wool_count):
        super(Wool_RC, self).__init__()
        font = pygame.font.SysFont(None, 48)
        self.name = "wool"
        self.surf = pygame.transform.scale_by(pygame.image.load("imgs/sheep.png").convert(),.25)
        self.rect = self.surf.get_rect()
        screen.blit(self.surf,(1165,50))
        img = font.render(str(wool_count),True,"black")
        screen.blit(img,(1230,60))
        self.rect = self.surf.get_rect()
        self.rect.x = 1165
        self.rect.y = 50
        self.rect.width += 20

class Settlement_CB(pygame.sprite.Sprite):
    def __init__(self,screen,color):
        super(Settlement_CB,self).__init__()
        self.name = "settlement"
        x = 700
        y = 250
        pygame.draw.polygon(screen,color,[(x,y),(x,y-30),(x+20,y-50),(x+40,y-30),(x+40,y)])
        self.rect = pygame.draw.polygon(screen,"black",[(x,y),(x,y-30),(x+20,y-50),(x+40,y-30),(x+40,y)],5)

class Road_CB(pygame.sprite.Sprite):
    def __init__(self,screen,color):
        super(Road_CB,self).__init__()
        self.name = "road"
        first = (825,250)
        second = (875,200)
        b_first = (822,253)
        b_second = (878,197)
        self.rect = pygame.draw.line(screen,"Black",b_first,b_second,10)
        pygame.draw.line(screen,color,first,second,6)

class Development_CB(pygame.sprite.Sprite):
    def __init__(self,screen,afford):
        self.name = "development card"
        super(Development_CB,self).__init__()
        x= 1100
        y = 200
        w = 50
        h = 65
        if not afford:
            self.rect = pygame.draw.rect(screen,"black",[(x-3,y-3),(w+6,h+6)])
            pygame.draw.rect(screen,"gray15",[(x,y),(w,h)])
            return
        self.rect = pygame.draw.rect(screen,"black",[(x-3,y-3),(w+6,h+6)])
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

class Development_Card_Button(pygame.sprite.Sprite):
    def __init__(self,front_end,screen,name,offset):
        super(Development_Card_Button,self).__init__()
        self.name = name
        x= 700 + offset
        y= 310
        w= 75
        h= 75
        self.rect = pygame.draw.rect(screen,"aqua",[(x,y),(w,h)])

class End_Turn_Button(pygame.sprite.Sprite):
    def __init__(self,front_end,screen):
        super(End_Turn_Button,self).__init__()
        self.name = "end turn"
        x = 1100 
        y = 625
        w = 150
        h = 70
        self.rect = pygame.draw.rect(screen,"black",[(x,y),(w,h)])
        font = pygame.font.SysFont(None, 48)
        img = font.render("End Turn",True,"white")
        screen.blit(img,(x+5,y+18))
        front_end.turn_sprites.add(self)
