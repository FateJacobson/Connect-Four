#simple connect four game 
#made by Fate Jacobson


class Board():
    def __init__(self):
        self.playfield = [[0 for i in range(7)] for j in range(6)]
        self.columns = [0 for i in range(7)] 
        self.columnTracker = [6 for i in range(7)] 
        for i in range(len(self.columns)):
            self.columns[i] = i + 1

    def display_board(self):
        print("--------board--------")
        for row in range(len(self.playfield)):
            print(self.playfield[row])
        print("-------columns-------")
        print(self.columns)
        
    def mark_board(self, column, player):
        column -= 1
        if self.columnTracker[column] > 0:
            self.columnTracker[column] -= 1
            self.playfield[self.columnTracker[column]][column] = player
        else:
            return False

class Game(object):
    def __init__(self):
        self.board = Board()

    def has_winner(self, player):
        # Check horizontal locations for wincl
        for c in range(4):
            for r in range(6):
                if self.board.playfield[r][c] == player and self.board.playfield[r][c+1] == player and self.board.playfield[r][c+2] == player and self.board.playfield[r][c+3] == player:
                    return True

        # Check vertical locations for win
        for c in range(7):
            for r in range(3):
                if self.board.playfield[r][c] == player and self.board.playfield[r+1][c] == player and self.board.playfield[r+2][c] == player and self.board.playfield[r+3][c] == player:
                    return True

        # Check positively sloped diaganols
        for c in range(4):
            for r in range(3):
                if self.board.playfield[r][c] == player and self.board.playfield[r+1][c+1] == player and self.board.playfield[r+2][c+2] == player and self.board.playfield[r+3][c+3] == player:
                    return True

        # Check negatively sloped diaganols
        for c in range(4):
            for r in range(3, 6):
                if self.board.playfield[r][c] == player and self.board.playfield[r-1][c+1] == player and self.board.playfield[r-2][c+2] == player and self.board.playfield[r-3][c+3] == player:
                    return True
        
        return False

    def play_game(self):
        self.winner = 0
        self.player = 1
        self.board.display_board()
        while (self.has_winner(1) == False and self.has_winner(2) == False):
            userInput = input("Player (" + str(self.player) + "), enter column: ")
            if userInput < 7 and userInput > 0:
                if self.board.mark_board(userInput, self.player) == False:
                    print("Column is full")
                else:
                    if self.player == 1:
                        self.player = 2
                    else:
                        self.player = 1
            else:
                print("Invalid column")
            self.board.display_board()
        if self.has_winner(1) == True:
            self.winner = 1
        else:
            self.winner = 2
        return self.winner

if __name__ == '__main__':
    game = Game()
    winner = game.play_game()
    print("Player " + str(winner) + " Has Won!")
    
    
