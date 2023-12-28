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
        self.take_turn()
        self.board_corners = []
        self.board_edges = []
    def pregame_setup(self):
        self.board_corners,self.board_edges = self.front_end.draw_board(200,175,self.game_board)
        corners = self.board_corners
        edges = self.board_edges
        #names = input("Who is playing today?(3):\n").split()
        names = ["Skyhlar","David","Daphne"]
        if len(names) == 3:
            self.player1.set_name(names[0])
            self.player2.set_name(names[1])
            self.player3.set_name(names[2])
        random.shuffle(self.player_arr)
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
    def take_turn(self):
        for player in self.player_arr:
            roll_result = self.dice.roll_two()
            print("A {} was rolled!".format(roll_result))
            self.game_board.bank.dice_rolled(self.game_board.turn_tree[roll_result])


def main():
    game = Game()
if __name__=="__main__":
    main()
