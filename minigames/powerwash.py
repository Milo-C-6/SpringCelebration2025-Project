import pyray as pr
from minigames.minigame import Minigame
from minigames.powerwashClasses.splat import PwSplat
from resource_type import ResourceType
from minigame_ids import MinigameIds

class MgPowerwash(Minigame):
    def __init__(self, resources, screen_width, screen_height):
        super().__init__(resources, screen_width, screen_width)
        self.id = MinigameIds.MGPOWERWASH
        self.instruction = "Clean off the mess!"
        self.splats = [PwSplat(screen_width,screen_height),PwSplat(screen_width,screen_height),PwSplat(screen_width,screen_height),PwSplat(screen_width,screen_height)]
        self.sparkle_rectangle = pr.Rectangle(0,0,480,480)
        self.sparkle_pos = [pr.Vector2(406, 594),pr.Vector2(449, 348),pr.Vector2(265, 338),pr.Vector2(142, 240),pr.Vector2(505, 47),pr.Vector2(667, 296),pr.Vector2(705, 396),pr.Vector2(1068, 229),pr.Vector2(1019, 101),pr.Vector2(945, 520),pr.Vector2(1004, 530),pr.Vector2(1121, 648),pr.Vector2(401, 592),pr.Vector2(257, 636),pr.Vector2(132, 493)]
        self.sparkle_frames = [0,14,3,9,4,17,8,0,19,10,11,15,4,2,1]
        self.max_time = 5

    def update(self):
        if pr.is_mouse_button_down(0):
            mouse_pos = pr.vector2_add(pr.get_mouse_position(),pr.Vector2(-10,-10))

            for splat in self.splats:
                collide = pr.check_collision_recs(
                    pr.Rectangle(
                        mouse_pos.x,
                        mouse_pos.y,
                        30,
                        30
                    ),
                    pr.Rectangle(
                        splat.position.x,
                        splat.position.y,
                        self.resources[splat.texture].width*splat.size,
                        self.resources[splat.texture].height*splat.size
                    )
                )
                if collide: 
                    splat.alpha -=0.05
                    splat.color = pr.color_alpha(splat.color,splat.alpha)
                    if splat.alpha <= 0:
                        self.splats.remove(splat)
        for i in range(len(self.sparkle_frames)):
            self.sparkle_frames[i] += 1
            if self.sparkle_frames[i] == 20:
                self.sparkle_frames[i] = 0
        
        if len(self.splats)==0:
            self.win = True

    def render(self):
        pr.draw_texture_pro(
            self.resources[ResourceType.TEXTURE_SIDEWALK],
            pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_SIDEWALK].width,self.resources[ResourceType.TEXTURE_SIDEWALK].height),
            pr.Rectangle(0,0,self.screen_width,self.screen_height),
            (0,0),
            0,
            pr.WHITE
        )

        for splat in self.splats:
            pr.draw_texture_ex(
                self.resources[splat.texture],
                splat.position,
                0,
                splat.size,
                splat.color
            )
            pr.draw_rectangle_lines_ex(
                pr.Rectangle(
                    splat.position.x,splat.position.y,
                    self.resources[splat.texture].width*splat.size,self.resources[splat.texture].height*splat.size
                ),
                1,
                pr.YELLOW
            )

        pr.draw_texture_ex(
            self.resources[ResourceType.TEXTURE_POWERWASH_GUN],
            pr.vector2_add(pr.get_mouse_position(),pr.Vector2(40,40)), #should be changed for scaling! if we still care for that
            0,
            0.5,
            pr.WHITE
        )

        if pr.is_mouse_button_down(0):
            pr.draw_triangle(
                pr.vector2_add(pr.get_mouse_position(),pr.Vector2(40,40)),
                pr.vector2_add(pr.get_mouse_position(),pr.Vector2(10,-10)),
                pr.vector2_add(pr.get_mouse_position(),pr.Vector2(-10,10)),
                pr.BLUE
            )

        if self.win:
            for i in range(len(self.sparkle_pos)):
                pr.draw_texture_pro(
                    self.resources[ResourceType.TEXTURE_SHEET_SPARKLE],
                    pr.Rectangle(0,self.sparkle_frames[i]*24,self.resources[ResourceType.TEXTURE_SHEET_SPARKLE].width,24),
                    pr.Rectangle(self.sparkle_pos[i].x,self.sparkle_pos[i].y,48,48),
                    pr.Vector2(0,0),
                    0,
                    pr.WHITE
                )