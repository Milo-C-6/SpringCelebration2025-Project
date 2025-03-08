import pyray as pr
from minigames.minigame import Minigame
from resource_type import ResourceType

class MgElectrician(Minigame):
    def __init__(self, resources, screen_width, screen_height):
        super().__init__(resources, screen_width, screen_width)
        #Statics
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
        #everything else
        self.x = screen_height*(-490/720) # a lot of these should be vector2s but I already did so much so whoop
        self.y = screen_height*(-760/720)
        self.offset_y = 0
        self.plug_opacity = 0
        self.task1 = True
        self.task2 = True

    def render(self):
        if self.something_tick <= 120 or self.task2 == True:
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
        elif self.something_tick >= 120 and self.task1 == False:
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_HOUSE],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_HOUSE].width,self.resources[ResourceType.TEXTURE_HOUSE].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                (0,0),
                0,
                pr.WHITE
            )
            #make it a moveable object{
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_CONNECT1],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_CONNECT1].width,self.resources[ResourceType.TEXTURE_CONNECT1].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                (0,3),
                0,
                pr.WHITE
            )
            #}
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_CONNECT2],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_CONNECT2].width,self.resources[ResourceType.TEXTURE_CONNECT2].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                (0,3),
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
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_WIRE2],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_WIRE2].width,self.resources[ResourceType.TEXTURE_WIRE2].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                (-1000,0),
                0,
                pr.WHITE
            )
        pass

    def update(self):
        self.something_tick += 1
        if self.something_tick >= 120:
            self.task1 = False
        if self.task1 == True:
            self.task2 = False
        if self.offset_tick != 16:
            self.offset_tick +=1
            self.offset_y+=3
            return
        if self.win:
            if self.win_tick != 15:
                self.win_tick += 1
                self.x += self.movement_x
                self.y += self.movement_y
                if self.win_tick == 1:
                    self.offset_y = 0
                    # self.x = self.screen_width/2-self.width/2
                    # self.y = self.screen_height/2-self.height
        pass

