import pyray as pr
from resource_type import ResourceType
from minigame_ids import MinigameIds
from minigames.minigame import Minigame

class MgSolder(Minigame):
    def __init__(self, resources, screen_width, screen_height):
        super().__init__(resources, screen_width, screen_width)
        #Static
        self.id = MinigameIds.MGSOLDER
        self.max_time = 5
        self.instruction = "Bind the wire and the PCB with solder!"
        #Not static
        self.led_texutre = self.resources[ResourceType.TEXTURE_LED_OFF]
        self.iron_distance = pr.Vector2(0,-300)
        self.solder_distance = pr.Vector2(-136,-87)
        self.top_solder_radius = 0 # 9.8-15.5
        self.bottom_solder_radius = 0 # 9.7-15.5
        self.top_texture = self.resources[ResourceType.TEXTURE_IMPORTANT]
        self.bottom_texture = self.resources[ResourceType.TEXTURE_IMPORTANT]
    
    def update(self):
        if pr.is_mouse_button_down(pr.MOUSE_LEFT_BUTTON):
            self.iron_distance = pr.Vector2(-3,-297)
            self.solder_distance = pr.Vector2(-133,-80)
            if pr.check_collision_circles(
                pr.get_mouse_position(),3,pr.Vector2(599,431), 10
            ): self.top_solder_radius += 0.2
            elif pr.check_collision_circles(
                pr.get_mouse_position(),3,pr.Vector2(599,582), 10
            ): self.bottom_solder_radius += 0.2

        else:
            if self.top_solder_radius >= 9.8 and self.top_solder_radius <= 15.5:
                self.top_texture = self.resources[ResourceType.TEXTURE_CHECK]
            elif self.top_solder_radius > 15.5:
                self.top_texture = self.resources[ResourceType.TEXTURE_WRONG]
            if self.bottom_solder_radius >= 9.7 and self.bottom_solder_radius <= 16:
                self.bottom_texture = self.resources[ResourceType.TEXTURE_CHECK]
            elif self.bottom_solder_radius > 16:
                self.bottom_texture = self.resources[ResourceType.TEXTURE_WRONG]

            self.iron_distance = pr.Vector2(0,-300)
            self.solder_distance = pr.Vector2(-136,-87)
        
        if self.top_solder_radius >= 9.8 and self.top_solder_radius <= 15.5 and self.bottom_solder_radius >= 9.7 and self.bottom_solder_radius <= 15.5:
            self.led_texutre = self.resources[ResourceType.TEXTURE_LED_ON]
            self.win = True
        else:
            self.led_texutre = self.resources[ResourceType.TEXTURE_LED_OFF]

    def render(self):
        pr.draw_texture_pro(
            self.resources[ResourceType.TEXTURE_TABLE_BG],
            pr.Rectangle(0,0,1280,720),
            pr.Rectangle(0,0,1280,720),
            pr.Vector2(0,0),
            0,
            pr.WHITE
        )
        pr.draw_texture_ex(
            self.resources[ResourceType.TEXTURE_PCB],
            pr.Vector2(400,200),
            0,
            1,
            pr.WHITE
        )
        pr.draw_texture_ex(
            self.resources[ResourceType.TEXTURE_SOLDER_IRON],
            pr.vector2_add(pr.get_mouse_position(),self.iron_distance),
            0,
            0.75,
            pr.WHITE
        )
        pr.draw_texture_ex(
            self.resources[ResourceType.TEXTURE_SOLDER],
            pr.vector2_add(pr.get_mouse_position(),self.solder_distance),
            0,
            0.75,
            pr.WHITE
        )
        pr.draw_texture_ex(
            self.led_texutre,
            pr.Vector2(800,200),
            0,
            0.75,
            pr.WHITE
        )
        pr.draw_line_bezier(pr.Vector2(599,431),pr.Vector2(929,399),5,pr.RED)
        pr.draw_line_bezier(pr.Vector2(599,582),pr.Vector2(956,405),5,pr.BLACK)
        pr.draw_circle(599,431,self.top_solder_radius, pr.GRAY)
        pr.draw_circle(599,582,self.bottom_solder_radius, pr.GRAY)

        if not pr.is_mouse_button_down(pr.MOUSE_LEFT_BUTTON):
            pr.draw_texture_ex(
                self.resources[ResourceType.TEXTURE_LEFT_CLICK],
                pr.Vector2(640,209),
                0,
                1,
                pr.WHITE
            )
            pr.draw_texture_ex(
                self.top_texture,
                pr.Vector2(630,321),
                0,
                0.25,
                pr.WHITE
                )
            pr.draw_texture_ex(
                self.bottom_texture,
                pr.Vector2(630,472),
                0,
                0.25,
                pr.WHITE
                )