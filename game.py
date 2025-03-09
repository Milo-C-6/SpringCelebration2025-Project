import pyray as pr
import random
from resource_type import ResourceType
from minigame_ids import MinigameIds
from minigames.sewing import MgSewing
from minigames.electrician import MgElectrician
from minigames.powerwash import MgPowerwash

class Game:
    def __init__(self, screen_width, screen_height):
        self.resources = {}
        self.screen_width = screen_width
        self.screen_height = screen_height
        # self.speed = 1
        # self.difficulty = 1
        
        self.current_minigame = None
        self.played_minigames = [None]
        self.debug_minigame = MinigameIds.MGELECTRICIAN # Replace this with the minigame you wanna debug, so if you wanna debug sewing you would set it to "MinigameIds.MGSEWING"
        # When a debug minigame is set, itll skip most of the elevator transition

        self.elevator_size = pr.Vector2(screen_width,screen_height)
        self.transition_tick = 0 # max 181, dont edit if you already have a debug minigame set
        self.door_width = 498
        self.transition = pr.load_render_texture(1280,720)
        self.stopwatch_color = pr.WHITE
        self.stopwatch_time = 7

    def startup(self):
        pr.init_audio_device()

        #i love having to scroll to the end of this to add images
        assets = ["assets/Arrow_Up_Key_Light.png","assets/Arrow_Right_Key_Light.png","assets/Arrow_Down_Key_Light.png","assets/Arrow_Left_Key_Light.png","assets/Sewing_Monster_Doll.png","assets/Sewing_Monster_Doll_Complete.png","assets/Starburst_Explosion.png","assets/Powerwash_Gun.png","assets/Sidewalk.png","assets/Splat_1.png","assets/Splat_2.png","assets/Splat_Coffee.png","assets/Splat_Stripe.png","assets/Sparkles_PLACEHOLDER.png","assets/computer.png","assets/background.png","assets/electricity.png","assets/Plug.png","assets/wire.png","assets/screen1.png","assets/wire2.png","assets/connect_wire1.png","assets/connect_wire2.png","assets/Elevator_Programmer_Art.png","assets/Timer.png","assets/tape.png","assets/tapedWire.png","assets/lasttaskbg.png"]
        iteration = 0

        for key in ResourceType:
            image = pr.load_image(assets[iteration])
            self.resources[key] = pr.load_texture_from_image(image)
            print(key)
            pr.unload_image(image)
            iteration+=1

    def update(self):
        if self.transition_tick != 181:
            if self.debug_minigame != None and self.transition_tick == 0:
                self.transition_tick = 109

            self.transition_tick+=1

            if self.transition_tick < 0:
                self.elevator_size = pr.vector2_add(self.elevator_size,pr.Vector2(-48.15,-48.15)) #fresh value, guess where it came from?
                self.door_width += 56.85
                self.stopwatch_color = pr.WHITE
            # i wish i knew about texture mode before, im going to crash out
            pr.begin_texture_mode(self.transition)

            # pr.clear_background(pr.WHITE)
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_MAIN_ELEVATOR],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_MAIN_ELEVATOR].width,self.resources[ResourceType.TEXTURE_MAIN_ELEVATOR].height),
                pr.Rectangle(self.screen_width//2,self.screen_height//2,self.screen_width,self.screen_height),
                pr.Vector2(self.screen_width/2,self.screen_height/2),
                0,
                pr.WHITE
            )
            pr.draw_rectangle(391,183,int(self.door_width),537,pr.GRAY)

            pr.end_texture_mode()
            if self.transition_tick >= 110:
                if self.transition_tick == 110:
                    if self.debug_minigame != None:
                        proposed_minigame = self.debug_minigame.value
                    else:
                        proposed_minigame = self.played_minigames[0]

                    while proposed_minigame in self.played_minigames:
                        proposed_minigame = random.randint(1,2) # second value is number of completed minigames

                    match proposed_minigame: # I want current_minigame to be assigned a new Minigame class, and this does that I think, but I feel like there should be a better way...
                        case 1:
                            self.current_minigame = MgSewing(self.resources, self.screen_width, self.screen_height)
                        case 2:
                            self.current_minigame = MgPowerwash(self.resources, self.screen_width, self.screen_height)
                        case 3:
                            self.current_minigame = MgElectrician(self.resources, self.screen_width, self.screen_height)
                        case _:
                            print("someone messed up")

                    self.current_minigame.update()

                self.door_width -= 15

                if self.transition_tick > 120:
                    self.elevator_size = pr.vector2_add(self.elevator_size,pr.Vector2(15,15))
                    if self.transition_tick == 180:
                        self.current_minigame.time = pr.get_time()
        
        elif self.current_minigame != None:
            self.current_minigame.update()
            self.stopwatch_time = round(self.current_minigame.max_time-(pr.get_time()-self.current_minigame.time),2)
            if self.current_minigame.win:
                self.stopwatch_color = pr.GREEN
            else:
                if self.stopwatch_time < 0:
                    self.stopwatch_color = pr.RED

            if self.stopwatch_time < -0.4:
                self.played_minigames[0] = self.current_minigame.id.value
                self.current_minigame = None
                self.transition_tick = -20

    def render(self): #i love the saxophone in this goofy punk rock french song https://www.youtube.com/watch?v=zreo9Y3EieA
        if self.current_minigame != None:
            self.current_minigame.render()

            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_TIMER],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_TIMER].width,self.resources[ResourceType.TEXTURE_TIMER].height),
                pr.Rectangle(0,720,200,258),
                pr.Vector2(0,258),
                0,pr.WHITE
            )

            pr.draw_text(str(self.stopwatch_time),50,590,50,self.stopwatch_color)


        if self.transition_tick != 181:
            pr.draw_texture_pro(
                self.transition.texture,
                pr.Rectangle(0,0,self.screen_width,-self.screen_height),
                pr.Rectangle(self.screen_width/2,self.screen_height/2,self.elevator_size.x,self.elevator_size.y),
                pr.Vector2(self.elevator_size.x/2,self.elevator_size.y/2),
                0,
                pr.WHITE
            )

    def shutdown(self):
        for key in ResourceType:
            pr.unload_texture(self.resources[key])

        pr.close_audio_device()
        
