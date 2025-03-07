import pyray as pr
from minigames.minigame import Minigame
from resource_type import ResourceType

# Minigame Sewing
class MgSewing(Minigame):
    def __init__(self, resources, screen_width, screen_height):
        super().__init__(resources, screen_width, screen_width)
        self.width = int(screen_height * 2)
        self.height = int(screen_height * 2)
        # Values for the sewing item, didn't really feel like putting it in its own class since there will likely only ever be one sewing item for the sewing minigame.
        self.x = -490
        self.y = -760
        self.stich_line_y = self.screen_width//3.5
        self.stiches = 0
        self.current_instruction = self.resources[ResourceType.TEXTURE_KEY_UP]

    def render(self):
        pr.draw_texture_pro(
            self.resources[ResourceType.TEXTURE_SEW_DOLL],
            pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_SEW_DOLL].width,self.resources[ResourceType.TEXTURE_SEW_DOLL].height),
            pr.Rectangle(self.x,self.y,self.width,self.height),
            pr.Vector2(self.resources[ResourceType.TEXTURE_SEW_DOLL].width // 4, self.resources[ResourceType.TEXTURE_SEW_DOLL].height // 4),
            0,
            pr.WHITE
        )
        pr.draw_texture_pro(
            self.current_instruction, 
            pr.Rectangle(0,0,self.current_instruction.width,self.current_instruction.height),
            pr.Rectangle(int(self.screen_width//1.2),int(self.screen_height//5),self.screen_width//5.5,self.screen_width//5.5),
            pr.Vector2(self.current_instruction.width // 4, self.current_instruction.height // 4),
            0,
            pr.WHITE
        )
        pr.draw_line_ex(pr.Vector2(int(self.screen_width//2.45),int(self.stich_line_y)),pr.Vector2(int(self.screen_width//2.8),int(self.screen_height//4.1)),self.screen_height*(6/720),pr.RED)

    def update(self):
        if self.stich_line_y >= self.screen_height*0.64: 
            self.current_instruction = self.resources[ResourceType.TEXTURE_KEY_DOWN]
        if pr.is_key_pressed(pr.KEY_DOWN) and self.current_instruction == self.resources[ResourceType.TEXTURE_KEY_DOWN]:
            self.y-=1
            self.stich_line_y-=1
        elif pr.is_key_down(pr.KEY_UP) and self.current_instruction == self.resources[ResourceType.TEXTURE_KEY_UP]:
            self.y+=1
            self.stich_line_y+=1