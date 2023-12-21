import random
LEFT_EDGES = [0,7,16,27,38,47]
RIGHT_EDGES = [6,15,26,37,46,53]
LEGAL_PREGAME = [9,10,11,12,13,23,24,35,34,44,43,42,41,40,30,29,18,19]
class Board():
    def __init__(self, *args, **kwargs):
        self.terrains = (4*['Pasture']+4*['Forest']+4*['Fields']+3*['Hills']+3*['Mountains']+1*['Desert'])
        self.numbers = ([2]+2*[3]+2*[4]+2*[5]+2*[6]+2*[8]+2*[9]+2*[10]+2*[11]+[12]+[0])
        self.harbors = 4*["3"] + ["Brick"] + ["Lumber"] + ["Ore"] + ["Grain"] + ["Wool"]
        self.city_locations = 54*[None]
        self.road_locations = 72*[None]
        self.settlement_locations = 54*[None]
        self.clear_corners = 54*[True]
        self.road_corners = 54*[[] for i in range(54)]
    def generate_random_board(self):
        # 4*Pasture, 4*Forest, 4*Fields, 3*Hills, 3*Mountains, 1*Desert
        # 1*2, 2*3, 2*4, 2*5, 2*6, 2*8, 2*9, 2*10, 2*11, 1*12
        n = ([2]+2*[3]+2*[4]+2*[5]+2*[6]+2*[8]+2*[9]+2*[10]+2*[11]+[12])
        random.shuffle(self.terrains)
        random.shuffle(n)
        random.shuffle(self.harbors)
        n.insert(self.terrains.index("Desert"),0)
        self.numbers = n
    def legal_placement(self,loc,pregame=False):
        if pregame and loc not in LEGAL_PREGAME:
            return False
        if not self.sides_clear(loc):
            print("sides")
            return False
        if loc < 7 and (loc%2==1 or (loc%2==0 and self.clear_corners[loc+8])):
            return True
        if loc > 6 and loc < 16 and ((loc%2==1 and self.clear_corners[loc+10]) or (loc%2==0 and self.clear_corners[loc-8])):
            return True
        if loc > 15 and loc < 27 and ((loc%2==1 and self.clear_corners[loc-10]) or (loc%2==0 and self.clear_corners[loc+11])):
            return True
        if loc > 26 and loc < 38 and ((loc%2==1 and self.clear_corners[loc-11]) or (loc%2==0 and self.clear_corners[loc+10])):
            return True
        if loc > 37 and loc < 47 and ((loc%2==1 and self.clear_corners[loc+8]) or (loc%2==0 and self.clear_corners[loc-10])):
            return True
        if loc > 46 and loc < 54 and ((loc%2==1 and self.clear_corners[loc-8]) or loc%2==0):
            return True
        print("vertical")
        return False
    def sides_clear(self,loc):
        if loc not in LEFT_EDGES and not self.clear_corners[loc-1]:
            return False
        if loc not in RIGHT_EDGES and not self.clear_corners[loc+1]:
            return False
        return True
    def place_settlement(self,loc,player):
        if not self.legal_placement(loc):
            return False
        self.settlement_locations[loc] = player
        self.clear_corners[loc] = False
        self.road_corners[loc].append(player)
        return True
    def legal_road(self,loc,player,pregame=False):
        if self.road_locations[loc] != None:
            return False, None
        # deriving connected vertices
        if loc < 6:
            left_vertex = loc
            right_vertex = loc+1
        elif loc > 5 and loc < 10:
            left_vertex = (loc-6)*2
            right_vertex = left_vertex+8
        elif loc > 9 and loc < 18:
            left_vertex = loc - 3
            right_vertex = left_vertex + 1
        elif loc > 17 and loc < 23:
            left_vertex = ((loc-18)*2)+7
            right_vertex = left_vertex + 10
        elif loc > 22 and loc < 33:
            left_vertex = loc - 7
            right_vertex = left_vertex + 1
        elif loc > 32 and loc < 39:
            left_vertex = ((loc-33)*2)+16
            right_vertex = left_vertex + 11
        elif loc > 38 and loc < 49:
            left_vertex = loc - 12
            right_vertex = left_vertex + 1
        elif loc > 48 and loc < 54:
            left_vertex = ((loc-49)*2)+28
            right_vertex = left_vertex + 10
        elif loc > 53 and loc < 62:
            left_vertex = loc - 16
            right_vertex = left_vertex + 1
        elif loc > 61 and loc < 66:
            left_vertex = ((loc-62)*2)+39
            right_vertex = left_vertex + 8
        elif loc > 65 and loc < 72:
            left_vertex = loc - 19
            right_vertex = left_vertex + 1
        else:
            print("illegal road location")
            return False, None
        print(left_vertex,right_vertex)
        if (player in self.road_corners[left_vertex]) or (player in self.road_corners[right_vertex]):
            if pregame == False or (left_vertex == pregame or right_vertex == pregame):
                return True, left_vertex, right_vertex
        else:
            return False, left_vertex, right_vertex
    def place_road(self,loc,player,pregame=False):
        result = self.legal_road(loc,player,pregame)
        if result[0]:
            self.road_corners[result[1]].append(player)
            self.road_corners[result[2]].append(player)
            self.road_locations[loc] = player
            return True
        return False

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

class Development_Cards():
    def __init__(self, *args, **kwargs):
        self.reset_stack()
    def reset_stack(a = None):
        if a == None:
            a = self
        a.card_stack = 14*["Knight"]+5*["VP"]+2*["RB"]+2*["Monopoly"]
        a.used_stack = []
        a.shuffle()
    def shuffle(a = None):
        if a == None:
            a = self 
        random.shuffle(a.card_stack)
        print(a.card_stack)
    def draw_card(a = None):
        if a == None:
            a = self
        if len(a.card_stack) == 0:
            if len(a.used_stack) > 0:
                print("RESHUFFLING")
                a.card_stack = a.used_stack
                a.shuffle()
            else:
                return None
        return(a.card_stack.pop())
    def card_used(card):
        if card not in ["KNIGHT", "RB", "Monopoly"]:
            print("INVALID CARD")
        self.used_stack.append(card)

class Dice():
    def roll_one():
        return random.randint(1,6)
    def roll_two():
        return random.randint(1,6) + random.randint(1,6)












