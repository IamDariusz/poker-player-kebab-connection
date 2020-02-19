import json

class Player:
    VERSION = "Kebab Maestro 0.18"

    def betRequest(self, game_state):
        for player in game_state["players"]:
            if player["name"] == "Kebab Connection":
                return player["stack"]/2
            else:
                continue


    def showdown(self, game_state):
        pass




