import pyray as pr
import random
from resource_type import ResourceType

class PwSplat:
    def __init__(self, screen_width, screen_height):
        self.position = pr.Vector2(random.randint(200,screen_width-200),random.randint(200,screen_height-200))
        if screen_width >= screen_height:
            self.size = screen_width*(0.4/1280)
        else:
            self.size = screen_height*(0.4/1280)

        colors = [pr.GREEN, pr.BROWN, pr.BLUE, pr.Color(218, 247, 166, 254),pr.BLACK]
        splats = [ResourceType.TEXTURE_SPLAT_1,ResourceType.TEXTURE_SPLAT_2,ResourceType.TEXTURE_SPLAT_STRIPE,ResourceType.TEXTURE_SPLAT_COFFEE]

        self.texture = splats[random.randint(0,len(splats)-1)]
        
        self.color = colors[random.randint(0,len(colors)-1)]
        self.alpha = 1.0