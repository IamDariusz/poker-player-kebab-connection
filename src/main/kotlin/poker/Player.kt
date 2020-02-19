package poker

import org.json.JSONObject

class Player {
    fun betRequest(game_state: JSONObject): Int {
        print(game_state)
        return 0
    }

    fun showdown() {
    }

    fun version(): String {
        return "Kotlin Player 0.0.1"
    }
}
