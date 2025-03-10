import pyray as pr
import random
from resource_type import ResourceType
from minigame_ids import MinigameIds
from minigames.sewing import MgSewing
from minigames.electrician import MgElectrician
from minigames.powerwash import MgPowerwash
from minigames.solder import MgSolder
from minigames.music import MgMusic
from minigames.construct import MgConstruct
from minigames.archaeology import MgArchaeology

class Game:
    def __init__(self, screen_width, screen_height):
        self.resources = {}
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = 1
        self.max_time_multiplier = 1
        self.current_minigame = None
        self.played_minigames = [None]
        self.debug_minigame = None # Replace this with the minigame you wanna debug, so if you wanna debug sewing you would set it to "MinigameIds.MGSEWING"
        # When a debug minigame is set, itll skip most of the elevator transition
        self.playing = False # make sure to set this if you have a debug minigame!!!
        self.elevator_size = pr.Vector2(screen_width,screen_height)
        self.transition_tick = 0 # max 181, dont edit if you already have a debug minigame set
        self.text_y_tick = 61
        self.door_width = 191
        self.transition = pr.load_render_texture(1280,720)
        self.stopwatch_color = pr.WHITE
        self.stopwatch_time = 7 # no clue why I called it "stopwatch", its a timer!!
        self.stopwatch_time_text = "7"
        self.text_pos_y = self.screen_height//2
        self.text_size = 250 #40
        self.title_colors = [pr.Color(165, 203, 242,255),pr.Color(0, 255, 255,255),pr.Color(15, 255, 80,255),pr.Color(76, 187, 23,255),pr.Color(255, 234, 0,255),pr.Color(255, 191, 0,255),pr.Color(255, 49, 49,255)]
        self.title_angle = 3
        self.direction = 0
        self.credits = False
        self.credits_txt = [line for line in open("credits.txt","r")]
        self.score = 0
        self.lives = 4
        self.lives_tick = 91
        self.lives_y = 730
        self.life_offset = pr.Vector2(0,0)
        self.lost_a_life = False
        self.game_end_score = 0
        self.speed_up_y = -75
        self.play_size = 1

    def startup(self):
        pr.init_audio_device()

        #i love having to scroll to the end of this to add images - Milo 3/7/25
        # Alt+Z to toggle Word Wrap, makes this MUCH easier - Milo 3/8/25
        assets = ["assets/Arrow_Up_Key_Light.png","assets/Arrow_Right_Key_Light.png","assets/Arrow_Down_Key_Light.png","assets/Arrow_Left_Key_Light.png","assets/Sewing_Monster_Doll.png","assets/Sewing_Monster_Doll_Complete.png","assets/Starburst_Explosion.png","assets/Powerwash_Gun.png","assets/Sidewalk.png","assets/Splat_1.png","assets/Splat_2.png","assets/Splat_Coffee.png","assets/Splat_Stripe.png","assets/Sparkles.png","assets/computer.png","assets/background.png","assets/electricity.png","assets/Plug.png","assets/wire.png","assets/screen1.png","assets/wire2.png","assets/connect_wire1.png","assets/connect_wire2.png","assets/Elevator.png","assets/Timer.png","assets/PCB.png","assets/Solder.png","assets/Solder_Iron.png","assets/LED_Off.png","assets/LED_On.png","assets/Check.png","assets/Important.png","assets/Wrong.png","assets/D_Key_Light.png","assets/F_Key_Light.png","assets/J_Key_Light.png","assets/K_Key_Light.png","assets/Sheet_Music_Transparent.png","assets/Guitar_1_3_7.mp3","assets/Guitar_2.mp3","assets/Guitar_4_6.mp3","assets/Guitar_5.mp3","assets/Guitar_8.mp3","assets/Guitar_9.mp3","assets/tape.png","assets/tapedWire.png","assets/lasttaskbg.png","assets/screen2.png","assets/Mouse_Left_Key_Light.png","assets/JobWare.png", "assets/Scroll.png","assets/7segment.ttf","assets/Heart.png","assets/Heart_Broken.png","assets/sounds/MainTheme.wav","assets/sounds/Background.wav","assets/sounds/ShortWin.wav","assets/sounds/Guitar_Fail.ogg","assets/Table_BG.jpg","assets/Wood.jpg","assets/sounds/Lose.wav","assets/Sewing_Needle.png","assets/sounds/Begin.ogg","assets/conbg.png","assets/condonebg.png","assets/block1.png","assets/block2.png","assets/Forest_BG.png","assets/Hole.png","assets/Shovel.png","assets/Pottery_Shard.png","assets/sounds/Dig.ogg"]
        iteration = 0

        for key in ResourceType:
            if key.name[:4]=="FONT":
                self.resources[key] = pr.load_font(assets[iteration])
            elif key.name[:5]=="SOUND":
                self.resources[key] = pr.load_sound(assets[iteration])
            elif key.name[:5]=="MUSIC":
                self.resources[key] = pr.load_music_stream(assets[iteration])
            else:
                image = pr.load_image(assets[iteration])
                self.resources[key] = pr.load_texture_from_image(image)
                pr.unload_image(image)
            iteration+=1

        pr.begin_texture_mode(self.transition)

        pr.clear_background(pr.WHITE)
        pr.draw_rectangle(455,39,191,657,pr.Color(188,188,188,255))
        pr.draw_rectangle(646,39,191,657,pr.Color(188,188,188,255))
        pr.draw_texture_pro(
            self.resources[ResourceType.TEXTURE_MAIN_ELEVATOR],
            pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_MAIN_ELEVATOR].width,self.resources[ResourceType.TEXTURE_MAIN_ELEVATOR].height),
            pr.Rectangle(self.screen_width//2,self.screen_height//2,self.screen_width,self.screen_height),
            pr.Vector2(self.screen_width/2,self.screen_height/2),
            0,
            pr.WHITE
        )
        pr.end_texture_mode()

        if not self.playing:
            pr.play_music_stream(self.resources[ResourceType.MUSIC_MAIN_MENU])

    def update(self):
        if self.lives_tick != 91:
            if self.lives_tick < 20:
                self.lives_y -= 8.5
                if self.score%3==0:
                    self.speed_up_y +=3.75
            elif self.lives_tick > 70:
                self.life_offset = pr.Vector2(0,0)
                self.lives_y += 8.5
                if self.score%3==0:
                    self.speed_up_y -=3.75
                pr.set_music_volume(self.resources[ResourceType.MUSIC_BACKGROUND],1)
                if self.lives_tick == 90: 
                    self.lost_a_life = False
                    if self.lives == 0: 
                        self.reset()
                        return
            elif self.lives_tick > 30 and self.lives_tick < 55:
                    self.life_offset = pr.Vector2(random.randint(-15,15),random.randint(-15,15))
            elif self.lives_tick == 56: self.life_offset = pr.Vector2(0,0)
            self.lives_tick+=1
        if not self.playing:
            pr.update_music_stream(self.resources[ResourceType.MUSIC_MAIN_MENU])
            if pr.check_collision_recs(pr.Rectangle(520,480,240,140),pr.Rectangle(pr.get_mouse_x(),pr.get_mouse_y(),2,2)):
                pr.set_mouse_cursor(4)
                if self.play_size <= 1.1:
                    self.play_size += 0.025
                if pr.is_mouse_button_pressed(pr.MOUSE_LEFT_BUTTON):
                    pr.play_sound(self.resources[ResourceType.SOUND_BEGIN])
                    pr.stop_music_stream(self.resources[ResourceType.MUSIC_MAIN_MENU])
                    pr.play_music_stream(self.resources[ResourceType.MUSIC_BACKGROUND])
                    self.playing = True
                    pr.set_mouse_cursor(0)
            else:
                if self.play_size >= 1:
                    self.play_size -= 0.025
                if pr.check_collision_circles(pr.Vector2(1235,45),39,pr.get_mouse_position(),2):
                    pr.set_mouse_cursor(4)
                    if pr.is_mouse_button_pressed(pr.MOUSE_LEFT_BUTTON):
                        if self.credits: self.credits = False
                        else: self.credits = True
                        pr.set_mouse_cursor(0)
                elif self.game_end_score > 1 and pr.check_collision_recs(pr.Rectangle(550,385,180,65),pr.Rectangle(pr.get_mouse_x(),pr.get_mouse_y(),2,2)):
                    pr.set_mouse_cursor(4)
                    if pr.is_mouse_button_pressed(pr.MOUSE_LEFT_BUTTON):
                        self.game_end_score = 0
                        pr.set_mouse_cursor(0)
                else:
                    pr.set_mouse_cursor(0)

            if self.direction == 0:
                self.title_angle -= 0.03
                if self.title_angle <= 0:
                    self.direction = 1
            else:
                self.title_angle += 0.03
                if self.title_angle >= 3:
                    self.direction = 0
        else:
            pr.update_music_stream(self.resources[ResourceType.MUSIC_BACKGROUND])
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
                pr.begin_texture_mode(self.transition) #=====================================BEGIN TEXTURE MODE (added this cuz I keep missing it)=====================================#

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
                pr.draw_text_ex(self.resources[ResourceType.FONT_7SEGMENT],str(self.score),pr.Vector2(293,105),70,5,pr.GREEN)
                pr.end_texture_mode() #=====================================END TEXTURE MODE=====================================#
                if self.transition_tick >= 110:
                    if self.transition_tick == 110:
                        if self.debug_minigame != None:
                            proposed_minigame = self.debug_minigame.value
                        else:
                            proposed_minigame = self.played_minigames[0]

                        while proposed_minigame in self.played_minigames:
                            proposed_minigame = random.randint(1,7) # second value is number of completed minigames

                        match proposed_minigame: # I want current_minigame to be assigned a new Minigame class, and this does that I think, but I feel like there should be a better way...
                            case MinigameIds.MGSEWING.value:
                                self.current_minigame = MgSewing(self.resources, self.screen_width, self.screen_height,self.speed,self.max_time_multiplier)
                            case MinigameIds.MGPOWERWASH.value:
                                self.current_minigame = MgPowerwash(self.resources, self.screen_width, self.screen_height,self.speed,self.max_time_multiplier)
                            case MinigameIds.MGELECTRICIAN.value:
                                self.current_minigame = MgElectrician(self.resources, self.screen_width, self.screen_height,self.speed,self.max_time_multiplier)
                            case MinigameIds.MGSOLDER.value:
                                self.current_minigame = MgSolder(self.resources, self.screen_width, self.screen_height,self.speed,self.max_time_multiplier)
                            case MinigameIds.MGMUSIC.value:
                                self.current_minigame = MgMusic(self.resources,self.screen_width,self.screen_height,self.speed,self.max_time_multiplier)
                                pr.set_music_volume(self.resources[ResourceType.MUSIC_BACKGROUND],0.2)
                            case MinigameIds.MGCONSTRUCT.value:
                                self.current_minigame = MgConstruct(self.resources, self.screen_width, self.screen_height, self.speed, self.max_time_multiplier)
                            case MinigameIds.MGARCHAEOLOGY.value:
                                self.current_minigame = MgArchaeology(self.resources, self.screen_width, self.screen_height, self.speed, self.max_time_multiplier)
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
                if self.stopwatch_time >= 0:
                    self.stopwatch_time_text = str(self.stopwatch_time)
                if self.current_minigame.win:
                    self.stopwatch_color = pr.GREEN
                else:
                    if self.stopwatch_time < 0:
                        self.stopwatch_color = pr.RED

                if self.stopwatch_time < -0.4:
                    self.played_minigames[0] = self.current_minigame.id.value
                    self.current_minigame = None
                    self.transition_tick = -20
                    self.score += 1
                    self.lives_tick = 0
                    pr.set_music_volume(self.resources[ResourceType.MUSIC_BACKGROUND],0.3)
                    if self.score%3==0:
                        self.speed += 0.3
                        self.max_time_multiplier *= 0.9
                    if self.stopwatch_color == pr.RED:
                        self.lives-=1
                        self.lost_a_life = True
                        pr.play_sound(self.resources[ResourceType.SOUND_LOSE])
                    else:
                        pr.play_sound(self.resources[ResourceType.SOUND_WIN])
            
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

            pr.draw_text(self.stopwatch_time_text,50,590,50,self.stopwatch_color)


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
        if self.lives_tick != 91:
            pr.draw_text("Speed up!",528,int(self.speed_up_y),48,pr.YELLOW) # might aswell put this in the lives tick right?
            for i in range(4):
                if i+1 <= self.lives:
                    texture = self.resources[ResourceType.TEXTURE_HEART]
                    used_offset = pr.Vector2(0,0)
                elif i == self.lives and self.lost_a_life:
                    used_offset = self.life_offset
                    if self.lives_tick > 41: 
                        texture = self.resources[ResourceType.TEXTURE_HEART_BROKE]
                    else:
                        texture = self.resources[ResourceType.TEXTURE_HEART]
                elif i+1 > self.lives:
                    used_offset = pr.Vector2(0,0)
                    texture = self.resources[ResourceType.TEXTURE_HEART_BROKE]
                else:
                    texture = self.resources[ResourceType.TEXTURE_HEART_BROKE]
                    used_offset = pr.Vector2(0,0)

                pr.draw_texture_pro(
                    texture,
                    pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_HEART].width,self.resources[ResourceType.TEXTURE_HEART].height),
                    pr.Rectangle(10+used_offset.x+i*160,self.lives_y+used_offset.y,150,138),
                    pr.Vector2(0,0),
                    0,
                    pr.WHITE
                )


        if not self.playing:
            pr.draw_rectangle(0,0,1280,720,pr.Color(30,30,30,150))
            for i in range(6,-1,-1):
                pr.draw_texture_pro(
                    self.resources[ResourceType.TEXTURE_JOBWARE],
                    pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_JOBWARE].width,self.resources[ResourceType.TEXTURE_JOBWARE].height),
                    pr.Rectangle(891,150,self.resources[ResourceType.TEXTURE_JOBWARE].width,self.resources[ResourceType.TEXTURE_JOBWARE].height),
                    pr.Vector2(self.resources[ResourceType.TEXTURE_JOBWARE].width,41),
                    -i*self.title_angle,
                    self.title_colors[i]
                )
            pr.draw_rectangle(int(640-((240*self.play_size)/2)),480,int(240*self.play_size),int(140*self.play_size),pr.BLUE) #Play button
            pr.draw_rectangle_lines_ex(pr.Rectangle(640-((240*self.play_size)/2),480,int(240*self.play_size),int(140*self.play_size)),5,pr.Color(56, 88, 138,255)) 
            pr.draw_text("Play",int(640-((pr.measure_text("Play",int(80*self.play_size)))/2)),510,int(80*self.play_size),pr.GREEN)
            pr.draw_circle(1235,45,39,pr.Color(56, 88, 138,255)) # Credits button
            pr.draw_circle(1235,45,35,pr.BLUE)
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_SCROLL],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_SCROLL].width,self.resources[ResourceType.TEXTURE_SCROLL].height),
                pr.Rectangle(1210,15,48,59),
                pr.Vector2(0,0),
                0,
                pr.WHITE
            )

            if self.game_end_score > 0:
                pr.draw_rectangle(440,260,400,200,pr.BLUE)
                pr.draw_rectangle_lines_ex(pr.Rectangle(440,260,400,200),5,pr.Color(56, 88, 138,255))
                pr.draw_text("Ending Score",470,270,50,pr.WHITE)
                pr.draw_text(str(self.game_end_score),int(640-(pr.measure_text(str(self.game_end_score),40)/2)),330,40,pr.WHITE)
                pr.draw_rectangle(550,385,180,65,pr.GREEN)
                pr.draw_rectangle_lines_ex(pr.Rectangle(550,385,180,65),5,pr.Color(34, 139, 34, 255))
                pr.draw_text("Cool!",604,400,30,pr.WHITE)

            if self.credits:
                pr.draw_rectangle(100,50,1080,660,pr.BLUE)
                pr.draw_rectangle_lines_ex(pr.Rectangle(100,50,1080,660),5,pr.Color(56, 88, 138,255))
                pr.draw_text("Credits:",110,60,32,pr.WHITE)
                for i in range(len(self.credits_txt)):
                    if i>9:
                        pr.draw_text(self.credits_txt[i],130,250+i*15,12,pr.WHITE)
                    else:
                        pr.draw_text(self.credits_txt[i],130,100+i*30,28,pr.WHITE)

    def shutdown(self):
        for key in ResourceType:
            if key.name[:4]=="FONT":
                pr.unload_font(self.resources[key])
            elif key.name[:5]=="SOUND":
                pr.unload_sound(self.resources[key])
            elif key.name[:5]=="MUSIC":
                pr.unload_music_stream(self.resources[key])
            else:
                pr.unload_texture(self.resources[key])

        pr.close_audio_device()
        
    def reset(self):
        self.game_end_score = self.score
        self.lives = 4
        self.score = 0
        self.transition_tick = 0 # max 181, dont edit if you already have a debug minigame set
        self.text_y_tick = 61
        self.door_width = 191
        self.lost_a_life = False
        self.stopwatch_time = 7
        self.text_pos_y = self.screen_height//2
        self.text_size = 250 #40
        self.speed = 1
        self.max_time_multiplier = 1
        self.stopwatch_time_text = "7"
        pr.stop_music_stream(self.resources[ResourceType.MUSIC_BACKGROUND])
        pr.play_music_stream(self.resources[ResourceType.MUSIC_MAIN_MENU])

        self.playing = False