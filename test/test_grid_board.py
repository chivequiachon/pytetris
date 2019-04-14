from src import grid_board, shapes

import pytest

@pytest.fixture()
def grid_board_resource():
    print("setup")

    TETRIS_BOARD_WIDTH = 400
    TETRIS_BOARD_HEIGHT = 600
    TETRIS_BOARD_START_X = 0
    TETRIS_BOARD_START_Y = 0

    yield grid_board.GridBoard(
            TETRIS_BOARD_WIDTH,
            TETRIS_BOARD_HEIGHT,
            TETRIS_BOARD_START_X,
            TETRIS_BOARD_START_Y
        )

    print("teardown")

def test_number_of_horizontal_grid_points(grid_board_resource):
    v_points, h_points = grid_board_resource.calculate_grid_points()
    assert(len(v_points) == 42 and len(h_points) == 60)

def test_board_to_screen_conversion(grid_board_resource):
    screen_x, screen_y = grid_board_resource.convert_to_screen_coordinates(0, 0)
    assert(screen_x == 10 and screen_y == 590.)

    screen_x, screen_y = grid_board_resource.convert_to_screen_coordinates(2, 1)
    assert(screen_x == (grid_board_resource.BOARD_LINE_DIST * 2) + (grid_board_resource.BOARD_LINE_DIST / 2) and \
            screen_y == 570.)

def test_screen_to_board_conversion(grid_board_resource):
    board_x, board_y = grid_board_resource.convert_to_board_coordinates(10, 590.)
    assert(board_x == 0 and board_y == 0)

    board_x, board_y = grid_board_resource.convert_to_board_coordinates(
        (grid_board_resource.BOARD_LINE_DIST * 2) + (grid_board_resource.BOARD_LINE_DIST / 2),
        570
    )
    assert(board_x == 2 and board_y == 1)

def test_collision_detection(grid_board_resource):
    grid_board_resource.calculate_grid_points()

    board_max_x = len(grid_board_resource.board_lookup_table[0])
    board_max_y = len(grid_board_resource.board_lookup_table)

    outside_bound_points = [
        (board_max_x, board_max_y),
        (board_max_x + 1, board_max_y + 1)
    ]

    result = grid_board_resource.has_collision(outside_bound_points)
    assert(result is True)

