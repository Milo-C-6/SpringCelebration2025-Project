import pyray as pr
import random
from minigames.minigame import Minigame
from minigame_ids import MinigameIds
from resource_type import ResourceType

# So far all the stuff that will be consitent with every minigame, but I imagine that will soon enough.

class MgArchaeology(Minigame):
    def __init__(self, resources, screen_width, screen_height, speed, max_time_multiplier):
        super().__init__(resources, screen_width, screen_width, speed, max_time_multiplier)
        self.id = MinigameIds.MGARCHAEOLOGY
        self.instruction = "Dig for artifacts!"
        self.holes_pos = []
        self.artifact_rect = pr.Rectangle(random.randint(211,980),random.randint(405,520),300,200)
        self.win_time = 0
        self.shard_offset_y = 0
        self.sparkle_frames = [10,0]

    def update(self):
        if pr.is_mouse_button_pressed(pr.MOUSE_LEFT_BUTTON) and not self.win and pr.get_mouse_y() > 404:
            pr.play_sound(self.resources[ResourceType.SOUND_DIG])
            self.holes_pos.append(pr.get_mouse_position())
            if pr.check_collision_recs(self.artifact_rect,pr.Rectangle(pr.get_mouse_x(),pr.get_mouse_y(),2,2)):
                self.win = True
                self.win_time = pr.get_time()
        
        if self.win and pr.get_time()-self.win_time>0.4:
            if self.shard_offset_y > -120:
                self.shard_offset_y -= 5
            else:
                for i in range(len(self.sparkle_frames)):
                    self.sparkle_frames[i] += 1
                    if self.sparkle_frames[i] == 20:
                        self.sparkle_frames[i] = 0

    def render(self):
        pr.draw_texture_pro(
            self.resources[ResourceType.TEXTURE_BG_FOREST],
            pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_BG_FOREST].width,self.resources[ResourceType.TEXTURE_BG_FOREST].height),
            pr.Rectangle(0,0,1280,720),
            pr.Vector2(0,0),
            0,
            pr.WHITE
        )
        for i in self.holes_pos:
            pr.draw_texture(self.resources[ResourceType.TEXTURE_HOLE],int(i.x-63.5),int(i.y-24),pr.WHITE)
        pr.draw_texture_ex(
            self.resources[ResourceType.TEXTURE_SHOVEL],
            pr.Vector2(int(pr.get_mouse_x()),int(pr.get_mouse_y()-self.resources[ResourceType.TEXTURE_SHOVEL].height/2)),
            0,
            0.5,
            pr.WHITE
        )
        if self.win:
            pr.draw_texture(self.resources[ResourceType.TEXTURE_POTTERY_SHARD],int(self.holes_pos[-1].x-69),int(self.holes_pos[-1].y-29.5+self.shard_offset_y),pr.WHITE)
            if self.shard_offset_y <= -120:
                for i in range(len(self.sparkle_frames)):
                    if i == 0:
                        x = int(self.holes_pos[-1].x-70)
                        y = int(self.holes_pos[-1].y+self.shard_offset_y-30)
                        size = 48
                    else:
                        x = int(self.holes_pos[-1].x+14)
                        y = int(self.holes_pos[-1].y+self.shard_offset_y+5)
                        size = 24
                    pr.draw_texture_pro(
                        self.resources[ResourceType.TEXTURE_SHEET_SPARKLE],
                        pr.Rectangle(0,0+self.sparkle_frames[i]*24,24,24),
                        pr.Rectangle(x,y,size,size),
                        pr.Vector2(0,0),
                        0,
                        pr.WHITE
                    )
