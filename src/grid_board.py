from enum import Enum, auto

class CollisonType(Enum):
    NONE = 0
    LEFT = auto()
    RIGHT = auto()
    DOWN = auto()


class GridBoard():
    def __init__(self, width, height, start_x, start_y):
        self.BOARD_WIDTH = width
        self.BOARD_HEIGHT = height
        self.BOARD_START_X = start_x # In screen coordinates
        self.BOARD_START_Y = start_y # In screen coordinates
        self.BOARD_LINE_DIST = 20
        self.board_lookup_table = None

    def calculate_grid_points(self):
        points_vertical_lines = []
        points_horizontal_lines = []

        width_board_coord = 0
        for x in range(self.BOARD_START_X, self.BOARD_WIDTH + 1, self.BOARD_LINE_DIST):
            width_board_coord += 1
            points_vertical_lines.append((x, 0))
            points_vertical_lines.append((x, self.BOARD_HEIGHT))

        height_board_coord = 0
        for y in range(self.BOARD_START_Y, self.BOARD_HEIGHT, self.BOARD_LINE_DIST):
            height_board_coord += 1
            points_horizontal_lines.append((0, y))
            points_horizontal_lines.append((self.BOARD_WIDTH, y))

        self.LOOKUP_TABLE_MAX_X = width_board_coord
        self.LOOKUP_TABLE_MAX_Y = height_board_coord
        self.board_lookup_table = [[False] * width_board_coord for i in range(height_board_coord)]

        return points_vertical_lines, points_horizontal_lines

    def convert_to_screen_coordinates(self, board_x, board_y):
        # Get x screen coordinate
        screen_x = self.BOARD_START_X + (board_x * self.BOARD_LINE_DIST) + (self.BOARD_LINE_DIST / 2)
        screen_y = self.BOARD_START_Y + self.BOARD_HEIGHT - (board_y * self.BOARD_LINE_DIST) - (self.BOARD_LINE_DIST / 2)

        # Return screen x, screen y
        return screen_x, screen_y

    def convert_to_board_coordinates(self, screen_x, screen_y):
        board_x = int((screen_x - self.BOARD_START_X - (self.BOARD_LINE_DIST / 2)) / self.BOARD_LINE_DIST)
        board_y = int(-((screen_y - self.BOARD_START_Y - self.BOARD_HEIGHT + (self.BOARD_LINE_DIST / 2)) / self.BOARD_LINE_DIST))

        return board_x, board_y

    def update_lookup_table(self, point_list):
        for point in point_list:
            board_x, board_y = self.convert_to_board_coordinates(point[0], point[1])
            self.board_lookup_table[board_y][board_x] = True

    def has_right_collision(self, board_x, board_y):
        result = CollisonType.NONE
        if board_x >= self.LOOKUP_TABLE_MAX_X  - 1:
            result = CollisonType.RIGHT

        return result

    def has_bottom_collision(self, board_x, board_y):
        result = CollisonType.NONE
        if board_y >= self.LOOKUP_TABLE_MAX_Y - 1 or \
            self.board_lookup_table[board_y][board_x] is True:
            result = CollisonType.DOWN

        return result

    def has_left_collision(self, board_x, board_y):
        result = CollisonType.NONE
        if board_x <= 0:
            result = CollisonType.LEFT

        return result
        

    def has_collision(self, point_list): # Board coordinates
        result = CollisonType.NONE

        for point in point_list:
            board_x, board_y = point[0], point[1]
            result = self.has_bottom_collision(board_x, board_y) | \
                     self.has_left_collision(board_x, board_y) | \
                     self.has_right_collision(board_x, board_y)

        return result
