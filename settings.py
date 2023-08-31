class Settings:
    """A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize the game's static settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (16, 15, 74)
        
        #ship settings
        self.ship_limit = 3
        
        #bullet settings
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_colour = (255, 165, 0)
        self.bullets_allowed = 3
        
        #alien settings
        
        self.fleet_drop_speed = 10
        
        #how quickly the game speeds up
        self.speedup_scale = 1.1

        #how quickly the alien point value increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the dynamic settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        #fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50
        
    def increase_speed(self):
        """Increase the speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
        