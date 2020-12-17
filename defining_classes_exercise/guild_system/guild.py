from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player: Player):
        if player in self.list_of_players:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        self.list_of_players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if player_name in [p.name for p in self.list_of_players]:
            p = [p for p in self.list_of_players if p.name == player_name][0]
            self.list_of_players.remove(p)
            Player.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        result += '\n'.join([p.player_info() for p in self.list_of_players])
        return result
