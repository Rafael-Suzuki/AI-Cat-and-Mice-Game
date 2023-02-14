import math
import Board
        
class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 1
        
    def get_moves(self):
        if self.current_player == 1:
            moves = self.board.get_cat_moves()
        else:
            moves = []
            for i in range(6):
                if self.board.rat_pos[i][0] < self.board.size-1:
                    moves.extend([(i, pos) for pos in self.board.get_rat_moves(i)])
        return moves
        
    def make_move(self, move):
        if self.current_player == 1:
            self.board.move_cat(move)
        else:
            self.board.move_rat(move[0], move[1])
        self.current_player *= -1
        
    def evaluate(self):
        if self.board.is_cat_win():
            return math.inf
        elif self.board.is_rat_win():
            return -math.inf
        else:
            return 0
        
    def minimax(self, depth, alpha, beta):
        if depth == 0:
            return self.evaluate(), None
        moves = self.get_moves()
        best_move = None
        if self.current_player == 1:
            value = -math.inf
            for move in moves:
                self.make_move(move)
                new_value, _ = self.minimax(depth-1, alpha, beta)
                self.make_move(move)
                if new_value > value:
                    value = new_value
                    best_move = move
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
        else:
           value = math.inf
        for move in moves:
            self.make_move(move)
            new_value, _ = self.minimax(depth-1, alpha, beta)
            self.make_move(move)
            if new_value < value:
                value = new_value
                best_move = move
            beta = min(beta, value)
            if beta <= alpha:
                break
            return value, best_move

    def print_game_state(self):
        print("Cat position:", self.board.cat_pos)
        print("Rat positions:", self.board.rat_pos)
        if self.current_player == 1:
            print("Cat to move")
            moves = self.board.get_cat_moves()
            print("Available moves:", moves)
        else:
            print("Rats to move")
            moves = self.get_moves()
            print("Available moves:")
            for move in moves:
                print(move[0], move[1])