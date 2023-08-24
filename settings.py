class Settings:
    """A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (16, 15, 74)
        
        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        #bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 20
        self.bullet_height = 15
        self.bullet_colour = (255, 165, 0)
        self.bullets_allowed = 3
        
        #alien settings
        self.alien_speed = 4.0
        self.fleet_drop_speed = 20
        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        
        