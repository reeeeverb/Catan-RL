import board, game
class Player():
    def __init__(self,*args,**kwargs):
        self.settlement_locations = []
        self.city_locations = []
        self.road_locations = []
        self.resource_cards = {"Brick":0, "Lumber":0, "Ore":0, "Grain":0, "Wool":0}
        self.development_cars = []
