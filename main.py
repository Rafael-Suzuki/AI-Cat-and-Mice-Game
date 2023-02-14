import Game
import math

def main():
    game = Game()
    while True:
        print(game.board)
        if game.current_player == 1:
            print("Cat's turn")
        else:
            print("Rat's turn")
        moves = game.get_moves()
        for i, move in enumerate(moves):
            print(i, move)
        choice = int(input())
        game.make_move(moves[choice])
        if game.evaluate() != 0:
            print(game.board)
            if game.evaluate() == math.inf:
                print("Cat wins")
            else:
                print("Rat wins")
            break
    