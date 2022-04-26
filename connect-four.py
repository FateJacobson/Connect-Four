#simple connect four game 
#made by Fate Jacobson


class board():
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

if __name__ == '__main__':
    board = board()
    board.mark_board(1, 1)
    board.mark_board(1, 2)
    board.mark_board(1, 1)
    board.mark_board(1, 2)
    board.display_board()
    
