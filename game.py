import pyray as pr
import random
from minigames.sewing import MgSewing
from resource_type import ResourceType

class Game:
    def __init__(self, screen_width, screen_height):
        self.resources = {}
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = 1
        self.difficulty = 1
        self.current_minigame = None
        self.transition_tick = 1 #will be changed for when the transition is made

    def startup(self):
        pr.init_audio_device()

        assets = ["assets/Arrow_Up_Key_Light.png","assets/Arrow_Right_Key_Light.png","assets/Arrow_Down_Key_Light.png","assets/Arrow_Left_Key_Light.png","assets/Sewing-monster-doll.png"]
        iteration = 0

        for key in ResourceType:
            image = pr.load_image(assets[iteration])
            self.resources[key] = pr.load_texture_from_image(image)
            pr.unload_image(image)
            iteration+=1

        #Will likely be moved to the update loop for when an actual menu, and a transition is made
        if self.current_minigame == None:
            self.current_minigame = MgSewing(self.resources, self.screen_width, self.screen_height)

    def update(self):
        if self.current_minigame != None:
            self.current_minigame.update()

    def render(self):
        if self.current_minigame != None:
            self.current_minigame.render()

    def shutdown(self):
        pr.unload_texture(self.resources[ResourceType.TEXTURE_KEY_UP])
        pr.unload_texture(self.resources[ResourceType.TEXTURE_KEY_DOWN])

        pr.close_audio_device()
        