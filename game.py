import pyray as pr
import random
from resource_type import ResourceType
from minigame_ids import MinigameIds
from minigames.sewing import MgSewing
from minigames.electrician import MgElectrician
from minigames.powerwash import MgPowerwash
from minigames.solder import MgSolder
from minigames.music import MgMusic

class Game:
    def __init__(self, screen_width, screen_height):
        self.resources = {}
        self.screen_width = screen_width
        self.screen_height = screen_height
        # self.speed = 1
        # self.difficulty = 1
        self.current_minigame = None
        self.played_minigames = [None]
        self.debug_minigame = None # Replace this with the minigame you wanna debug, so if you wanna debug sewing you would set it to "MinigameIds.MGSEWING"
        # When a debug minigame is set, itll skip most of the elevator transition

        self.elevator_size = pr.Vector2(screen_width,screen_height)
        self.transition_tick = 0 # max 181, dont edit if you already have a debug minigame set
        self.text_y_tick = 61
        self.door_width = 191
        self.transition = pr.load_render_texture(1280,720)
        self.stopwatch_color = pr.WHITE
        self.stopwatch_time = 7
        self.text_pos_y = self.screen_height//2
        self.text_size = 250 #40

    def startup(self):
        pr.init_audio_device()

        #i love having to scroll to the end of this to add images - Milo 3/7/25
        # Alt+Z to toggle Word Wrap, makes this MUCH easier - Milo 3/8/25
        assets = ["assets/Arrow_Up_Key_Light.png","assets/Arrow_Right_Key_Light.png","assets/Arrow_Down_Key_Light.png","assets/Arrow_Left_Key_Light.png","assets/Sewing_Monster_Doll.png","assets/Sewing_Monster_Doll_Complete.png","assets/Starburst_Explosion.png","assets/Powerwash_Gun.png","assets/Sidewalk.png","assets/Splat_1.png","assets/Splat_2.png","assets/Splat_Coffee.png","assets/Splat_Stripe.png","assets/Sparkles.png","assets/computer.png","assets/background.png","assets/electricity.png","assets/Plug.png","assets/wire.png","assets/screen1.png","assets/wire2.png","assets/connect_wire1.png","assets/connect_wire2.png","assets/Elevator.png","assets/Timer.png","assets/PCB.png","assets/Solder.png","assets/Solder_Iron.png","assets/LED_Off.png","assets/LED_On.png","assets/Check.png","assets/Important.png","assets/Wrong.png","assets/D_Key_Light.png","assets/F_Key_Light.png","assets/J_Key_Light.png","assets/K_Key_Light.png","assets/Sheet_Music_Transparent.png","assets/Guitar_1_3_7.mp3","assets/Guitar_2.mp3","assets/Guitar_4_6.mp3","assets/Guitar_5.mp3","assets/Guitar_8.mp3","assets/Guitar_9.mp3","assets/tape.png","assets/tapedWire.png","assets/lasttaskbg.png","assets/screen2.png","assets/Mouse_Left_Key_Light.png","assets/JobWare.png"]
        iteration = 0

        for key in ResourceType:
            if key.name[:5]=="SOUND":
                print("Loaded sound")
                self.resources[key] = pr.load_sound(assets[iteration])
            else:
                image = pr.load_image(assets[iteration])
                self.resources[key] = pr.load_texture_from_image(image)
                pr.unload_image(image)
            iteration+=1

    def update(self):
        if pr.is_mouse_button_pressed(pr.MOUSE_RIGHT_BUTTON):
            print(pr.get_mouse_position().x,pr.get_mouse_position().y)
        if self.transition_tick != 181:
            if self.debug_minigame != None and self.transition_tick == 0:
                self.transition_tick = 109

            self.transition_tick+=1

            if self.transition_tick < 0:
                # print(print(self.elevator_size.y))
                # print(1/0) intentionally causing errors is a real good way to get values :D . Python debugger? Never heard of her
                self.elevator_size = pr.vector2_add(self.elevator_size,pr.Vector2(-51.37,-28.9)) #fresh value, guess where it came from?
                self.door_width += 16
                self.stopwatch_color = pr.WHITE
            # i wish i knew about texture mode before, im going to crash out
            pr.begin_texture_mode(self.transition)

            pr.clear_background(pr.WHITE)
            #Door, Top left (455, 40), Top right (836,39), Bottom Right (836, 695), Bottom Left (454, 695)
            # pr.draw_rectangle(391,183,int(self.door_width),537,pr.Color(188,188,188,255))
            pr.draw_rectangle(455,39,self.door_width,657,pr.Color(188,188,188,255))
            pr.draw_rectangle(837+(-self.door_width),39,self.door_width,657,pr.Color(188,188,188,255)) # I have no clue what possesed me to think of that math for the door
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_MAIN_ELEVATOR],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_MAIN_ELEVATOR].width,self.resources[ResourceType.TEXTURE_MAIN_ELEVATOR].height),
                pr.Rectangle(self.screen_width//2,self.screen_height//2,self.screen_width,self.screen_height),
                pr.Vector2(self.screen_width/2,self.screen_height/2),
                0,
                pr.WHITE
            )
            pr.end_texture_mode()
            if self.transition_tick >= 110:
                if self.transition_tick == 110:
                    if self.debug_minigame != None:
                        proposed_minigame = self.debug_minigame.value
                    else:
                        proposed_minigame = self.played_minigames[0]

                    while proposed_minigame in self.played_minigames:
                        proposed_minigame = random.randint(1,5) # second value is number of completed minigames

                    match proposed_minigame: # I want current_minigame to be assigned a new Minigame class, and this does that I think, but I feel like there should be a better way...
                        case MinigameIds.MGSEWING.value:
                            self.current_minigame = MgSewing(self.resources, self.screen_width, self.screen_height)
                        case MinigameIds.MGPOWERWASH.value:
                            self.current_minigame = MgPowerwash(self.resources, self.screen_width, self.screen_height)
                        case MinigameIds.MGELECTRICIAN.value:
                            self.current_minigame = MgElectrician(self.resources, self.screen_width, self.screen_height)
                        case MinigameIds.MGSOLDER.value:
                            self.current_minigame = MgSolder(self.resources, self.screen_width, self.screen_height)
                        case MinigameIds.MGMUSIC.value:
                            self.current_minigame = MgMusic(self.resources,self.screen_width,self.screen_height)
                        case _:
                            print("someone messed up")
                    self.text_size = 250
                    self.text_pos_y = 360
                    self.current_minigame.update()
                if not self.transition_tick > 129:
                    self.door_width -= 15
                if not self.text_size < 60:
                    self.text_size -= 15
                if self.transition_tick > 120:
                    self.elevator_size = pr.vector2_add(self.elevator_size,pr.Vector2(16,9))
                    if self.transition_tick == 180:
                        self.current_minigame.time = pr.get_time()
                        self.text_y_tick = 0
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
        
        if self.text_y_tick!=61:
            self.text_pos_y-=15
            self.text_y_tick+=1

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
        if self.current_minigame != None:
            pr.draw_text(self.current_minigame.instruction,int(self.screen_width//2-(pr.measure_text(self.current_minigame.instruction,self.text_size)/2)),int(self.text_pos_y),self.text_size,pr.BLACK)

    def shutdown(self):
        for key in ResourceType:
            pr.unload_texture(self.resources[key])

        pr.close_audio_device()
        
