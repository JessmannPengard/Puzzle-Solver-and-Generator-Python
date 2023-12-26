# puzzle.py

from typing import List
from puzzle.puzzle_piece import PuzzlePiece


class Puzzle:
    def __init__(self):
        """
        Puzzle class constructor.
        """
        self.cols: int = 0
        self.rows: int = 0
        self.pieces: List[PuzzlePiece] = []

    def get_cols(self) -> int:
        """
        Get the number of columns in the puzzle.

        Returns:
            int: Number of columns.
        """
        return self.cols

    def set_cols(self, cols: int) -> None:
        """
        Set the number of columns in the puzzle.

        Args:
            cols (int): Number of columns to set.
        """
        self.cols = cols

    def get_rows(self) -> int:
        """
        Get the number of rows in the puzzle.

        Returns:
            int: Number of rows.
        """
        return self.rows

    def set_rows(self, rows: int) -> None:
        """
        Set the number of rows in the puzzle.

        Args:
            rows (int): Number of rows to set.
        """
        self.rows = rows

    def get_pieces(self) -> List[PuzzlePiece]:
        """
        Get the list of puzzle pieces.

        Returns:
            List[PuzzlePiece]: List of puzzle pieces.
        """
        return self.pieces

    def set_pieces(self, pieces: List[PuzzlePiece]) -> None:
        """
        Set the list of puzzle pieces.

        Args:
            pieces (List[PuzzlePiece]): List of puzzle pieces to set.
        """
        self.pieces = pieces

    def to_string(self) -> str:
        """
        Convert puzzle information to a string.

        Returns:
            str: Puzzle information as a string.
        """
        separator = "\n"
        return (
            f"Columns: {self.cols} - Rows: {self.rows}"
            f"{separator}Pieces:{self.show_pieces(self.pieces)}"
        )

    def show_pieces(self, pieces: List[PuzzlePiece]) -> str:
        """
        Convert puzzle pieces to a string.

        Args:
            pieces (List[PuzzlePiece]): List of puzzle pieces.
            for_web (bool): Whether the string is for web output.

        Returns:
            str: Puzzle pieces as a string.
        """
        str_pieces = ""
        separator = "\n"
        for piece in pieces:
            str_pieces += separator
            for face in piece.get_faces():
                str_pieces += f"{face} "
            str_pieces = str_pieces.rstrip()
        return str_pieces

    @staticmethod
    def handle_error(message: str) -> None:
        """
        Handle and print an error message.

        Args:
            message (str): Error message to handle and print.
        """
        print(f"Error: {message}")

    @classmethod
    def load_puzzle(cls, file_name: str) -> 'Puzzle':
        """
        Load a puzzle from a file.

        Args:
            cls: Class reference.
            file_name (str): Name of the file containing puzzle information.

        Returns:
            'Puzzle': Loaded puzzle object or None if an error occurs.
        """
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
        """
        Check if the puzzle is one-dimensional.

        Returns:
            bool: True if the puzzle is one-dimensional, False otherwise.
        """
        return self.get_rows() == 1 or self.get_cols() == 1
