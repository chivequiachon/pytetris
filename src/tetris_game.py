from grid_board import GridBoard, CollisonType
from shapes import TestShape

import arcade

class TetrisGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self, window_height):
        TETRIS_BOARD_WIDTH = 400
        TETRIS_BOARD_HEIGHT = window_height
        TETRIS_BOARD_START_X = 0
        TETRIS_BOARD_START_Y = 0

        self.tetris_grid_board = GridBoard(
            TETRIS_BOARD_WIDTH,
            TETRIS_BOARD_HEIGHT,
            TETRIS_BOARD_START_X,
            TETRIS_BOARD_START_Y
        )
        self.TETRIS_H_POINTS, self.TETRIS_V_POINTS = \
            self.tetris_grid_board.calculate_grid_points()

        self.t1 = TestShape(1,0)


    def on_draw(self):
        arcade.start_render()

        # Draw tetris grid board
        arcade.draw_lines(self.TETRIS_V_POINTS, arcade.color.BLACK, 1)
        arcade.draw_lines(self.TETRIS_H_POINTS, arcade.color.BLACK, 1)

        # Draw shapes
        self.t1.recalculate_points()
        for point in self.t1.rect_points:
            screen_x, screen_y = \
                self.tetris_grid_board.convert_to_screen_coordinates(point[0], point[1])

            arcade.draw_rectangle_filled(
                screen_x, screen_y,
                self.tetris_grid_board.BOARD_LINE_DIST,
                self.tetris_grid_board.BOARD_LINE_DIST,
                arcade.color.GREEN,
                0
            ) 
            
    def update(self, delta_time):
        self.tetris_grid_board.update_lookup_table(self.t1.rect_points)

        collision_test_result = self.tetris_grid_board.has_collision(self.t1.rect_points)
        if not collision_test_result == CollisonType.DOWN:
            self.t1.fall_down()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.t1.move_right()
            collision_test_result = self.tetris_grid_board.has_collision(self.t1.rect_points)
            if collision_test_result 

    def on_key_release(self, key, modifiers):
        pass


