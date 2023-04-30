class TicTacToeAlgorithm:
    def __init__(self, board_list):
        self.board_list = list(board_list)
        self.cond_list = [self.board_list[0] + self.board_list[1] + self.board_list[2],
                          self.board_list[3] + self.board_list[4] + self.board_list[5],
                          self.board_list[6] + self.board_list[7] + self.board_list[8],
                          self.board_list[0] + self.board_list[3] + self.board_list[6],
                          self.board_list[1] + self.board_list[4] + self.board_list[7],
                          self.board_list[2] + self.board_list[5] + self.board_list[8],
                          self.board_list[0] + self.board_list[4] + self.board_list[8],
                          self.board_list[2] + self.board_list[4] + self.board_list[6]]

    def check_x_won(self):
        return "XXX" in self.cond_list

    def check_y_won(self):
        return "YYY" in self.cond_list

    def check_draw(self):
        return " " not in self.board_list
