class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """initialize the games Statics settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 640
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_limit = 3
        
        #Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #alien settings
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represents left


        #how qucikly the game speeds up
        self.startup_scale = 1.1
        #How quickly thhe alien pooins values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize setting that change throughout the game"""
        self.bullet_speed = 2.5
        self.ship_speed = 1.5
        self.alien_speed = 1.0

        #fleet_direction of 1 represents right; -1 represemts left
        self.fleet_direction = 1

        #scoreing setting
        self.alien_point = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_point = int(self.alien_point * self.score_scale)
        print(self.alien_point)