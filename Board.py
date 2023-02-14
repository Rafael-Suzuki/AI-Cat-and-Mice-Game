class Board:
    def __init__(self):
        self.size = 8
        self.cat_pos = (7, 3)
        self.rat_pos = [(1, 1), (1, 3), (1, 5), (6, 0), (6, 2), (6, 4)]
        
    def move_cat(self, move):
        self.cat_pos = move
        
    def move_rat(self, index, move):
        self.rat_pos[index] = move
        
    def get_cat_moves(self):
        moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if abs(i) != abs(j):
                    new_pos = (self.cat_pos[0]+i, self.cat_pos[1]+j)
                    if 0 <= new_pos[0] < self.size and 0 <= new_pos[1] < self.size:
                        moves.append(new_pos)
        return moves
        
    def get_rat_moves(self, index):
        moves = []
        rat = self.rat_pos[index]
        for i in range(1, 3):
            for j in [-1, 1]:
                new_pos = (rat[0]+j*i, rat[1]+i)
                if 0 <= new_pos[0] < self.size and 0 <= new_pos[1] < self.size:
                    if j == -1:
                        if new_pos in self.rat_pos:
                            break
                    else:
                        moves.append(new_pos)
        return moves
        
    def is_cat_win(self):
        for i in range(3):
            if self.cat_pos[0] == 0 and self.cat_pos[1] == 2*i+1:
                return True
        return False
        
    def is_rat_win(self):
        for pos in self.rat_pos:
            if pos[0] == self.size-1:
                return True
        return False