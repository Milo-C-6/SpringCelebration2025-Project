import pyray as pr
import asyncio
from game import Game

async def main():

    screen_width = 1280
    screen_height = 720
    
    pr.init_window(screen_width, screen_height, "Spring Celebration 2025 Project")

    current_game = Game(screen_width, screen_height)

    pr.set_target_fps(60)

    current_game.startup()

    while not pr.window_should_close():
        current_game.update()

        pr.begin_drawing()

        pr.clear_background(pr.RAYWHITE)

        current_game.render()

        pr.end_drawing()
        await asyncio.sleep(0)

    pr.close_window()
    current_game.shutdown()


if __name__ == '__main__':
    asyncio.run(main())