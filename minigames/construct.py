import pyray as pr
from minigames.minigame import Minigame
from resource_type import ResourceType
from minigame_ids import MinigameIds
# So far all the stuff that will be consitent with every minigame, but I imagine that will soon enough.

class Minigame:
    def __init__(self, resources, screen_width, screen_height, speed, max_time_multiplier):
        self.resources = resources
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = speed
        self.max_time_multiplier = max_time_multiplier
        self.id = MinigameIds.MGCONSTRUCT
        self.win = False
        self.time = 0
        self.max_time = 7*max_time_multiplier
        self.instruction = "Build The House!"
        self.b1 = False
        self.b2 = True

    def update(self):
        pass

    def render(self):
        pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_BGUNDONE],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_BGUNDONE].width,self.resources[ResourceType.TEXTURE_BGUNDONE].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                (0,0),
                0,
                pr.WHITE
            )
        if pr.is_mouse_button_down and self.b1 == False:
            pr.draw_texture_ex(
                self.resources[ResourceType.TEXTURE_BLOCK1],
                pr.vector2_add(pr.get_mouse_position(),pr.Vector2(-250,-300)), #should be changed for scaling! if we still care for that
                0,
                1,
                pr.WHITE
            )
            if pr.is_mouse_button_released(0) and pr.check_collision_recs(pr.Rectangle(pr.get_mouse_position().x,pr.get_mouse_position().y,1,1),pr.Rectangle(340,0,300,300)):
                pr.draw_texture_pro(
                    self.resources[ResourceType.TEXTURE_BLOCK1],
                    pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_BLOCK1].width,self.resources[ResourceType.TEXTURE_BLOCK1].height),
                    pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                    (pr.get_mouse_position().x,pr.get_mouse_position().y),
                    .75,
                    pr.WHITE
                )
                self.b1 = True
                self.b2 = False

        elif not pr.is_mouse_button_down and self.b1 == False:
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_BLOCK1],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_BLOCK1].width,self.resources[ResourceType.TEXTURE_BLOCK1].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                (pr.get_mouse_position().x,pr.get_mouse_position().y),
                0,
                pr.WHITE
            )
        
        if pr.is_mouse_button_down and self.b2 == False:
            pr.draw_texture_ex(
                self.resources[ResourceType.TEXTURE_BLOCK2],
                pr.vector2_add(pr.get_mouse_position(),pr.Vector2(-250,-300)), #should be changed for scaling! if we still care for that
                0,
                1,
                pr.WHITE
            )
            if pr.is_mouse_button_released(0) and pr.check_collision_recs(pr.Rectangle(pr.get_mouse_position().x,pr.get_mouse_position().y,1,1),pr.Rectangle(640,0,300,300)):
                pr.draw_texture_pro(
                    self.resources[ResourceType.TEXTURE_BLOCK2],
                    pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_BLOCK2].width,self.resources[ResourceType.TEXTURE_BLOCK2].height),
                    pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                    (pr.get_mouse_position().x,pr.get_mouse_position().y),
                    .75,
                    pr.WHITE
                )
                self.b2 = True
                self.win = True

        elif not pr.is_mouse_button_down and self.b2 == False:
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_BLOCK2],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_BLOCK2].width,self.resources[ResourceType.TEXTURE_BLOCK2].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                (pr.get_mouse_position().x,pr.get_mouse_position().y),
                0,
                pr.WHITE
            )
        if self.win == True:
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_BGDONE],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_BGDONE].width,self.resources[ResourceType.TEXTURE_BGDONE].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                (0,0),
                0,
                pr.WHITE
            )

