import unittest
import connect_four as cf

class testBoard(unittest.TestCase):
    def test_board_playfeild_initialization(self):
        expectedResult = expectedResult = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        board = cf.Board()
        self.assertEqual(expectedResult, board.playfield)
    
    def test_board_columns_initialization(self):
        expectedResult = expectedResult = [1,2,3,4,5,6,7]
        board = cf.Board()
        self.assertEqual(expectedResult, board.columns)

    def test_board_column_tracker_initialization(self):
        expectedResult = expectedResult = [6,6,6,6,6,6,6]
        board = cf.Board()
        self.assertEqual(expectedResult, board.columnTracker)

    def test_mark_board(self):
        expectedResult = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,0,0,0,0,0,0]]
        board = cf.Board()
        board.mark_board(1, 1)
        self.assertEqual(expectedResult, board.playfield)

    def test_mark_board_invalid_column(self):
        expectedResult = False
        board = cf.Board()
        for x in range(6):
            board.mark_board(1, 1)
        self.assertEqual(expectedResult, board.mark_board(1,1))

class testGame(unittest.TestCase):
    def test_has_winner_horizontal(self):
        expectedResult = True
        game = cf.Game()
        game.board.playfield = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,1,1,0,0,0]]
        self.assertEqual(expectedResult, game.has_winner(1))
    
    def test_has_winner_vertical(self):
        expectedResult = True
        game = cf.Game()
        game.board.playfield = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0]]
        self.assertEqual(expectedResult, game.has_winner(1))
    
    def test_has_winner_diagonal_positive_slope(self):
        expectedResult = True
        game = cf.Game()
        game.board.playfield = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,1,0,0,0,0],[0,1,0,0,0,0,0],[1,0,0,0,0,0,0]]
        self.assertEqual(expectedResult, game.has_winner(1))

    def test_has_winner_diagonal_negative_slope(self):
        expectedResult = True
        game = cf.Game()
        game.board.playfield = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]]
        self.assertEqual(expectedResult, game.has_winner(1))
    
    def test_has_no_winner(self):
        expectedResult = False 
        game = cf.Game()
        game.board.playfield = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        self.assertEqual(expectedResult, game.has_winner(1))

    def test_play_game_with_player_1_win(self):
        expectedResult = 1
        game = cf.Game()
        game.board.playfield = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,1,1,0,0,0]]
        self.assertEqual(expectedResult, game.play_game())

    def test_play_game_with_player_2_win(self):
        expectedResult = 2
        game = cf.Game()
        game.board.playfield = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[2,2,2,2,0,0,0]]
        self.assertEqual(expectedResult, game.play_game())

unittest.main()