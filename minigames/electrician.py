import pyray as pr
from minigames.minigame import Minigame
from resource_type import ResourceType
from minigame_ids import MinigameIds

class MgElectrician(Minigame):
    def __init__(self, resources, screen_width, screen_height):
        super().__init__(resources, screen_width, screen_width)
        #Statics
        self.id = MinigameIds.MGELECTRICIAN
        self.distance_x = (self.screen_width//2.45-self.screen_width//2.8)/2
        self.distance_y = (self.screen_width//3.5-self.screen_height//4.1)/2
        #mostly static
        self.width = screen_height
        self.height = screen_height
        self.movement_x = 0
        self.movement_y = 0
        #Ticks
        self.offset_tick = 16
        self.win_tick = 15
        self.win = 0
        self.something_tick = 0
        self.max_time = 14
        self.time_tick = 0
        #everything else
        self.x = screen_height*(-490/720) # a lot of these should be vector2s but I already did so much so whoop
        self.y = screen_height*(-760/720)
        self.offset_y = 0
        self.plug_opacity = 0
        self.task11 = True
        self.task12 = True
        self.task2 = True
        self.task3 = True
        self.Rbool = False
        self.holding = False
        self.end_scene = False


    def update(self):
        self.something_tick += 1
        if self.something_tick >= 90:
            self.task11 = False
        if self.Rbool:
            self.time_tick += 1


    def render(self):
        if self.end_scene == True:
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
                    self.resources[ResourceType.TEXTURE_SCREEN2],
                    pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_SCREEN2].width,self.resources[ResourceType.TEXTURE_SCREEN2].height),
                    pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                    (-50,-75),
                    0,
                    pr.WHITE
                )
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
                    #action of taping of wire
                    if pr.check_collision_recs(pr.Rectangle(pr.get_mouse_position().x,pr.get_mouse_position().y,1,1),pr.Rectangle(900,290,100,100)) and pr.is_mouse_button_pressed(0) and self.task2 == True:
                        self.task2 = False
                        pr.draw_texture_pro(
                            self.resources[ResourceType.TEXTURE_HOUSE],
                            pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_HOUSE].width,self.resources[ResourceType.TEXTURE_HOUSE].height),
                            pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                            (100,0),
                            0,
                            pr.WHITE
                        )
                        pr.draw_texture_pro(
                            self.resources[ResourceType.TEXTURE_TAPE_WIRE],
                            pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_TAPE_WIRE].width,self.resources[ResourceType.TEXTURE_TAPE_WIRE].height),
                            pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                            (100,0),
                            0,
                            pr.WHITE
                        )
                        

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
                (100,0),
                0,
                pr.WHITE
            )
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_TAPE_WIRE],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_TAPE_WIRE].width,self.resources[ResourceType.TEXTURE_TAPE_WIRE].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                (100,0),
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
                        (600,-100),
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
                if pr.check_collision_recs(pr.Rectangle(pr.get_mouse_position().x,pr.get_mouse_position().y,1,1),pr.Rectangle(1130,170,100,100)) and self.task2 == False:
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
                    


                    
        
            

            
