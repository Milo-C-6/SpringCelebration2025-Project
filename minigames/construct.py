import pyray as pr
from minigames.minigame import Minigame
from resource_type import ResourceType
from minigame_ids import MinigameIds
# So far all the stuff that will be consitent with every minigame, but I imagine that will soon enough.
#gm
class MgConstruct(Minigame):
    def __init__(self, resources, screen_width, screen_height, speed, max_time_multiplier):
        super().__init__(resources, screen_width, screen_width, speed, max_time_multiplier)
        self.id = MinigameIds.MGCONSTRUCT
        self.max_time = 7*max_time_multiplier
        self.instruction = "Build The House!"
        self.b1 = False
        self.b2 = True
        self.bp1 = False
        self.bp2 = False
        self.something_tick = 0
        self.time_new_tick = 0
        self.wait_tick = 0

    def update(self):
        self.something_tick += 1
        if self.bp2 == True:
            self.time_new_tick += 1
        if self.b1 == True:
            self.wait_tick += 1

    def render(self):
        pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_BGUNDONE],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_BGUNDONE].width,self.resources[ResourceType.TEXTURE_BGUNDONE].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                (0,0),
                0,
                pr.WHITE
            )
        if pr.is_mouse_button_down(pr.MOUSE_LEFT_BUTTON) and self.b1 == False:
            pr.draw_texture_ex(
                self.resources[ResourceType.TEXTURE_BLOCK1],
                pr.vector2_add(pr.get_mouse_position(),pr.Vector2(-1200,-300)), #should be changed for scaling! if we still care for that
                0,
                1,
                pr.WHITE
            )
            if pr.check_collision_recs(pr.Rectangle(pr.get_mouse_position().x,pr.get_mouse_position().y,1,1),pr.Rectangle(340,0,300,300)):
                self.b1 = True
                self.b2 = False
                self.bp1 = True

        if self.bp1 == True:
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_BLOCK1],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_BLOCK1].width,self.resources[ResourceType.TEXTURE_BLOCK1].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/2),
                (540,160),
                1,
                pr.WHITE
            )

        elif not pr.is_mouse_button_down(pr.MOUSE_LEFT_BUTTON) and self.b1 == False:
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_BLOCK1],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_BLOCK1].width,self.resources[ResourceType.TEXTURE_BLOCK1].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                (0,0),
                0,
                pr.WHITE
            )
            ###SECOND BLOCK###
        if pr.is_mouse_button_down(pr.MOUSE_LEFT_BUTTON) and self.b2 == False and self.wait_tick >= 45:
            pr.draw_texture_ex(
                self.resources[ResourceType.TEXTURE_BLOCK2],
                pr.vector2_add(pr.get_mouse_position(),pr.Vector2(-300,-300)), #should be changed for scaling! if we still care for that
                0,
                1,
                pr.WHITE
            )
            if pr.check_collision_recs(pr.Rectangle(pr.get_mouse_position().x,pr.get_mouse_position().y,1,1),pr.Rectangle(640,0,300,300)):
                self.bp2 = True
                self.b2 = True
                self.win = True

        elif not pr.is_mouse_button_down(pr.MOUSE_LEFT_BUTTON) and self.b2 == False:
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_BLOCK2],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_BLOCK2].width,self.resources[ResourceType.TEXTURE_BLOCK2].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/2),
                (0,0),
                0,
                pr.WHITE
            )
        if self.bp2 == True:
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_BLOCK2],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_BLOCK2].width,self.resources[ResourceType.TEXTURE_BLOCK2].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                (-500,210),
                1,
                pr.WHITE
            )
            for i in range(-1,1): # Efficiency!
                pr.draw_texture_pro(
                    self.resources[ResourceType.TEXTURE_DUST],
                    pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_DUST].width,self.resources[ResourceType.TEXTURE_DUST].height),
                    pr.Rectangle(0,0,self.screen_width*i,self.screen_height/1.75),
                    (0,0),
                    1,
                    pr.WHITE
                )
        
        if self.win and self.time_new_tick >= 60:
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_BGDONE],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_BGDONE].width,self.resources[ResourceType.TEXTURE_BGDONE].height),
                pr.Rectangle(0,0,self.screen_width,self.screen_height/1.75),
                (0,0),
                0,
                pr.WHITE
            )
        

