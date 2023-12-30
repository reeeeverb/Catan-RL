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
        self.victory_points = 0
        self.possible_road = []
    def set_info(self,name,color,human):
        self.name = name
        self.color = color
        self.human = human
    def other_player(self):
        return
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
        
