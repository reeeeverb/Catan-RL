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

    def draw_tile(self,x,y,terrain):
        screen = self.screen
        terrain_to_color = {"Mountains":"gray","Hills":"0xB22222","Forest":"0x023020","Fields":"0xcac407","Pasture":"0x5adc14","Desert":"navajowhite"}
        color = terrain_to_color[terrain]
        pygame.draw.polygon(screen,color,[(x,y),(x-50,y-25),(x-50,y-75),(x,y-100),(x+50,y-75),(x+50,y-25)])
        pygame.draw.polygon(screen,"black",[(x,y),(x-50,y-25),(x-50,y-75),(x,y-100),(x+50,y-75),(x+50,y-25)],4)
        pygame.display.flip()

    def draw_board(self,x,y,board):
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
        pygame.display.flip()

