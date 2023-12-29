import pygame
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
        pygame.draw.polygon(self.screen,color,[(x,y),(x,y-15),(x+10,y-25),(x+20,y-15),(x+20,y)])
        pygame.draw.polygon(self.screen,"black",[(x,y),(x,y-15),(x+10,y-25),(x+20,y-15),(x+20,y)],3)
        self.settlements[index] = player
        pygame.display.flip()

    def draw_road(self,index,player):
        coords = self.edges_coords[index]
        color = player.color
        pygame.draw.line(self.screen,color,coords[0],coords[1],5)
        self.roads[index] = player
        pygame.display.flip()

    def refresh(self,board):
        for index in range(len(board.settlement_locations)):
            if board.settlement_locations[index] != self.settlements[index]:
                player = board.settlement_locations[index]
                self.draw_settlement(index,player)
        for index in range(len(board.road_locations)):
            if board.road_locations[index] != self.roads[index]:
                player = board.road_locations[index]
                self.draw_road(index,player)



