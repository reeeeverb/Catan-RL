import random
LEFT_EDGES = [0,7,16,27,38,47]
RIGHT_EDGES = [6,15,26,37,46,53]
LEGAL_PREGAME = [9,10,11,12,13,23,24,35,34,44,43,42,41,40,30,29,18,19]
HARBOR_LOCATIONS = [0,1,3,4,14,15,26,37,45,46,50,51,47,48,28,38,17,7]
VERTEX_CONTACTS = [[0], [0], [0,1], [1], [1,2], [2], [2], [3],[0,3], [0,3,4], [0,1,4], [1,4,5], [5,1,2], [2,5,6], [2,6], [6], [7], [3,7], [3,7,8], [3,4,8], [8,4,9], [4,5,9], [9,10,5], [5,6,10], [6,10,11], [6,11], [11], [7], [7,12], [7,12,8], [8,12,13], [8,13,9], [9,13,14], [10,9,14], [10,14,15], [10,11,15], [11,15], [11], [12], [12,16], [12,16,13], [13,16,17], [13,17,14], [14,17,18], [14,15,18], [15,18], [15], [16], [16], [16,17], [17], [17,18], [18], [18]]
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
        self.harbor_ownership = 9*[False]
        self.bank = Bank()
        self.turn_tree = 13*[[] for i in range(13)]
        self.pygame_coords = (None,None)
    def generate_random_board(self):
        # 4*Pasture, 4*Forest, 4*Fields, 3*Hills, 3*Mountains, 1*Desert
        # 1*2, 2*3, 2*4, 2*5, 2*6, 2*8, 2*9, 2*10, 2*11, 1*12
        n = ([2]+2*[3]+2*[4]+2*[5]+2*[6]+2*[8]+2*[9]+2*[10]+2*[11]+[12])
        random.shuffle(self.terrains)
        random.shuffle(n)
        random.shuffle(self.harbors)
        n.insert(self.terrains.index("Desert"),0)
        self.numbers = n
    def legal_placement(self,loc,player,pregame=False):
        if pregame and loc not in LEGAL_PREGAME:
            return False
        if not pregame and (not self.bank.can_afford("Settlment",player)[0]) and (player not in self.road_corners[loc]):
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
    def place_settlement(self,loc,player,pregame=False):
        if not self.legal_placement(loc,player,pregame):
            return False
        self.bank.craft("Settlement",player)
        self.settlement_locations[loc] = player
        self.clear_corners[loc] = False
        self.road_corners[loc].append(player)
        for tile in VERTEX_CONTACTS[loc]:
            self.turn_tree[self.numbers[tile]].append((self.terrains[tile],player))
        if loc in HARBOR_LOCATIONS:
            self.harbor_ownership[HARBOR_LOCATIONS.index(loc)//2] = player
            player.harbors_owned.append(self.harbors[HARBOR_LOCATIONS.index(loc//2)])
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
        #print(left_vertex,right_vertex)
        if (player in self.road_corners[left_vertex]) or (player in self.road_corners[right_vertex]):
            if (pregame == False and self.bank.can_afford("Road",player)) or (left_vertex == pregame or right_vertex == pregame):
                return True, left_vertex, right_vertex
        else:
            return False, left_vertex, right_vertex
    def place_road(self,loc,player,pregame=False):
        result = self.legal_road(loc,player,pregame)
        if result[0]:
            if not pregame:
                self.bank.craft("Road",player)
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

class Bank():
    def __init__(self, *args, **kwargs):
        self.resource_cards = {"Brick":0,"Lumber":0,"Ore":0,"Grain":0,"Wool":0}
        self.building_costs = {"Settlement":{"Brick":1,"Lumber":1,"Ore":0,"Grain":1,"Wool":1},
                               "Road":{"Brick":1,"Lumber":1,"Ore":0,"Grain":0,"Wool":0},
                               "City":{"Brick":0,"Lumber":0,"Ore":3,"Grain":0,"Wool":2},
                               "Development_Card":{"Brick":0,"Lumber":0,"Ore":1,"Grain":1,"Wool":1}}
        self.resources = ["Brick","Lumber","Ore","Grain","Wool"]
        self.max_crafts = {"Settlement":5,"City":4,"Road":15}
        self.reset_bank()
    def reset_bank(self):
        self.resource_cards = {"Brick":19,"Lumber":19,"Ore":19,"Grain":19,"Wool":19}
    def give_resources(self,resource,players):
        if self.resource_cards[resource] > len(players):
            for player in players:
                player.resources_cards[resources] += 1
        self.resources_cards[resources] -= len(players)
    def give_resource(self,resource,player):
        if self.resource_cards[resource] > 0:
            player.resource_cards[resource] += 1
        self.resource_cards[resource] -= 1
    def can_afford(self,thing,player):
        if self.max_crafts[thing] <= player.craft_count[thing]:
            return False, "Player has no remaining {}".format(thing)
        for key in self.resources:
            if player.resource_cards[key] < self.building_costs[thing][key]:
                return False, "insufficent funds"
    def craft(self,thing,player):
        if not self.can_afford(thing,player)[0]:
            return self.can_afford(thing,player)
        for key in self.resources:
            player.resource[key] -= self.building_costs[thing][key]
            self.resource_cards += self.building_costs[thing][key]
            return True
    def dice_rolled(self,turn_tree):
        terrain_to_resource = {"Forest":"Lumber","Hills":"Brick","Mountains":"Ore","Fields":"Grain","Pasture":"Wool"}
        if len(turn_tree) == 0:
            return True
        for e in turn_tree:
            self.give_resource(terrain_to_resource[e[0]],e[1])

class Dice():
    def roll_one(self):
        return random.randint(1,6)
    def roll_two(self):
        return random.randint(1,6) + random.randint(1,6)












