import random

def main():
    board = generate_board()
    pp_board(board)

def generate_board():
    # 4*Pasture, 4*Forest, 4*Fields, 3*Hills, 3*Mountains, 1*Desert
    board = (4*['Pasture']+4*['Forest']+4*['Fields']+3*['Hills']+3*['Mountains']+1*['Desert'])
    random.shuffle(board)
    return board

def pp_board(board):
    board = list(map("{:^10}".format,board))
    gap = " "*10
    hgap = " "*5
    print(gap,board[0],board[1],board[2])
    print()
    print(hgap,board[3],board[4],board[5],board[6])
    print()
    print(board[7],board[8],board[9],board[10],board[11])
    print()
    print(hgap,board[12],board[13],board[14],board[15])
    print()
    print(gap,board[16],board[17],board[18])

if __name__=="__main__":
    main()
