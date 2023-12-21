#!/usr/bin/python3
import pdb
import random
import board
import player
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

        self.pregame_setup()
    def pregame_setup(self):
        player_arr = [self.player1,self.player2,self.player3]
        names = input("Who is playing today?(3):\n").split()
        if len(names) == 3:
            self.player1.set_name(names[0])
            self.player2.set_name(names[1])
            self.player3.set_name(names[2])
        random.shuffle(player_arr)
        for player in (player_arr + list(reversed(player_arr))):
            done = False
            while not done:
                val = input(player.name + ", where would you like to place your settlement?\n")
                try:
                    val = int(val)
                    if player.place_settlement(self.game_board,val,True):
                        done = True
                    else:
                        print("Invalid settlement location entered.\n")
                except ValueError:
                    print("Nonvalid int entered.\n")
                val = input(player.name + ", where would you like to place your road?\n")
                try:
                    val = int(val)
                    if player.place_road(self.game_board,val,True):
                        done = True
                    else:
                        print("Invalid road location entered.\n")
                except ValueError:
                    print("Nonvalid int entered.\n")

def main():
    game = Game()
    breakpoint()
if __name__=="__main__":
    main()
