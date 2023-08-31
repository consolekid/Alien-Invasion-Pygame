import json

class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initialise statistics"""
        filename = 'high_score.json'
        with open(filename) as f:
            high_score = json.load(f)

        self.settings = ai_game.settings 
        self.reset_stats()
        #start alien invasion in an inactive state.
        self.game_active = False
        #high score should never be reset
        self.high_score = high_score
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    def save_high_score(self):
        """Save the high score so it is available after the game has quit"""
        high_score = self.high_score
        
        filename = 'high_Score.json'
        with open(filename, 'w') as f:
            json.dump(high_score, f)

        

        
    