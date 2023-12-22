#!/usr/bin/python3
import pdb
import random
import board
import player
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

        self.pregame_setup()
        self.take_turn()
    def pregame_setup(self):
        names = input("Who is playing today?(3):\n").split()
        if len(names) == 3:
            self.player1.set_name(names[0])
            self.player2.set_name(names[1])
            self.player3.set_name(names[2])
        random.shuffle(self.player_arr)
        for player in (self.player_arr + list(reversed(self.player_arr))):
            done = False
            while not done:
                val = input(player.name + ", where would you like to place your settlement?\n")
                try:
                    val = int(val)
                    if player.place_settlement(self.game_board,val,True):
                        done = True
                        sett = val
                    else:
                        print("Invalid settlement location entered.\n")
                except ValueError:
                    print("Nonvalid int entered.\n")
            done1 = False
            while not done1:
                val = input(player.name + ", where would you like to place your road?\n")
                try:
                    val = int(val)
                    if player.place_road(self.game_board,val,sett):
                        done1 = True
                    else:
                        print("Invalid road location entered.\n")
                except ValueError:
                    print("Nonvalid int entered.\n")
    def take_turn(self):
        for player in self.player_arr:
            roll_result = self.dice.roll_two()
            print("A {} was rolled!".format(roll_result))
            self.game_board.bank.dice_rolled(self.game_board.turn_tree[roll_result])


def main():
    game = Game()
if __name__=="__main__":
    main()
