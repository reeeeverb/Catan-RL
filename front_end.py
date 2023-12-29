import pygame
import sprites
class Front():
    def __init__(self,*args,**kwargs):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        running = True
        self.screen.fill("aqua")
        #draw_board(200,175,[])
        pygame.display.flip()
        self.clock.tick(60)
        self.settlements = 54*[None]
        self.roads = 72*[None]
        self.corners = []
        self.edges = []
        self.edges_coords=[]
        self.settlement_sprites = pygame.sprite.Group()
        self.settlement_bg_sprites = pygame.sprite.Group()
        self.turn_sprites = pygame.sprite.Group()

    def draw_tile(self,x,y,terrain):
        screen = self.screen
        terrain_to_color = {"Mountains":"gray","Hills":"0xB22222","Forest":"0x023020","Fields":"0xcac407","Pasture":"0x5adc14","Desert":"navajowhite"}
        color = terrain_to_color[terrain]
        pygame.draw.polygon(screen,color,[(x,y),(x-50,y-25),(x-50,y-75),(x,y-100),(x+50,y-75),(x+50,y-25)])
        pygame.draw.polygon(screen,"black",[(x,y),(x-50,y-25),(x-50,y-75),(x,y-100),(x+50,y-75),(x+50,y-25)],4)
        pygame.display.flip()

    def draw_board(self,x,y,board):
        board.pygame_coords = (x,y) 
        draw_tile = self.draw_tile
        terrains = board.terrains
        draw_tile(x,y,terrains[0])
        draw_tile(x+100,y,terrains[1])
        draw_tile(x+200,y,terrains[2])
        draw_tile(x-50,y+75,terrains[3])
        draw_tile(x+50,y+75,terrains[4])
        draw_tile(x+150,y+75,terrains[5])
        draw_tile(x+250,y+75,terrains[6])
        draw_tile(x-100,y+150,terrains[7])
        draw_tile(x,y+150,terrains[8])
        draw_tile(x+100,y+150,terrains[9])
        draw_tile(x+200,y+150,terrains[10])
        draw_tile(x+300,y+150,terrains[11])
        draw_tile(x-50,y+225,terrains[12])
        draw_tile(x+50,y+225,terrains[13])
        draw_tile(x+150,y+225,terrains[14])
        draw_tile(x+250,y+225,terrains[15])
        draw_tile(x,y+300,terrains[16])
        draw_tile(x+100,y+300,terrains[17])
        draw_tile(x+200,y+300,terrains[18])
        self.edges = self.board_edges(x,y)
        self.corners = self.board_corners(x,y)
        pygame.display.flip()
        return self.corners,self.edges

    def board_edges(self,x,y):
        tile_edges = self.tile_edges
        out = []
        out+=(tile_edges(x-50,y-75,3))
        out+=(tile_edges(x-50,y-75,3,vertical=True))
        out+=(tile_edges(x-100,y,4))
        out+=(tile_edges(x-100,y,4,vertical=True))
        out+=(tile_edges(x-150,y+75,5))
        out+=(tile_edges(x-150,y+75,5,vertical=True))
        out+=(tile_edges(x-150,y+125,5,inverted = True))
        out+=(tile_edges(x-100,y+150,4,vertical = True))
        out+=(tile_edges(x-100,y+200,4,inverted = True))
        out+=(tile_edges(x-50,y+225,3,vertical = True))
        out+=(tile_edges(x-50,y+275,3,inverted = True))
        return out
    def tile_edges(self,x,y,r,inverted = False, vertical=False):
        result = []
        sprites = []
        for i in range(r):
            if inverted:
                result.append(((x,y),(x+50,y+25)))
                result.append(((x+50,y+25),(x+100,y)))
            elif vertical:
                result.append(((x,y),(x,y+50)))
            else:  
                result.append(((x,y),(x+50,y-25)))
                result.append(((x+50,y-25),(x+100,y)))
            x +=100 
        if vertical:
            result.append(((x,y),(x,y+50)))
        for fir in result:
            s = pygame.draw.line(self.screen,"black",fir[0],fir[1],4)
            sprites.append(s)
        self.edges_coords += result
        return sprites


    def board_corners(self,x,y):
        out = []
        tile_corners = self.tile_corners
        out+=(tile_corners(x-50,y-75,3))
        out+=(tile_corners(x-100,y,4))
        out+=(tile_corners(x-150,y+75,5))
        out+=(tile_corners(x-150,y+125,5,True))
        out+=(tile_corners(x-100,y+200,4,True))
        out+=(tile_corners(x-50,y+275,3,True))
        return out

    def tile_corners(self,x,y,r,inverted=False):
        #150,100
        result = []
        sprites = []
        result.append((x,y))
        for i in range(r):
            if inverted:
                result.append((x+50,y+25))
                result.append((x+100,y))
            else:  
                result.append((x+50,y-25))
                result.append((x+100,y))
            x +=100 
        for c in result:
            s = pygame.draw.circle(self.screen,"red",(c[0],c[1]),5)
            sprites.append(s)
        return sprites
    def draw_settlement(self,index,player):
        rect = self.corners[index]
        x = rect.x-5
        y = rect.y+15
        color = player.color
        s = pygame.draw.polygon(self.screen,color,[(x,y),(x,y-15),(x+10,y-25),(x+20,y-15),(x+20,y)])
        s2 = pygame.draw.polygon(self.screen,"black",[(x,y),(x,y-15),(x+10,y-25),(x+20,y-15),(x+20,y)],3)
        self.settlements[index] = player
        pygame.display.flip()

    def draw_road(self,index,player):
        coords = self.edges_coords[index]
        color = player.color
        pygame.draw.line(self.screen,color,coords[0],coords[1],5)
        self.roads[index] = player
        pygame.display.flip()

    def refresh(self,board):
        for index in range(len(board.road_locations)):
            if board.road_locations[index] != None:
                self.draw_road(index,board.road_locations[index])
        for index in range(len(board.settlement_locations)):
            if board.settlement_locations[index] != None:
                self.draw_settlement(index,board.settlement_locations[index])
        pygame.display.flip()

    def draw_player_turn(self,board,player):
        font = pygame.font.SysFont(None, 48)

        lumber = sprites.Lumber_RC()
        self.screen.blit(lumber.surf,(600,30))
        img = font.render(str(player.resource_cards["Lumber"]),True,"black")
        self.screen.blit(img,(720,60))

        brick = sprites.Brick_RC()
        self.screen.blit(brick.surf,(750,30))
        img = font.render(str(player.resource_cards["Brick"]),True,"black")
        self.screen.blit(img,(840,60))

        ore = sprites.Ore_RC()
        self.screen.blit(ore.surf,(875,30))
        img = font.render(str(player.resource_cards["Ore"]),True,"black")
        self.screen.blit(img,(980,60))

        grain = sprites.Grain_RC()
        self.screen.blit(grain.surf,(1000,15))
        img = font.render(str(player.resource_cards["Grain"]),True,"black")
        self.screen.blit(img,(1100,60))

        wool = sprites.Wool_RC()
        self.screen.blit(wool.surf,(1165,50))
        img = font.render(str(player.resource_cards["Wool"]),True,"black")
        self.screen.blit(img,(1230,60))

        img = font.render("Crafting",True,"Black")
        self.screen.blit(img,(870,150))

        sett_color = "grey15"
        if board.bank.can_afford("Settlement",player)[0]:
            sett_color = player.color
        settlement = sprites.Settlement_CB(self.screen,sett_color)

        road_color = "grey15"
        if board.bank.can_afford("Road",player)[0]:
            road_color = player.color
        road = sprites.Road_CB(self.screen,road_color)

        dev_afford = board.bank.can_afford("Development_Card",player)[0]
        development_card = sprites.Development_CB(self.screen,dev_afford)

        end_turn_b = sprites.End_Turn_Button(self.screen)

        self.turn_sprites.add(end_turn_b)

        pygame.display.flip()

        return self.turn_sprites






