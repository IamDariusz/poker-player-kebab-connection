import json

class Player:
    VERSION = "Kebab Maestro 0.18"

    def check_how_many_active(self, game_state):
        count = 0
        for player in game_state["players"]:
            if player["status"] == "active":
                count = count + 1
        return count

    def get_first_non_kebab_active_player(self, game_state):
        for player in game_state["players"]:
            if player["name"] == "Kebab Connection":
                continue
            if player["status"] == "active":
                return player

    def betRequest(self, game_state):
        for player in game_state["players"]:
            if player["name"] == "Kebab Connection":
                if self.check_how_many_active(game_state) > 1:
                    return player["stack"]/2
                else:
                    return (self.get_first_non_kebab_active_player(game_state)["stack"])/2
            else:
                continue


    def showdown(self, game_state):
        pass




