import pygame
import sprites
GLOBAL_X = 200
GLOBAL_Y = 175
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
        self.tile_sprites = pygame.sprite.Group()
        self.turn_sprites = pygame.sprite.Group()
        self.steal_sprites = pygame.sprite.Group()
        self.last_roll = (0,0)
        self.selected_trade = None

    def draw_tile(self,x,y,terrain,index,n):
        screen = self.screen
        tile = sprites.Terrain_Tile(screen,terrain,x,y,index,n)
        self.tile_sprites.add(tile)

    def draw_board(self,x,y,board):
        board.pygame_coords = (x,y) 
        draw_tile = self.draw_tile
        terrains = board.terrains
        n = board.numbers
        draw_tile(x,y,terrains[0],0,n[0])
        draw_tile(x+100,y,terrains[1],1,n[1])
        draw_tile(x+200,y,terrains[2],2,n[2])
        draw_tile(x-50,y+75,terrains[3],3,n[3])
        draw_tile(x+50,y+75,terrains[4],4,n[4])
        draw_tile(x+150,y+75,terrains[5],5,n[5])
        draw_tile(x+250,y+75,terrains[6],6,n[6])
        draw_tile(x-100,y+150,terrains[7],7,n[7])
        draw_tile(x,y+150,terrains[8],8,n[8])
        draw_tile(x+100,y+150,terrains[9],9,n[9])
        draw_tile(x+200,y+150,terrains[10],10,n[10])
        draw_tile(x+300,y+150,terrains[11],11,n[11])
        draw_tile(x-50,y+225,terrains[12],12,n[12])
        draw_tile(x+50,y+225,terrains[13],13,n[13])
        draw_tile(x+150,y+225,terrains[14],14,n[14])
        draw_tile(x+250,y+225,terrains[15],15,n[15])
        draw_tile(x,y+300,terrains[16],16,n[16])
        draw_tile(x+100,y+300,terrains[17],17,n[17])
        draw_tile(x+200,y+300,terrains[18],18,n[18])
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
            s = pygame.draw.circle(self.screen,"black",(c[0],c[1]),5)
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

    def show_legal_settlement_loc(self,board,player):
        for index in range(len(board.corner_placeable)):
            if board.corner_placeable[index] == True:
                old_rect = self.corners[index]
                c = old_rect.center
                new_rect = pygame.draw.circle(self.screen,player.color,(c[0],c[1]),8)
                self.corners[index] = new_rect
        pygame.display.flip() 

    def refresh(self,board,player_arr = None, player=None):
        pygame.draw.rect(self.screen,"aqua",[(0,0),(600,720)])
        self.draw_board(GLOBAL_X,GLOBAL_Y,board)
        for index in range(len(board.road_locations)):
            if board.road_locations[index] != None:
                self.draw_road(index,board.road_locations[index])
        for index in range(len(board.settlement_locations)):
            if board.settlement_locations[index] != None:
                self.draw_settlement(index,board.settlement_locations[index])
        if player != None:
            self.clear_turn()
            self.draw_player_turn(board,player_arr,player)
        pygame.display.flip()

    def steal_from(self,stealable):
        steal_from = sprites.Steal_From(self,self.screen,stealable)
        pygame.display.flip()

    def cover_steal(self):
        self.steal_sprites.empty()
        pygame.draw.rect(self.screen,"aqua",[(0,500),(600,200)])

    def clear_turn(self):
        self.turn_sprites.empty()
        pygame.draw.rect(self.screen,"aqua",[(600,0),(700,720)])

    def draw_dice(self,roll):
        self.last_roll = roll
        dice = sprites.Dice(self,self.screen,roll[0])
        dice = sprites.Dice(self,self.screen,roll[1],75)
        pygame.display.flip()

    def update_development_cards_display(self,board,player):
        pygame.draw.rect(self.screen,"aqua",[(700,270),(600,120)])

        knight = sprites.Development_Card_Button(self,self.screen,"Knight",0)
        self.turn_sprites.add(knight)

        rb = sprites.Development_Card_Button(self,self.screen,"RB",135)
        self.turn_sprites.add(rb)

        mono = sprites.Development_Card_Button(self,self.screen,"Monopoly",280)
        self.turn_sprites.add(mono)

        yop = sprites.Development_Card_Button(self,self.screen,"YOP",430)
        self.turn_sprites.add(yop)

        font = pygame.font.SysFont(None, 48)
        img = font.render("Development Cards",True,"Black")
        self.screen.blit(img,(780,270))

        font2 = pygame.font.SysFont(None, 30)

        img = font2.render("Knight",True,"Blue")
        self.screen.blit(img,(700,310))

        img = font.render(str(player.development_cards["Knight"]),True,"Blue")
        self.screen.blit(img,(720,330))

        img = font2.render("Road Building",True,"Blue")
        self.screen.blit(img,(800,310))

        img = font.render(str(player.development_cards["RB"]),True,"Blue")
        self.screen.blit(img,(860,330))

        img = font2.render("Monopoly",True,"Blue")
        self.screen.blit(img,(975,310))

        img = font.render(str(player.development_cards["Monopoly"]),True,"Blue")
        self.screen.blit(img,(1015,330))

        img = font2.render("Year of Plenty",True,"Blue")
        self.screen.blit(img,(1100,310))

        img = font.render(str(player.development_cards["YOP"]),True,"Blue")
        self.screen.blit(img,(1150,330))

        pygame.display.flip()

    def trade_label_change(self,player_arr,player,new):
        pygame.draw.rect(self.screen,"aqua",[(970,425),(300,25)])
        for sprite in self.turn_sprites:
            if len(sprite.name.split()) > 2 and "label" == sprite.name.split()[2]:
                self.turn_sprites.remove(sprite)
        offset = 0
        person_name = ""
        if new != None:
            person_name = (new.name.split()[0])
        for temp in player_arr:
            if temp != player:
                selected = (person_name == temp.name)
                label = sprites.Trade_Label(self.screen,temp.name,offset,selected)
                self.turn_sprites.add(label)
                offset +=100
        selected = person_name == "Bank"
        label = sprites.Trade_Label(self.screen,"Bank",offset,selected)
        self.turn_sprites.add(label)
        self.selected_trade = new
        pygame.display.flip()
    def draw_trade(self,board,player_arr,player,selection=False):

        pygame.draw.rect(self.screen,"aqua",[(650,450),(650,150)])
        for sprite in self.turn_sprites:
            if len(sprite.name.split()) > 1 and "trade" == sprite.name.split()[1]:
                self.turn_sprites.remove(sprite)

        temp_sprites = pygame.sprite.Group()
        sprite_list = []

        font = pygame.font.SysFont(None, 48)
        img = font.render("Trading",True,"Black")
        self.screen.blit(img,(870,375))

        lumber = sprites.Lumber_Trade(self.screen,705,450,player.trade_resources["Lumber"])
        sprite_list.append(lumber)
        
        brick = sprites.Brick_Trade(self.screen,795,450,player.trade_resources["Brick"])
        sprite_list.append(brick)

        ore = sprites.Ore_Trade(self.screen,650,490,player.trade_resources["Ore"])
        sprite_list.append(ore)

        grain = sprites.Grain_Trade(self.screen,740,490,player.trade_resources["Grain"])
        sprite_list.append(grain)

        wool = sprites.Wool_Trade(self.screen,830,490,player.trade_resources["Wool"])
        sprite_list.append(wool)

        if not selection:
            self.trade_label_change(player_arr,player,self.selected_trade)

            lumber = sprites.Lumber_Trade(self.screen,1005,450,player.trade_take_resources["Lumber"])
            sprite_list.append(lumber)
            
            brick = sprites.Brick_Trade(self.screen,1095,450,player.trade_take_resources["Brick"])
            sprite_list.append(brick)

            ore = sprites.Ore_Trade(self.screen,950,490,player.trade_take_resources["Ore"])
            sprite_list.append(ore)

            grain = sprites.Grain_Trade(self.screen,1040,490,player.trade_take_resources["Grain"])
            sprite_list.append(grain)

            wool = sprites.Wool_Trade(self.screen,1130,490,player.trade_take_resources["Wool"])
            sprite_list.append(wool)

            submit = sprites.Submit_Trade_Button(self.screen)
            sprite_list.append(submit)

        pygame.display.flip()


        if not selection:
            for sprite in sprite_list:
                self.turn_sprites.add(sprite)
        else:
            for sprite in sprite_list:
                temp_sprites.add(sprite)
            return temp_sprites

        return

    def draw_player_turn(self,board,player_arr,player):
        font = pygame.font.SysFont(None, 48)

        lumber = sprites.Lumber_RC(self.screen,player.resource_cards["Lumber"])
        self.turn_sprites.add(lumber)

        brick = sprites.Brick_RC(self.screen, player.resource_cards["Brick"])
        self.turn_sprites.add(brick)

        ore = sprites.Ore_RC(self.screen, player.resource_cards["Ore"])
        self.turn_sprites.add(ore)

        grain = sprites.Grain_RC(self.screen, player.resource_cards["Grain"])
        self.turn_sprites.add(grain)

        wool = sprites.Wool_RC(self.screen, player.resource_cards["Wool"])
        self.turn_sprites.add(wool)

        img = font.render("Crafting",True,"Black")
        self.screen.blit(img,(870,150))

        sett_color = "grey15"
        if board.bank.can_afford("Settlement",player)[0]:
            sett_color = player.color
        settlement = sprites.Settlement_CB(self.screen,sett_color)
        self.turn_sprites.add(settlement)

        road_color = "grey15"
        if board.bank.can_afford("Road",player)[0]:
            road_color = player.color
        road = sprites.Road_CB(self.screen,road_color)
        self.turn_sprites.add(road)

        dev_afford = board.bank.can_afford("Development_Card",player)[0]
        development_card = sprites.Development_CB(self.screen,dev_afford)
        self.turn_sprites.add(development_card)

        end_turn_b = sprites.End_Turn_Button(self,self.screen)

        self.update_development_cards_display(board,player)

        self.draw_trade(board,player_arr,player)

        return self.turn_sprites






