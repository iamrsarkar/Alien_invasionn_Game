class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (195, 240, 255)
        #ship settings 
        self.ship_speed= 1.2
        self.ship_limit = 4
        # Bullet settings
        self.bullet_speed = 1.3
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = (150, 60, 60)
        self.bullets_allowed = 6
        # Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 4.5
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        #cloud settings
        self.cloud_speed=.2