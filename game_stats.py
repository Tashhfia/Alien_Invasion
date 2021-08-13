class GameStats:
    """stats of the game"""
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        # game is active
        self.game_active = False

    def reset_stats(self):
        self.spaceShips_left = self.settings.spaceShip_limit