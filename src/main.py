from tetris_game import TetrisGame

import arcade

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Bouncing Rectangle Example"
    
def main():
    window = TetrisGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup(SCREEN_HEIGHT)
    window.set_update_rate(1/2)

    arcade.run()

if __name__ == "__main__":
    main()