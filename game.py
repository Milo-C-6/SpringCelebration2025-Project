import pyray as pr
import random
from minigames.sewing import MgSewing
from minigames.electrician import MgElectrician
from resource_type import ResourceType
from minigames.sewing import MgSewing
from minigames.powerwash import MgPowerwash

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

        assets = ["assets/Arrow_Up_Key_Light.png","assets/Arrow_Right_Key_Light.png","assets/Arrow_Down_Key_Light.png","assets/Arrow_Left_Key_Light.png","assets/Sewing_Monster_Doll.png","assets/Sewing_Monster_Doll_Complete.png","assets/Starburst_Explosion.png","assets/Powerwash_Gun.png","assets/Sidewalk.png","assets/Splat_1.png","assets/Splat_2.png","assets/Splat_Coffee.png","assets/Splat_Stripe.png","assets/Sparkles_PLACEHOLDER.png","assets/computer.png","assets/background.png","assets/electricity.png","assets/Plug.png","assets/wire.png","assets/screen1.png","assets/wire2.png","assets/connect_wire1.png","assets/connect_wire2.png"]
        iteration = 0

        for key in ResourceType:
            image = pr.load_image(assets[iteration])
            self.resources[key] = pr.load_texture_from_image(image)
            print(key)
            pr.unload_image(image)
            iteration+=1

        #Will likely be moved to the update loop for when an actual menu, and a transition is made
        if self.current_minigame == None:
            self.current_minigame = MgPowerwash(self.resources, self.screen_width, self.screen_height)

    def update(self):
        if self.current_minigame != None:
            self.current_minigame.update()

    def render(self):
        if self.current_minigame != None:
            self.current_minigame.render()

    def shutdown(self):
        for key in ResourceType:
            pr.unload_texture(self.resources[key])

        pr.close_audio_device()
        
