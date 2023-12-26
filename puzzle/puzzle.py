from typing import List
from puzzle.puzzle_piece import PuzzlePiece


class Puzzle:
    def __init__(self):
        self.cols: int = 0
        self.rows: int = 0
        self.pieces: List[PuzzlePiece] = []

    def get_cols(self) -> int:
        return self.cols

    def set_cols(self, cols: int) -> None:
        self.cols = cols

    def get_rows(self) -> int:
        return self.rows

    def set_rows(self, rows: int) -> None:
        self.rows = rows

    def get_pieces(self) -> List[PuzzlePiece]:
        return self.pieces

    def set_pieces(self, pieces: List[PuzzlePiece]) -> None:
        self.pieces = pieces

    def to_string(self, for_web: bool = False) -> str:
        separator = "<br>" if for_web else "\n"
        return (
            f"Columns: {self.cols} - Rows: {self.rows}"
            f"{separator}Pieces:{self.show_pieces(self.pieces, for_web)}"
        )

    def show_pieces(self, pieces: List[PuzzlePiece], for_web: bool = False) -> str:
        str_pieces = ""
        separator = "<br>" if for_web else "\n"
        for piece in pieces:
            str_pieces += separator
            for face in piece.get_faces():
                str_pieces += f"{face} "
            str_pieces = str_pieces.rstrip()
        return str_pieces

    @staticmethod
    def handle_error(message: str) -> None:
        print(f"Error: {message}")

    @classmethod
    def load_puzzle(cls, file_name: str) -> 'Puzzle':
        try:
            with open(file_name, 'r') as file:
                lines = file.read().splitlines()

            first_row = lines.pop(0)
            dimensions = list(map(int, first_row.split()))
            cols, rows = dimensions[0], dimensions[1]

            pieces = []

            for line in lines:
                if line:
                    faces_values = list(map(int, line.split()))

                    if len(faces_values) != 4:
                        cls.handle_error("Invalid piece format.")
                        return None

                    piece_id = len(pieces) + 1
                    faces = faces_values

                    piece = PuzzlePiece(piece_id, faces)
                    pieces.append(piece)

            expected_num_pieces = cols * rows
            if expected_num_pieces != len(pieces):
                cls.handle_error(
                    "The number of pieces does not fit puzzle dimensions.")
                return None

            puzzle = cls()
            puzzle.cols = cols
            puzzle.rows = rows
            puzzle.pieces = pieces

            return puzzle
        except Exception as e:
            cls.handle_error(f"Error processing content: {str(e)}")
            return None

    def is_one_dimensional(self) -> bool:
        return self.get_rows() == 1 or self.get_cols() == 1
