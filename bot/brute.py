import chess


class Brute:
    def move(board: chess.Board) -> chess.Move:
        
            print(list(board.legal_moves)[-1])
            board.push(list(board.legal_moves)[-1])
            return board