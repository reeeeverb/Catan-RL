import pygame
def pygame_start():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    screen.fill("aqua")
    #draw_board(200,175,[])
    pygame.display.flip()
    clock.tick(60)

def draw_tile(x,y,terrain):
    terrain_to_color = {"Mountains":"gray","Hills":"red","Forest":"darkgreen","Fields":"yellow","Pasture":"yellowgreen","Desert":"navajowhite"}
    color = terrain_to_color[terrain]
    pygame.draw.polygon(screen,color,[(x,y),(x-50,y-25),(x-50,y-75),(x,y-100),(x+50,y-75),(x+50,y-25)])

def draw_board(x,y,terrains):
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

