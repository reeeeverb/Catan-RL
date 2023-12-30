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
                                self.front_end.refresh(board)
                                return True
                    else:
                        print("Invalid Location")
                        return False
                if event.type == pygame.QUIT:
                    running = False
        return
    def take_turn(self):
        game_over = False
        while not game_over:
            for player in self.player_arr:
                roll_result = self.dice.roll_two()
                print("A {} was rolled!".format(roll_result))
                self.game_board.bank.dice_rolled(self.game_board.turn_tree[roll_result])
                if player.human:
                    turn_ended = False
                    sprites = self.front_end.draw_player_turn(self.game_board,player)
                    while not turn_ended:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                pos = pygame.mouse.get_pos()
                                clicked = [s for s in sprites if s.rect.collidepoint(pos)]
                                print(clicked)
                                if clicked !=[] and clicked[0].name == "end turn":
                                    turn_ended = True
                                elif clicked !=[] and clicked[0].name == "settlement":
                                    self.craft_settlement_clicked(player, self.game_board)
                                else:
                                    print("Invalid Location")
                            if event.type == pygame.QUIT:
                                running = False
                    self.front_end.clear_turn()
                    
                if player.victory_points >= 10:
                    game_over = True

def main():
    game = Game()
if __name__=="__main__":
    main()
