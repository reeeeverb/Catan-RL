#!/usr/bin/python3
import pdb
import random
import board,player
class Game():
    def __init__(self,*args,**kwargs):
        self.game_board = board.Board()
        self.game_board.generate_random_board()
        self.game_board.pp()
        self.game_deck = board.Development_Cards()
        self.turn_tree = 12*[[]]
        self.pregame_setup()

    def pregame_setup(self):
        self.player1 = player.Player()
        self.player2 = player.Player()
        self.player3 = player.Player()
        player_arr = [self.player1,self.player2,self.player3]
        random.shuffle(player_arr)

def main():
    game = Game()
    breakpoint()

if __name__=="__main__":
    main()
