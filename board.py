class Board:
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1,-1, 0, 0, 0],
                      [0, 0, 0, -1,1, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0]]

    def search_color(self, pos, color):
        y, x = pos
        if self.board[y][x] != 0:
            return []
        other_color = color * -1
        l = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (not 7 >= x+j >= 0 and 7 >= y+i >= 0) \
                                    or (i == 0 and j == 0):
                    continue
                if self.board[y+i][x+j] == other_color:
                    l.append((i, j))
        return l

    def can_set(self, pos, color):
        y0, x0 = pos
        search_color_list = self.search_color(pos, color)
        if search_color_list == []:
            return False
        for i in range(len(search_color_list)):
            direction = search_color_list[i]
            for n in range(2, 8, 1):
                y = y0+(n*direction[0])
                x = x0+(n*direction[1])
                if not 0 <= x <= 7 or not 0 <= y <= 7:
                    break
                if self.board[y][x] == color:
                    return True
        return False

if __name__ == "__main__":
    pass
    board = Board()
    board.board = [[0, 0, 0, 0, 0, 0, 0, 0], #0
                   [0, 0, 0, 0, 0, 0, 0, 0], #1
                   [0, 0, 0, 0, 0, 0, 0, 0], #2
                   [0, 0,-1,-1,-1, 0, 0, 0], #3
                   [0, 0, 1, 1, 1, 0, 0, 0], #4
                   [0, 0, 0, 0, 0, 0, 0, 0], #5
                   [0, 0, 0, 0, 0, 0, 0, 0], #6
                   [0, 0, 0, 0, 0, 0, 0, 0]] #7
    #assert set(board.search_color((5, 2), -1)) == {(-1, 0), (-1, 1)}
    #print(board.search_color((5, 3), -1))
    assert board.can_set((5, 2), -1) == True
