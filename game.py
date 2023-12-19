#!/usr/bin/python3
import pdb
import random
import board
def main():
    main_board = board.Board() 
    main_board.generate_random_board()
    main_board.pp()
    deck = board.Development_Cards()
    deck.shuffle()
    print(deck.draw_card())
    breakpoint()

if __name__=="__main__":
    main()

class Game():
    def __init(self,*args,**kwargs):
        game_board = board.Board()
        game_board.generate_random_board()
        game_board.pp()
        game_deck = board.Development_Cards()
        generate_turn_tree()
        self.turn_tree = []
    def generate_turn_tree():
        for c in range(len(game_board.terrain)):
            self.turn_tree[game_board.numbers[c]].append(c,game_board.terrain[c])

