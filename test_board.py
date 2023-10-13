import pytest
from board import Board

def test_Board():
    board = Board()
    assert board.board == [[0, 0, 0, 0, 0, 0, 0, 0], #0
                           [0, 0, 0, 0, 0, 0, 0, 0], #1
                           [0, 0, 0, 0, 0, 0, 0, 0], #2
                           [0, 0, 0, 1,-1, 0, 0, 0], #3
                           [0, 0, 0,-1, 1, 0, 0, 0], #4
                           [0, 0, 0, 0, 0, 0, 0, 0], #5
                           [0, 0, 0, 0, 0, 0, 0, 0], #6
                           [0, 0, 0, 0, 0, 0, 0, 0]] #7
    board.board[4][2] = 1
    board.board[4][3] = 1
    board.board[3][2] = -1
    board.board[3][3] = -1
    assert board.board == [[0, 0, 0, 0, 0, 0, 0, 0], #0
                           [0, 0, 0, 0, 0, 0, 0, 0], #1
                           [0, 0, 0, 0, 0, 0, 0, 0], #2
                           [0, 0,-1,-1,-1, 0, 0, 0], #3
                           [0, 0, 1, 1, 1, 0, 0, 0], #4
                           [0, 0, 0, 0, 0, 0, 0, 0], #5
                           [0, 0, 0, 0, 0, 0, 0, 0], #6
                           [0, 0, 0, 0, 0, 0, 0, 0]] #7

@pytest.fixture
def board():
    board1 = Board()
    board1.board = [[0, 0, 0, 0, 0, 0, 0, 0], #0
                    [0, 0, 0, 0, 0, 0, 0, 0], #1
                    [0, 0, 0, 0, 0, 0, 0, 0], #2
                    [0, 0,-1,-1,-1, 0, 0, 0], #3
                    [0, 0, 1, 1, 1, 0, 0, 0], #4
                    [0, 0, 0, 0, 0, 0, 0, 0], #5
                    [0, 0, 0, 0, 0, 0, 0, 0], #6
                    [0, 0, 0, 0, 0, 0, 0, 0]] #7
    board2 = Board()
    board2.board = [[ 0, 0, 0, 0, 0, 0, 0, 0],#0
                    [ 0, 0, 0,-1, 0, 0, 0, 0],#1
                    [-1, 1, 0,-1, 1, 0, 0, 1],#2
                    [-1,-1,-1,-1, 1,-1,-1, 0],#3
                    [ 0, 1,-1,-1, 1, 1, 0,-1],#4
                    [ 0, 0, 0, 1, 0,-1, 1, 0],#5
                    [ 0, 0, 0, 0, 1, 0, 0, 0],#6
                    [ 0, 0, 0, 0, 0, 0, 0, 0]]#7
    return board1, board2

def test_search_color(board):
    board1, board2 = board
    assert set(board1.search_color((5, 2), -1)) == {(-1, 0), (-1, 1)}
    assert set(board1.search_color((5, 3), -1)) == {(-1, 0), (-1, 1), (-1, -1)}
    assert set(board1.search_color((6, 5), 1)) == set()
    assert set(board1.search_color((2, 5), 1)) == {(1, -1)}
    assert set(board1.search_color((4, 1), -1)) == {(0, 1)}

def test_can_set(board):
    board1, board2 = board
    assert board1.can_set((5, 2), -1) == True
    assert board1.can_set((2, 3), 1) == True
    assert board1.can_set((5, 5), -1) == True
    assert board1.can_set((2, 4), -1) == False
    assert board1.can_set((6, 4), -1) == False
    assert board1.can_set((6, 4), 1) == False
    assert board1.can_set((4, 1), -1) == False
    assert board2.can_set((5, 1), -1) == True
    assert board2.can_set((5, 2), -1) == True
    assert board2.can_set((1, 4), 1) == True
    assert board2.can_set((5, 5), -1) == False
    assert board2.can_set((2, 4), -1) == False
    assert board2.can_set((6, 4), -1) == False
    assert board2.can_set((6, 4), 1) == False
    assert board2.can_set((4, 1), -1) == False
    assert board2.can_set((5, 1), -1) == True
