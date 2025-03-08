import pyray as pr
from minigames.minigame import Minigame
from minigames.powerwashClasses.splat import PwSplat
from resource_type import ResourceType

class MgPowerwash(Minigame):
    def __init__(self, resources, screen_width, screen_height):
        super().__init__(resources, screen_width, screen_width)
        self.splats = [PwSplat(screen_width,screen_height),PwSplat(screen_width,screen_height),PwSplat(screen_width,screen_height),PwSplat(screen_width,screen_height)]
        self.sparkle_rectangle = pr.Rectangle(0,0,480,480)
        self.sparkle_tick = 29

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
        if self.sparkle_tick!=29:
            offset_y = 0
            if self.sparkle_tick>5: offset_y=480 #probably a way better way to do this, but i dont know!!!
            if self.sparkle_tick>10: offset_y=960
            if self.sparkle_tick>15: offset_y=1440
            if self.sparkle_tick>20: offset_y=1920
            if self.sparkle_tick>25: offset_y=2400
            self.sparkle_rectangle = pr.Rectangle(
                self.sparkle_tick%6*480,
                offset_y,
                480,480
            )
            self.sparkle_tick+=1
            return
        if len(self.splats)==0:
            self.sparkle_tick = 0
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
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_SHEET_SPARKLE],
                self.sparkle_rectangle,
                pr.Rectangle(0,0,self.screen_width,self.screen_height),
                pr.Vector2(0,0),
                0,
                pr.WHITE
            )