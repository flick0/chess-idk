import chess
import render
import bot

board = chess.Board()

if __name__ == "__main__":
    while 1:
        render.Unicode.from_board(board)
        move = input("Enter move: ")
        board.push_san(move)
        board = bot.Brute.move(board)