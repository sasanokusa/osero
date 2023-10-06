class board:
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1,-1, 0, 0, 0],
                      [0, 0, 0, -1,1, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],]

    def search_color(self, pos, color):
        x, y = pos
        other_color = color * -1
        l = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (not 8 >= x+i >= 0 and 8 >= y+j >= 0) \
                                    or (i == 0 and j == 0):
                    continue
                set_pos = (x+i, y+j)

                if self.board[set_pos[0]][set_pos[1]] == other_color:
                    l.append((i, j))
        return l
