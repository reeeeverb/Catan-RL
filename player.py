import board, game
class Player():
    def __init__(self,*args,**kwargs):
        self.settlement_locations = []
        self.city_locations = []
        self.road_locations = []
        self.resource_cards = {"Brick":0, "Lumber":0, "Ore":0, "Grain":0, "Wool":0}
        self.development_cards = {"VP":0,"Knight":0,"YOP":0,"Monopoly":0,"RB":0}
        self.harbors_owned = []
        self.craft_count = {"Settlement":0,"City":0,"Road":0,"Development_Card":0}
        self.name = "None"
        self.color = None
        self.human = True
        self._victory_points = 0
        self.possible_road = []
        self.played_knights = 0
        self.largest_army = False
    def adjust_victory_points(self,value):
        player._victory_points += value
        if player._victory_points > 9:
            print("Game Over")
    def set_info(self,name,color,human):
        self.name = name
        self.color = color
        self.human = human
    def discard_half(self):
        return
    def give_largest_army(self):
        if self.largest_army == False:
            self.adjust_victory_points(2)
            self.largest_army = True
    def remove_largest_army(self):
        if self.largest_army == True:
            self.adjust_victory_points(-2)
            self.largest_army = False
    def place_settlement(self,board,loc,pregame=False):
        if board.legal_placement(loc,self,pregame)[0]:
            board.place_settlement(loc,self,pregame)
            self.craft_count["Settlement"]+=1
            return True
        return False 
    def place_road(self,board,loc,pregame=False):
        if board.legal_road(loc,self,pregame)[0]:
            board.place_road(loc,self,pregame)
            self.craft_count["Road"]+=1
            return True
        return False
        
