class GameStats:
    """Track statistics for Alien In"""

    def __init__(self, ai_game):
        """Inialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        #high score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialize stats that can change durring the game"""
        self.ships_left =  self.settings.ship_limit
        self.score = 0
        self.level = 1