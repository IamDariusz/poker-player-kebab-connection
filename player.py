import json

class Player:
    VERSION = "Kebab Mestro 0.12"

    def betRequest(self, game_state):
        json = json.loads(game_state)
        
        return 25

    def showdown(self, game_state):
        pass

    def do_bet(json):
        return json["current_buy_in"]




