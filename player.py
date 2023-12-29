import board, game
class Player():
    def __init__(self,*args,**kwargs):
        self.settlement_locations = []
        self.city_locations = []
        self.road_locations = []
        self.resource_cards = {"Brick":0, "Lumber":0, "Ore":0, "Grain":0, "Wool":0}
        self.development_cars = []
        self.harbors_owned = []
        self.craft_count = {"Settlement":0,"City":0,"Road":0,"Development_Card":0}
        self.name = "None"
        self.color = None
        self.human = True
    def set_info(self,name,color,human):
        self.name = name
        self.color = color
        self.human = human
    def place_settlement(self,board,loc,pregame=False):
        if board.legal_placement(loc,self,pregame):
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
        
