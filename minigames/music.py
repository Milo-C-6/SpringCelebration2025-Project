import pyray as pr
from resource_type import ResourceType
from minigame_ids import MinigameIds
from minigames.minigame import Minigame

class MgMusic(Minigame):
    def __init__(self, resources, screen_width, screen_height, speed, max_time_multiplier):
        super().__init__(resources,screen_width,screen_height, speed, max_time_multiplier)
        #Statics
        self.id = MinigameIds.MGMUSIC
        self.controls = [self.resources[ResourceType.TEXTURE_KEY_LEFT],self.resources[ResourceType.TEXTURE_KEY_DOWN],self.resources[ResourceType.TEXTURE_KEY_UP],self.resources[ResourceType.TEXTURE_KEY_RIGHT],self.resources[ResourceType.TEXTURE_KEY_D],self.resources[ResourceType.TEXTURE_KEY_F],self.resources[ResourceType.TEXTURE_KEY_J],self.resources[ResourceType.TEXTURE_KEY_K]]
        self.instruction = "Play the riff!"
        #Not Statics
        self.notes = 1 # max 9
        self.note_sequence = [0,1,0,2,4,2,0,1,0]
        self.lost = False
        self.bg_color = pr.WHITE
        self.rainbow = pr.load_render_texture(1280,720)
        self.rainbow_ys = [-103,0,103,206,309,412,515,618]

    def update(self):
        if pr.is_key_pressed(pr.KEY_LEFT) or pr.is_key_pressed(pr.KEY_D):
            match self.notes:
                case 1 | 3 | 7:
                    self.bg_color = pr.PURPLE
                    self.note_sequence.pop(0)
                    pr.play_sound(self.resources[ResourceType.SOUND_GUITAR_1])
                    
                    self.notes += 1
                case 9:
                    pr.play_sound(self.resources[ResourceType.SOUND_GUITAR_9])
                    self.win = True
                case _:
                    self.lose()
        elif pr.is_key_pressed(pr.KEY_DOWN) or pr.is_key_pressed(pr.KEY_F):
            match self.notes:
                case 2 | 8:
                    self.bg_color = pr.BLUE
                    self.note_sequence.pop(0)
                    if self.notes == 2: pr.play_sound(self.resources[ResourceType.SOUND_GUITAR_2])
                    else: pr.play_sound(self.resources[ResourceType.SOUND_GUITAR_8])

                    self.notes += 1
                case _:
                    self.lose()
        elif pr.is_key_pressed(pr.KEY_UP) or pr.is_key_pressed(pr.KEY_J):
            match self.notes:
                case 4 | 6:
                    self.bg_color = pr.YELLOW
                    self.note_sequence.pop(0)
                    pr.play_sound(self.resources[ResourceType.SOUND_GUITAR_4])
                    self.notes += 1
                case _:
                    self.lose()
        elif pr.is_key_pressed(pr.KEY_RIGHT) or pr.is_key_pressed(pr.KEY_K):
            if self.notes == 5:
                self.bg_color = pr.Color(64, 224, 208,255)
                self.note_sequence.pop(0)
                pr.play_sound(self.resources[ResourceType.SOUND_GUITAR_5])
                self.notes += 1
            else:
                self.lose()
        if self.win:
            pr.begin_texture_mode(self.rainbow)
            pr.draw_rectangle_gradient_v(0,self.rainbow_ys[0],1280,103,pr.Color(255,79,226,255),pr.RED)
            pr.draw_rectangle_gradient_v(0,self.rainbow_ys[1],1280,103,pr.RED,pr.ORANGE)
            pr.draw_rectangle_gradient_v(0,self.rainbow_ys[2],1280,103,pr.ORANGE,pr.YELLOW)
            pr.draw_rectangle_gradient_v(0,self.rainbow_ys[3],1280,103,pr.YELLOW,pr.Color(132,253,129,255))
            pr.draw_rectangle_gradient_v(0,self.rainbow_ys[4],1280,103,pr.Color(132,253,129,255),pr.Color(0,251,255,255))
            pr.draw_rectangle_gradient_v(0,self.rainbow_ys[5],1280,103,pr.Color(0,251,255,255),pr.Color(0,16,255,255))
            pr.draw_rectangle_gradient_v(0,self.rainbow_ys[6],1280,103,pr.Color(0,16,255,255),pr.PURPLE)
            pr.draw_rectangle_gradient_v(0,self.rainbow_ys[7],1280,103,pr.PURPLE,pr.Color(255,79,226,255))
            pr.end_texture_mode()
            for i in range(len(self.rainbow_ys)):
                self.rainbow_ys[i]+=3
                if self.rainbow_ys[i]>720:
                    self.rainbow_ys[i]=-103

    def render(self):
        # Draw Background
        if self.win:
            pr.draw_texture(self.rainbow.texture,0,0,pr.WHITE)
        else:
            pr.draw_rectangle(0,0,self.screen_width,self.screen_height,self.bg_color)
        pr.draw_texture_pro(
            self.resources[ResourceType.TEXTURE_SHEET_MUSIC_TRANSPARENT],
            pr.Rectangle(0,0,self.resources[ResourceType.TEXTURE_SHEET_MUSIC_TRANSPARENT].width,self.resources[ResourceType.TEXTURE_SHEET_MUSIC_TRANSPARENT].height),
            pr.Rectangle(0,0,self.screen_width,self.screen_height),
            pr.Vector2(0,0),
            0,
            pr.WHITE
        )
        # Draw the guitar neck
        pr.draw_rectangle(600,200,600,300,pr.Color(158,100,41,255))
        pr.draw_circle(780,350,20,pr.BLACK)
        pr.draw_circle(1020,350,20,pr.BLACK)
        for i in range(6): # Frets
            pr.draw_line_ex(
                pr.Vector2(600+i*120,190),
                pr.Vector2(600+i*120,510),
                5,
                pr.Color(218,165,32,255)
            )
        for i in range(6): # Strings
            pr.draw_line_ex(
                pr.Vector2(590,200+i*60),
                pr.Vector2(1210,200+i*60),
                5,
                pr.Color(238,238,238,255)
            )
        #Controls for Guitar neck
        for i in range(8):
            y_offset = 0
            x_offset = i
            if i > 3:
                x_offset -= 4
                y_offset = 100
            if i == 3 or i == 7:
                x_offset = 4
            pr.draw_texture_ex(
                self.controls[i],
                pr.Vector2(600+x_offset*125,510+y_offset),
                0,
                1,
                pr.WHITE
            )
        #Falling notes
        if not self.win:
            for i in range(4):
                try:
                    x_offset = self.note_sequence[i]
                except IndexError:
                    break
                pr.draw_rectangle(600+x_offset*125,155+i*-40,125,37,pr.RED)
    
    def lose(self):
        pr.play_sound(self.resources[ResourceType.SOUND_GUITAR_FAIL])
        self.lost = True
        self.bg_color = pr.RED
        self.notes = 10 # bro wont see it coming part 2