import json

class Player:
    VERSION = "Kebab Maestro 0.21"

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
                    if player["stack"] < 200:
                        if game_state["current_buy_in"] < 50:
                            return 50
                        else:
                            return 0
                    else:
                        return player["stack"]/2
                else:
                    if player["stack"] < 200:
                        return (self.get_first_non_kebab_active_player(game_state)["stack"])
                    else:
                        return (self.get_first_non_kebab_active_player(game_state)["stack"])/2
            else:
                continue


    def showdown(self, game_state):
        pass




