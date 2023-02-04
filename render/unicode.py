from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from chess import Board

class Unicode:
    def from_board(board: "Board") -> str:
        print(board.unicode().replace("⭘","·"))
            
