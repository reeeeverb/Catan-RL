import random
class Board():
    terrains = (4*['Pasture']+4*['Forest']+4*['Fields']+3*['Hills']+3*['Mountains']+1*['Desert'])
    numbers = ([2]+2*[3]+2*[4]+2*[5]+2*[6]+2*[8]+2*[9]+2*[10]+2*[11]+[12]+[0])
    harbors = 4*["3"] + ["Brick"] + ["Lumber"] + ["Ore"] + ["Grain"] + ["Wool"]
    def generate_random_board(self):
        # 4*Pasture, 4*Forest, 4*Fields, 3*Hills, 3*Mountains, 1*Desert
        # 1*2, 2*3, 2*4, 2*5, 2*6, 2*8, 2*9, 2*10, 2*11, 1*12
        n = ([2]+2*[3]+2*[4]+2*[5]+2*[6]+2*[8]+2*[9]+2*[10]+2*[11]+[12])
        random.shuffle(self.terrains)
        random.shuffle(n)
        random.shuffle(self.harbors)
        n.insert(self.terrains.index("Desert"),0)
        self.numbers = n
    def pp(self):
        temp_b = 19 * [""]
        for c in range(len(self.terrains)):
            temp_b[c] = "{0}[{1}]".format(self.terrains[c],str(self.numbers[c]))
        board = list(map("{:^10}".format,temp_b))
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

