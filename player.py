import json

class Player:
    VERSION = "Kebab Maestro 1.0"

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

    def get_me(self, game_state):
        for player in game_state["players"]:
            if player["name"] == "Kebab Connection":
                return player

    def have_pair(self, game_state):
        me = self.get_me(game_state)
        card1 = me["hole_cards"][0]["rank"]
        card2 = me["hole_cards"][1]["rank"]
        if card1 == card2:
            return True
        else:
            return False

    def get_ranking(self, game_state):
        me = self.get_me(game_state)
        card1 = me["hole_cards"][0]["rank"]
        card2 = me["hole_cards"][1]["rank"]

        listshit = ["2", "3", "4", "5", "6", "7", "8"]

        ranking = 0
        # get lost for everything under 9
        if card1 in listshit or card2 in listshit:
            if card1 == card2 and card1 > 6:
                ranking = 0.5

        if self.have_pair(game_state):
            if card1 == "9":
                ranking = 0.6
            if card1 == "T":
                ranking = 0.66

        list1 = ["A", "Q", "K", "J", "T"]
        if card1 in list1 and card2 in list1:
            ranking = 1

        return ranking
    
    def get_river_rank(self, game_state):
        me = self.get_me(game_state)
        river_card1 = me["community_cards"][0]["rank"]
        river_card2 = me["community_cards"][1]["rank"]
        river_card3 = me["community_cards"][2]["rank"]

        river_list_rank = []
        river_list_rank.append(river_card1)
        river_list_rank.append(river_card2)
        river_list_rank.append(river_card3)

        return river_list_rank

    def betRequest(self, game_state):
        me = self.get_me(game_state)
        active_players = self.check_how_many_active(game_state)
        my_ranking = self.get_ranking(game_state)

        if my_ranking == 0:
            return 0

        if my_ranking == 1:
            return me["stack"]

        if active_players > 1:
            if me["stack"] < 200:
                if game_state["current_buy_in"] < 50:
                    return 50
                else:
                    return 0
            else:
                return me["stack"] / 2
        else:
            if me["stack"] < 200:
                return (self.get_first_non_kebab_active_player(game_state)["stack"])
            else:
                return (self.get_first_non_kebab_active_player(game_state)["stack"]) / 2

    def showdown(self, game_state):
        pass




