from minigame_ids import MinigameIds
# So far all the stuff that will be consitent with every minigame, but I imagine that will soon enough.

class Minigame:
    def __init__(self, resources, screen_width, screen_height, speed, max_time_multiplier):
        self.resources = resources
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = speed
        self.max_time_multiplier = max_time_multiplier
        self.id = MinigameIds.MGNONE
        self.win = False
        self.time = 0
        self.max_time = 7*max_time_multiplier
        self.instruction = ""

    def update(self):
        pass

    def render(self):
        pass
