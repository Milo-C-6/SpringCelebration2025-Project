import pyray as pr
from minigames.minigame import Minigame
from resource_type import ResourceType
from minigame_ids import MinigameIds

class MgElectrician(Minigame):
    def __init__(self, resources, screen_width, screen_height, speed, max_time_multiplier):
        super().__init__(resources, screen_width, screen_width, speed, max_time_multiplier)
        #Statics
        self.id = MinigameIds.MGELECTRICIAN
        self.instruction = "Fix issues!"
        #mostly static
        self.width = screen_height
        self.height = screen_height
        #Ticks
        self.win = 0
        self.something_tick = 0
        self.max_time = 14*self.max_time_multiplier
        self.time_tick = 0
        #everything else
        self.plug_opacity = 0
        self.task11 = True
        self.task12 = True
        self.task2 = True
        self.task3 = True
        self.Rbool = False
        self.holding = False
        self.end_scene = False
        self.just_once = True


    def update(self):
        self.something_tick += 1
        if self.something_tick >= 90:
            self.task11 = False
        if self.Rbool:
            self.time_tick += 1


    def render(self):
        ##########Begining Scene
        if self.something_tick <= 90 or self.task2 == True:
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_HOUSE],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_HOUSE].width,self.resources[ResourceType.TEXTURE_HOUSE].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                (0,0),
                0,
                pr.WHITE
            )
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_COMPUTER],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_COMPUTER].width,self.resources[ResourceType.TEXTURE_COMPUTER].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                (0,0),
                0,
                pr.WHITE
            )
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_SCREEN1],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_SCREEN1].width,self.resources[ResourceType.TEXTURE_SCREEN1].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                (-50,-75),
                0,
                pr.WHITE
            )

        #task 1 and 2 of 3
        if self.something_tick >= 90 and self.task11 == False and self.task2 == True:
                pr.draw_texture_pro(
                    self.resources[ResourceType.TEXTURE_WIRE2],
                    pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_WIRE2].width,self.resources[ResourceType.TEXTURE_WIRE2].height),
                    pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                    (-1000,0),
                    0,
                    pr.WHITE
                )
                pr.draw_texture_pro(
                    self.resources[ResourceType.TEXTURE_HOUSE],
                    pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_HOUSE].width,self.resources[ResourceType.TEXTURE_HOUSE].height),
                    pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                    (0,0),
                    0,
                    pr.WHITE
                )
                pr.draw_texture_pro(
                    self.resources[ResourceType.TEXTURE_CONNECT1],
                    pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_CONNECT1].width,self.resources[ResourceType.TEXTURE_CONNECT1].height),
                    pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                    (0,0),
                    0,
                    pr.WHITE
                )

                if pr.check_collision_recs(pr.Rectangle(pr.get_mouse_position().x,pr.get_mouse_position().y,1,1),pr.Rectangle(900,290,40,30)) and self.task11 == False and self.task2 == True:
                    pr.draw_texture_pro(
                        self.resources[ResourceType.TEXTURE_CONNECT2],
                        pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_CONNECT2].width,self.resources[ResourceType.TEXTURE_CONNECT2].height),
                        pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                        (-700,4),
                        0,
                        pr.WHITE
                    )
                    pr.draw_texture_pro(
                        self.resources[ResourceType.TEXTURE_WIRE],
                        pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_WIRE].width,self.resources[ResourceType.TEXTURE_WIRE].height),
                        pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                        (400,0),
                        0,
                        pr.WHITE
                    )
                    self.task11 = True

                if self.task11 == True and self.task2 == True:
                    self.task12 = False
                    pr.draw_texture_pro(
                        self.resources[ResourceType.TEXTURE_CONNECT2],
                        pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_CONNECT2].width,self.resources[ResourceType.TEXTURE_CONNECT2].height),
                        pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                        (-700,4),
                        0,
                        pr.WHITE
                    )
                    pr.draw_texture_pro(
                        self.resources[ResourceType.TEXTURE_WIRE],
                        pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_WIRE].width,self.resources[ResourceType.TEXTURE_WIRE].height),
                        pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                        (400,0),
                        0,
                        pr.WHITE
                    )
                    pr.draw_texture_pro(
                        self.resources[ResourceType.TEXTURE_TAPE],
                        pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_TAPE].width,self.resources[ResourceType.TEXTURE_TAPE].height),
                        pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                        (0,0),
                        0,
                        pr.WHITE
                    )
                    pr.draw_texture_ex(self.resources[ResourceType.TEXTURE_LEFT_CLICK],pr.Vector2(820,115),0,1,pr.WHITE)
                    #action of taping of wire
                    if pr.check_collision_recs(pr.Rectangle(pr.get_mouse_position().x,pr.get_mouse_position().y,1,1),pr.Rectangle(900,290,100,150)) and pr.is_mouse_button_pressed(0) and self.task2 == True:
                        self.task2 = False
                        

                    #player controls
                elif pr.is_mouse_button_down(0) and self.task11 == False and self.task2 == True:
                    pr.draw_texture_ex(
                        self.resources[ResourceType.TEXTURE_CONNECT2],
                        pr.vector2_add(pr.get_mouse_position(),pr.Vector2(-250,-300)), #should be changed for scaling! if we still care for that
                        0,
                        1,
                        pr.WHITE
                    )
                    pr.draw_texture_ex(
                        self.resources[ResourceType.TEXTURE_WIRE],
                        pr.vector2_add(pr.get_mouse_position(),pr.Vector2(-1280,-295)), #should be changed for scaling! if we still care for that
                        0,
                        1,
                        pr.WHITE
                    )
                    #if player is not holding wire
                if not pr.is_mouse_button_down(0) and self.task11 == False and self.task2 == True:
                    pr.draw_texture_pro(
                        self.resources[ResourceType.TEXTURE_CONNECT2],
                        pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_CONNECT2].width,self.resources[ResourceType.TEXTURE_CONNECT2].height),
                        pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                        (0,0),
                        0,
                        pr.WHITE
                    )
                    pr.draw_texture_pro(
                        self.resources[ResourceType.TEXTURE_WIRE],
                        pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_WIRE].width,self.resources[ResourceType.TEXTURE_WIRE].height),
                        pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                        (1000,0),
                        0,
                        pr.WHITE
                    )


                            #####################################################
                            #Task 3 out of 3
                            

                            
        if self.task2 == False:
            self.Rbool = True
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_HOUSE],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_HOUSE].width,self.resources[ResourceType.TEXTURE_HOUSE].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                (0,0),
                0,
                pr.WHITE
            )
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_TAPE_WIRE],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_TAPE_WIRE].width,self.resources[ResourceType.TEXTURE_TAPE_WIRE].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                (0,0),
                0,
                pr.WHITE
            )
            if self.time_tick >= 60:
                pr.draw_texture_pro(
                    self.resources[ResourceType.TEXTURE_HOUSE2],
                    pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_HOUSE2].width,self.resources[ResourceType.TEXTURE_HOUSE2].height),
                    pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                    (0,0),
                    0,
                    pr.WHITE
                )
                
                #player controls
                if pr.is_mouse_button_down(0):
                    self.holding = True
                    pr.draw_texture_ex(
                        self.resources[ResourceType.TEXTURE_WIRE],
                        pr.vector2_add(pr.get_mouse_position(),pr.Vector2(-930,-225)), #should be changed for scaling! if we still care for that
                        1,
                        .75,
                        pr.WHITE
                    )
                    pr.draw_texture_ex(
                        self.resources[ResourceType.TEXTURE_WIRE2],
                        pr.vector2_add(pr.get_mouse_position(),pr.Vector2(-1330,-230)), #should be changed for scaling! if we still care for that
                        1,
                        .75,
                        pr.WHITE
                    )
                    pr.draw_texture_ex(
                        self.resources[ResourceType.TEXTURE_PLUG],
                        pr.vector2_add(pr.get_mouse_position(),pr.Vector2(-500,-250)), #should be changed for scaling! if we still care for that
                        0,
                        .75,
                        pr.WHITE
                    )
                else:
                    self.holding = False
                    
                #if player is not holding wire
                if not pr.is_mouse_button_down(0) and self.holding == False:
                    pr.draw_texture_pro(
                        self.resources[ResourceType.TEXTURE_WIRE],
                        pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_WIRE].width,self.resources[ResourceType.TEXTURE_WIRE].height),
                        pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                        (600,-50),
                        0,
                        pr.WHITE
                    )
                    pr.draw_texture_pro(
                        self.resources[ResourceType.TEXTURE_PLUG],
                        pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_PLUG].width,self.resources[ResourceType.TEXTURE_PLUG].height),
                        pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                        (0,0),
                        0,
                        pr.WHITE
                    )
                if pr.check_collision_recs(pr.Rectangle(pr.get_mouse_position().x,pr.get_mouse_position().y,1,1),pr.Rectangle(1220,170,100,200)) and self.task2 == False:
                    pr.draw_texture_pro(
                        self.resources[ResourceType.TEXTURE_PLUG],
                        pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_PLUG].width,self.resources[ResourceType.TEXTURE_PLUG].height),
                        pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                        (-700,4),
                        .75,
                        pr.WHITE
                    )
                    pr.draw_texture_pro(
                        self.resources[ResourceType.TEXTURE_WIRE],
                        pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_WIRE].width,self.resources[ResourceType.TEXTURE_WIRE].height),
                        pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                        (400,0),
                        .75,
                        pr.WHITE
                    )
                    self.task2 = True
                    self.end_scene = True
        if self.end_scene == True:
            self.win = True
            if self.just_once:
                if self.max_time-(pr.get_time()-self.time) < 1:
                    self.max_time+=1
                self.just_once = False
            if self.something_tick <= 90 or self.task2 == True:
                pr.draw_texture_pro(
                    self.resources[ResourceType.TEXTURE_HOUSE],
                    pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_HOUSE].width,self.resources[ResourceType.TEXTURE_HOUSE].height),
                    pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                    (0,0),
                    0,
                    pr.WHITE
                )
                pr.draw_texture_pro(
                    self.resources[ResourceType.TEXTURE_SCREEN2],
                    pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_SCREEN2].width,self.resources[ResourceType.TEXTURE_SCREEN2].height),
                    pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                    (0,0),
                    0,
                    pr.WHITE
                )
                    


                    
        
            

            
