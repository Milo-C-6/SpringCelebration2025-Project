import pyray as pr
from minigames.minigame import Minigame
from resource_type import ResourceType

# Minigame Sewing, i love spending 5+ hours on one minigame, and the code ends up being super speghetti
class MgSewing(Minigame):
    def __init__(self, resources, screen_width, screen_height):
        super().__init__(resources, screen_width, screen_width)
        #Statics
        self.distance_x = (self.screen_width//2.45-self.screen_width//2.8)/2
        self.distance_y = (self.screen_width//3.5-self.screen_height//4.1)/2
        #mostly static
        self.width = screen_height * 2
        self.height = screen_height * 2
        self.current_doll = resources[ResourceType.TEXTURE_SEW_DOLL]
        self.movement_x = 0
        self.movement_y = 0
        #Ticks
        self.stich_tick = 29
        self.offset_tick = 16
        self.win_tick = 15
        self.win = 0
        #everything else
        self.x = screen_height*(-490/720) # a lot of these should be vector2s but I already did so much so whoop
        self.y = screen_height*(-760/720)
        self.offset_y = 0
        self.stich_line_y = self.screen_width//3.5
        self.stich_end_x = self.screen_width//2.8
        self.stich_end_y = self.screen_height//4.1
        self.stiches = 0
        self.current_instruction = self.resources[ResourceType.TEXTURE_KEY_RIGHT]
        self.side = 0 # 0: Front, 1: Back
        self.direction = 0 # 0: Right, 1: Left
        self.starburst_opacity = 0

    def render(self):
        if self.side == 1:
            pr.draw_line_ex(pr.Vector2(int(self.screen_width//2.45),int(self.stich_line_y)),pr.Vector2(int(self.stich_end_x),int(self.stich_end_y)),self.screen_height*(6/720),pr.RED)

        if self.win:
            pr.clear_background(pr.Color(255,191,0,self.starburst_opacity))
            pr.draw_texture_pro(
                self.resources[ResourceType.TEXTURE_STARBURST_EXPLOSION],
                pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_STARBURST_EXPLOSION].width,self.resources[ResourceType.TEXTURE_STARBURST_EXPLOSION].height),
                pr.Rectangle(self.x-self.screen_height/6,self.y-self.screen_height/6,self.width+self.screen_height/4,self.height+self.screen_height/4),
                pr.Vector2(self.resources[ResourceType.TEXTURE_STARBURST_EXPLOSION].width // 4, self.resources[ResourceType.TEXTURE_STARBURST_EXPLOSION].height // 4),
                0,
                pr.Color(255,255,255,self.starburst_opacity)
            )

        pr.draw_texture_pro(
            self.current_doll,
            pr.Rectangle(0,0,self.current_doll.width,self.current_doll.height),
            pr.Rectangle(self.x,self.y+self.offset_y,self.width,self.height),
            pr.Vector2(self.current_doll.width // 4, self.current_doll.height // 4),
            0,
            pr.WHITE
        )
        if self.win:
            return

        pr.draw_texture_pro(
            self.current_instruction, 
            pr.Rectangle(0,0,self.current_instruction.width,self.current_instruction.height),
            pr.Rectangle(int(self.screen_width//1.2),int(self.screen_height//5),self.screen_width//5.5,self.screen_width//5.5),
            pr.Vector2(self.current_instruction.width // 4, self.current_instruction.height // 4),
            0,
            pr.WHITE
        )
        if self.side == 0:
            pr.draw_line_ex(pr.Vector2(int(self.screen_width//2.45),int(self.stich_line_y)),pr.Vector2(int(self.stich_end_x),int(self.stich_end_y)),self.screen_height*(6/720),pr.RED)

        #these stupid stiches were such a pain to make
        if self.stiches > 0:
            for i in range(0,self.stiches,2):
                start_y = self.screen_width//3.5+self.offset_y-i*48
                end_y = self.screen_height//4.1+self.offset_y-i*48

                pr.draw_line_ex(pr.Vector2(int(self.screen_width//2.45),int(start_y)),pr.Vector2(int(self.screen_width//2.45),int(end_y)),self.screen_height*(6/720),pr.RED)

    def update(self):
        if self.stich_tick != 29:
            self.stich_tick+=1
            if self.stich_tick%7==0:
                if self.direction == 0: self.stich_end_x += self.distance_x
                else: self.stich_end_x -= self.distance_x

                if self.stich_tick==14:
                    self.stiches +=1
                    if self.side == 0:
                        self.side = 1
                    else: self.side = 0
                    self.stich_line_y = self.screen_height//4.1
                
                if self.stich_tick==28:
                    self.offset_tick = 0
            return
        if self.offset_tick != 16:
            self.offset_tick +=1
            self.offset_y+=3
            self.stich_line_y=self.screen_height//4.1+self.offset_tick*3
            return
        if self.win:
            if self.win_tick != 15:
                self.win_tick += 1
                self.starburst_opacity+=17
                self.x += self.movement_x
                self.y += self.movement_y
                if self.win_tick == 1:
                    self.offset_y = 0
                    # self.x = self.screen_width/2-self.width/2
                    # self.y = self.screen_height/2-self.height
            return
        if self.stiches==9:
            self.win = True
            self.win_tick = 0
            self.resources[ResourceType.TEXTURE_SEW_DOLL_COMPLETE]
            self.side = 3 # stops the line from drawing(bro wont see it coming)
            self.width = self.screen_height / 2.5
            self.height = self.screen_height / 2.5
            self.movement_x = ((self.screen_width/2-self.width/2)-self.x)/15
            self.movement_y = ((self.screen_height/2-self.height/2)-self.y)/18 # this is such a horrible fix
            return

        if pr.is_key_pressed(pr.KEY_RIGHT) and self.current_instruction == self.resources[ResourceType.TEXTURE_KEY_RIGHT]:
            self.direction = 0
            self.stich_tick = 1
            self.current_instruction = self.resources[ResourceType.TEXTURE_KEY_LEFT]
        elif pr.is_key_down(pr.KEY_LEFT) and self.current_instruction == self.resources[ResourceType.TEXTURE_KEY_LEFT]:
            self.direction = 1
            self.stich_tick = 1
            self.current_instruction = self.resources[ResourceType.TEXTURE_KEY_RIGHT]