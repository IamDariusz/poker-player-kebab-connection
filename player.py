import json

class Player:
    VERSION = "Kebab Mestro 0.11"

    def betRequest(self, game_state):
        json = json.loads(game_state)
        
        
        return do_bet(json)

    def showdown(self, game_state):
        pass

    def do_bet(json):
        return json(["current_buy_in"])

