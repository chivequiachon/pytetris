class TestShape():

    def __init__(self, board_x, board_y):
        self.board_x = board_x
        self.board_y = board_y
        #self.state = ShapeState.MOVE
        self.rect_points = [(board_x, board_y), (board_x + 1, board_y + 1)]

    def recalculate_points(self):
        self.rect_points = [(self.board_x, self.board_y), (self.board_x + 1, self.board_y + 1)]

    def fall_down(self):
        self.board_y = self.board_y + 1
        
    def move_right(self):
        self.board_x += 1

    def move_left(self):
        self.board_x -= 1

    def go_up(self):
        self.board_y -= 1

        
    

    