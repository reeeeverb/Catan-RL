#!/usr/bin/python3
import time
import pygame
import pdb
import random
import board
import player
import front_end
import builtins
from unittest.mock import patch
DEBUG_SKIP_PG = True
class Game():
    def __init__(self,*args,**kwargs):
        self.game_board = board.Board()
        self.game_board.generate_random_board()
        self.game_board.pp()
        self.game_deck = board.Development_Cards()
        self.turn_tree = 12*[[]]
        self.player1 = player.Player()
        self.player2 = player.Player()
        self.player3 = player.Player()
        self.player_arr = [self.player1,self.player2,self.player3]
        self.dice = board.Dice()
        self.front_end = front_end.Front()
        self.pregame_setup()
        self.board_corners = []
        self.board_edges = []
        self.take_turn()
        self.longest_road = (4,None)
        self.largest_army = (2,None)
    def pregame_setup(self):
        self.board_corners,self.board_edges = self.front_end.draw_board(200,175,self.game_board)
        corners = self.board_corners
        edges = self.board_edges
        #names = input("Who is playing today?(3):\n").split()
        names = ["Skyhlar","David","Daphne"]
        if len(names) == 3:
            self.player1.set_info(names[0],"indigo",True)
            self.player2.set_info(names[1],"fuchsia",False)
            self.player3.set_info(names[2],"orangered",False)
        random.shuffle(self.player_arr)
        if DEBUG_SKIP_PG:
            self.player1.place_settlement(self.game_board,9,True)
            self.player2.place_settlement(self.game_board,30,True)
            self.player3.place_settlement(self.game_board,41,True)
            self.player1.place_settlement(self.game_board,12,True)
            self.player2.place_settlement(self.game_board,23,True)
            self.player3.place_settlement(self.game_board,35,True)
            self.front_end.refresh(self.game_board)
            return
        for player in (self.player_arr + list(reversed(self.player_arr))):
            #val = input(player.name + ", where would you like to place your settlement?\n")
            invalid_loc = True
            while invalid_loc:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        clicked = [s for s in corners if s.collidepoint(pos)]
                        if clicked !=[] and player.place_settlement(self.game_board,corners.index(clicked[0]),True):
                            invalid_loc = False
                            sett = corners.index(clicked[0])
                        else:
                            print("Invalid Location")
                    if event.type == pygame.QUIT:
                        running = False
            self.front_end.refresh(self.game_board)
            invalid_loc = True
            while invalid_loc:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        c_clicked = [s for s in edges if s.collidepoint(pos)]
                        if c_clicked !=[] and player.place_road(self.game_board,edges.index(c_clicked[0]),sett):
                            invalid_loc = False
                        else:
                            print("Invalid Location")
                    if event.type == pygame.QUIT:
                        running = False
            self.front_end.refresh(self.game_board)
    def move_robber(self,board,player,knight_card=False):        
        if not knight_card:
            for other_player in self.player_arr:
                if sum(other_player.resource_cards.values()) > 7:
                    other_player.discard_half()
        not_done = True
        while not_done:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    clicked = [s for s in self.front_end.tile_sprites if s.rect.collidepoint(pos)]
                    if clicked !=[]:
                        index = clicked[0].index
                        board.robber_tile = index
                        not_done = False 
                    else:
                        print("No")
                if event.type == pygame.QUIT:
                    not_done = False
        stealable = []
        for number in self.game_board.turn_tree:
            for tile in number:
                if tile[2] == index and tile[1] not in stealable and tile[1] != player:
                    stealable.append(tile[1])
        self.front_end.steal_from(stealable)
        not_done = True
        while not_done:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    clicked = [s for s in self.front_end.steal_sprites if s.rect.collidepoint(pos)]
                    if clicked !=[]:
                        take_person = clicked[0].person
                        print(take_person.name)
                        self.game_board.bank.steal_random(player,take_person)
                        not_done = False 
                    else:
                        print("No")
                if event.type == pygame.QUIT:
                    not_done = False
        self.front_end.cover_steal()
        return

    def craft_settlement_clicked(self,player,board):
        self.front_end.show_legal_settlement_loc(board,player)
        not_done = True
        while not_done:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    clicked = [s for s in self.front_end.corners if s.collidepoint(pos)]
                    print(clicked)
                    if clicked !=[]:
                        index = self.front_end.corners.index(clicked[0])
                        if board.legal_placement(index,player):
                            if player.place_settlement(board,int(index)):
                                print("hit")
                                self.front_end.refresh(board,self.player_arr,player)
                                return True
                    else:
                        self.front_end.refresh(board,self.player_arr,player)
                        return False
                if event.type == pygame.QUIT:
                    running = False
        return
    def craft_road_clicked(self,player,board):
        not_done = True
        while not_done:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    clicked = [s for s in self.front_end.edges if s.collidepoint(pos)]
                    print(clicked)
                    if clicked !=[]:
                        index = self.front_end.edges.index(clicked[0])
                        if board.legal_placement(index,player):
                            if player.place_road(board,int(index)):
                                self.front_end.refresh(board,self.player_arr,player)
                                return True
                    else:
                        self.front_end.refresh(board,self.player_arr,player)
                        return False
                if event.type == pygame.QUIT:
                    running = False
        return
    def craft_card_clicked(self,player,board):
        card = self.game_deck.draw_card() 
        player.development_cards[card] +=1
        self.game_board.bank.craft("Development_Card",player)
        print(player.development_cards)
        self.front_end.update_development_cards_display(board,player)
        self.front_end.refresh(board,self.player_arr,player)
    def play_knight(self,board,player):
        move_robber(board,player,True)
        player.played_knights += 1
        if player.played_knights > self.largest_army[0]:
            if self.largest_army[1] != None:
                self.largest_army[1].remove_largest_army()
            self.largest_army[1] = player
            self.largest_army[0] = player.played_knights
            player.give_largest_army()
        return
    def play_monopoly(self,board,player):
        player.development_cards["Monopoly"] -= 1
        player.craft_count["Development_Card"] -= 1
        self.game_deck.card_used("Monopoly")
        select_sprites = self.front_end.draw_trade(board,player,True)
        not_done = True
        while not_done:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    clicked = [s for s in select_sprites if s.rect.collidepoint(pos)]
                    print(clicked)
                    if clicked !=[]:
                        print("MONOPOLY:" + clicked[0].name)
                        board.bank.monopolize(self.player_arr,player,clicked[0].name.split()[0])
                        not_done = False
                if event.type == pygame.QUIT:
                    running = False
        self.front_end.refresh(board,self.player_arr,player)
    def play_rb(self,board,player):
        return
    def play_yop(self,board,player):
        player.development_cards["YOP"] -= 1
        player.craft_count["Development_Card"] -= 1
        self.game_deck.card_used("YOP")
        select_sprites = self.front_end.draw_trade(board,player,True)
        count = 0
        not_done = True
        while not_done:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    clicked = [s for s in select_sprites if s.rect.collidepoint(pos)]
                    if clicked !=[]:
                        print("YOP:" + clicked[0].name)
                        if board.bank.give_resource(clicked[0].name.split()[0],player):
                            count += 1
                            self.front_end.refresh(board,self.player_arr,player)
                        if count == 2:
                            not_done = False
                if event.type == pygame.QUIT:
                    running = False
        return
    def take_turn(self):
        game_over = False
        while not game_over:
            for player in self.player_arr:
                dice_one, dice_two = self.dice.roll_two()
                roll_result = dice_one+dice_two
                print("A {} was rolled!".format(roll_result))
                self.front_end.draw_dice((dice_one,dice_two))
                self.game_board.bank.dice_rolled(self.game_board,self.game_board.turn_tree[roll_result])
                if player.human:
                    if roll_result == 7:
                        self.move_robber(self.game_board,player)
                    turn_ended = False
                    sprites = self.front_end.draw_player_turn(self.game_board,self.player_arr,player)
                    while not turn_ended:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                pos = pygame.mouse.get_pos()
                                clicked = [s for s in sprites if s.rect.collidepoint(pos)]
                                print(clicked)
                                if clicked !=[] and clicked[0].name == "end turn":
                                    turn_ended = True
                                elif clicked !=[] and clicked[0].name == "settlement" and self.game_board.bank.can_afford("Settlement",player)[0]:
                                    self.craft_settlement_clicked(player, self.game_board)
                                elif clicked !=[] and clicked[0].name == "road" and self.game_board.bank.can_afford("Road",player)[0]:
                                    self.craft_road_clicked(player, self.game_board)
                                elif clicked !=[] and clicked[0].name == "development card" and self.game_board.bank.can_afford("Development_Card",player)[0]:
                                    self.craft_card_clicked(player, self.game_board)
                                elif clicked !=[] and clicked[0].name == "Knight" and player.development_cards["Knight"] > 0:
                                    self.play_knight(self.game_board,player)
                                elif clicked !=[] and clicked[0].name == "RB" and player.development_cards["RB"] > 0:
                                    self.play_rb(self.game_board,player)
                                elif clicked !=[] and clicked[0].name == "Monopoly" and player.development_cards["Monopoly"] > 0:
                                    self.play_monopoly(self.game_board,player)
                                elif clicked !=[] and clicked[0].name == "YOP" and player.development_cards["YOP"]:
                                    self.play_yop(self.game_board,player)
                                elif clicked != [] and event.button == 3:
                                    player.trade_resources = {"Brick":0, "Lumber":0, "Ore":0, "Grain":0, "Wool":0}
                                    player.trade_take_resources = {"Brick":0, "Lumber":0, "Ore":0, "Grain":0, "Wool":0}
                                    self.front_end.draw_trade(board,self.player_arr,player)
                                elif clicked !=[] and clicked[0].name == "Lumber trade":
                                    if clicked[0].rect.x < 950 and player.resource_cards["Lumber"]> player.trade_resources["Lumber"]:
                                        player.trade_resources["Lumber"] += 1
                                    else:
                                        player.trade_take_resources["Lumber"] += 1
                                    self.front_end.draw_trade(board,self.player_arr,player)
                                elif clicked !=[] and clicked[0].name == "Brick trade":
                                    if clicked[0].rect.x < 950 and player.resource_cards["Brick"]> player.trade_resources["Brick"]:
                                        player.trade_resources["Brick"] += 1
                                    else:
                                        player.trade_take_resources["Brick"] += 1
                                    self.front_end.draw_trade(board,self.player_arr,player)
                                elif clicked !=[] and clicked[0].name == "Ore trade":
                                    if clicked[0].rect.x < 950 and player.resource_cards["Ore"]> player.trade_resources["Ore"]:
                                        player.trade_resources["Ore"] += 1
                                    else:
                                        player.trade_take_resources["Ore"] +=1
                                    self.front_end.draw_trade(board,self.player_arr,player)
                                elif clicked !=[] and clicked[0].name == "Grain trade":
                                    if clicked[0].rect.x < 950 and player.resource_cards["Grain"]> player.trade_resources["Grain"]:
                                        player.trade_resources["Grain"] += 1
                                    else:
                                        player.trade_take_resources["Grain"] += 1
                                    self.front_end.draw_trade(board,self.player_arr,player)
                                elif clicked !=[] and clicked[0].name == "Wool trade":
                                    if clicked[0].rect.x < 950 and player.resource_cards["Wool"]> player.trade_resources["Wool"]:
                                        player.trade_resources["Wool"] += 1
                                    else:
                                        player.trade_take_resources["Wool"] +=1
                                    self.front_end.draw_trade(board,self.player_arr,player)
                                elif clicked !=[] and len(clicked[0].name.split()) == 3 and clicked[0].name.split()[2] == "label":
                                    print("hit")
                                    self.front_end.trade_label_change(self.player_arr,player,clicked[0])
                                else:
                                    print("Invalid Location")
                            if event.type == pygame.QUIT:
                                running = False
                    self.front_end.clear_turn()

def main():
    game = Game()
if __name__=="__main__":
    main()
