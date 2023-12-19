#!/usr/bin/python3
import pdb
import random
import board
class Game():
    def __init__(self,*args,**kwargs):
        self.game_board = board.Board()
        self.game_board.generate_random_board()
        self.game_board.pp()
        self.game_deck = board.Development_Cards()
        self.turn_tree = 12*[[]]

def main():
    main_board = board.Board() 
    main_board.generate_random_board()
    main_board.pp()
    deck = board.Development_Cards()
    deck.shuffle()
    print(deck.draw_card())
    game = Game()
    breakpoint()

if __name__=="__main__":
    main()
