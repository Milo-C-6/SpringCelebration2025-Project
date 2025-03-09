from minigame_ids import MinigameIds
# So far all the stuff that will be consitent with every minigame, but I imagine that will soon enough.

class Minigame:
    def __init__(self, resources, screen_width, screen_height):
        self.resources = resources
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.id = MinigameIds.MGNONE
        self.win = False
        self.time = 0
        self.max_time = 7

    def update(self):
        pass

    def render(self):
        pass
