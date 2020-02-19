import json

class Player:
    VERSION = "Kebab Mestro 0.1"

    def betRequest(self, game_state):
        json = json.loads(game_state)
        

        return json(["current_buy_in"])

    def showdown(self, game_state):
        pass

