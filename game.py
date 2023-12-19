import random
import board
def main():
    main_board = board.Board() 
    main_board.generate_random_board()
    main_board.pp()

if __name__=="__main__":
    main()
