from puzzle.puzzle import Puzzle
from puzzle.puzzle_piece import PuzzlePiece
from typing import List, Optional


class PuzzleSolver:
    def __init__(self, puzzle: Puzzle):
        self.puzzle = puzzle
        self.solutions = []

    def get_solutions_as_string(self) -> str:
        separator = "\n"
        result = f"{separator}Solution(s){separator}"
        for solution in self.solutions:
            for row in solution:
                for piece in row:
                    result += f"{piece.get_id()} " if piece is not None else "null "
                result += separator
            result += separator
        return result

    def solve(self) -> None:
        current_solution = [[None]*self.puzzle.get_cols()
                            for _ in range(self.puzzle.get_rows())]
        self.solve_puzzle(0, 0, current_solution, [])

    def solve_puzzle(self, row: int, col: int, current_solution: List[List[Optional[PuzzlePiece]]], used_pieces: List[PuzzlePiece]) -> None:
        num_pieces = len(self.puzzle.get_pieces())

        # Calculate next row and column
        next_row = row
        next_col = col + 1
        if next_col == self.puzzle.get_cols():
            next_row += 1
            next_col = 0

        # Base case: if we've placed all the pieces, we found a solution
        if len(used_pieces) == num_pieces:
            # Save current solution to the solutions array
            self.solutions.append([row[:] for row in current_solution])
            return

        pieces = self.puzzle.get_pieces()

        if row == 0 and col == 0:
            # Find fixed top left corner to avoid rotated solutions
            fixed_corner_piece = self.find_fixed_corner_piece(pieces)

            # Add to used pieces
            used_pieces.append(fixed_corner_piece)

            # Place the piece in the current solution
            current_solution[row][col] = fixed_corner_piece

            # Recursively try to solve the puzzle with the updated solution
            self.solve_puzzle(next_row, next_col,
                              current_solution, used_pieces)
        else:
            # Iterate through all pieces and try placing them
            for i in range(num_pieces):
                current_piece = pieces[i]

                if current_piece not in used_pieces and self.try_piece(row, col, current_piece, current_solution):
                    # Add to used pieces
                    used_pieces.append(current_piece)

                    # Place the piece in the current solution
                    current_solution[row][col] = current_piece

                    # Recursively try to solve the puzzle with the updated solution
                    self.solve_puzzle(next_row, next_col,
                                      current_solution, used_pieces)

                    # Backtrack: Undo the changes made for backtracking
                    current_solution[row][col] = None
                    used_pieces.pop()

    def find_fixed_corner_piece(self, pieces: List[PuzzlePiece]) -> Optional[PuzzlePiece]:
        for piece in pieces:
            if self.puzzle.is_one_dimensional():
                if piece.is_linear_corner():
                    if self.puzzle.get_rows() == 1:
                        piece.rotate_to_corner("left")
                    else:
                        piece.rotate_to_corner("top")
                    return piece
            else:
                if piece.is_corner():
                    piece.rotate_to_corner("top-left")
                    return piece
        return None

    def try_piece(self, row: int, col: int, piece: PuzzlePiece, solution: List[List[PuzzlePiece]]) -> bool:
        width = self.puzzle.get_cols()
        height = self.puzzle.get_rows()

        top_piece = solution[row - 1][col] if row > 0 else None
        left_piece = solution[row][col - 1] if col > 0 else None

        if self.puzzle.is_one_dimensional():
            # One-dimensional puzzle
            if height == 1:
                # X linear
                if col == 0:
                    # Left Corner
                    if piece.is_linear_corner():
                        piece.rotate_to_corner("left")
                        return True
                elif 0 < col < width - 1:
                    # Interior X linear
                    if piece.is_double_edge():
                        if left_piece.get_faces()[2] == piece.get_faces()[0]:
                            return True
                        for _ in range(3):
                            piece.rotate()
                            if left_piece.get_faces()[2] == piece.get_faces()[0]:
                                return True
                else:
                    # Right Corner
                    if piece.is_linear_corner():
                        piece.rotate_to_corner("right")
                        return True
            else:
                # Y linear
                if row == 0:
                    # Top corner
                    if piece.is_linear_corner():
                        piece.rotate_to_corner("top")
                        return True
                elif 0 < row < height - 1:
                    # Interior Y linear
                    if piece.is_double_edge():
                        if top_piece.get_faces()[3] == piece.get_faces()[1]:
                            return True
                        for _ in range(3):
                            piece.rotate()
                            if top_piece.get_faces()[3] == piece.get_faces()[1]:
                                return True
                else:
                    # Bottom corner
                    if piece.is_linear_corner():
                        piece.rotate_to_corner("bottom")
                        return True
        else:
            # Square or rectangular puzzle
            if row == 0:
                # First row
                if col == 0:
                    # Top Left Corner
                    if piece.is_corner():
                        piece.rotate_to_corner("top-left")
                        return True
                elif col == width - 1:
                    # Top Right Corner
                    if piece.is_corner():
                        piece.rotate_to_corner("top-right")
                        if left_piece.get_faces()[2] == piece.get_faces()[0]:
                            return True
                else:
                    # Top Edge
                    if piece.is_edge():
                        piece.rotate_to_edge("top")
                        if left_piece.get_faces()[2] == piece.get_faces()[0]:
                            return True
            elif row == height - 1:
                # Last row
                if col == 0:
                    # Bottom Left Corner
                    if piece.is_corner():
                        piece.rotate_to_corner("bottom-left")
                        if top_piece.get_faces()[3] == piece.get_faces()[1]:
                            return True
                elif col == width - 1:
                    # Bottom Right Corner
                    if piece.is_corner():
                        piece.rotate_to_corner("bottom-right")
                        if (
                            top_piece.get_faces()[3] == piece.get_faces()[1]
                            and left_piece.get_faces()[2] == piece.get_faces()[0]
                        ):
                            return True
                else:
                    # Bottom Edge
                    if piece.is_edge():
                        piece.rotate_to_edge("bottom")
                        if (
                            top_piece.get_faces()[3] == piece.get_faces()[1]
                            and left_piece.get_faces()[2] == piece.get_faces()[0]
                        ):
                            return True
            else:
                # Intermediate rows
                if col == 0:
                    # Left Edge
                    if piece.is_edge():
                        piece.rotate_to_edge("left")
                        if top_piece.get_faces()[3] == piece.get_faces()[1]:
                            return True
                elif col == width - 1:
                    # Right Edge
                    if piece.is_edge():
                        piece.rotate_to_edge("right")
                        if (
                            top_piece.get_faces()[3] == piece.get_faces()[1]
                            and left_piece.get_faces()[2] == piece.get_faces()[0]
                        ):
                            return True
                else:
                    # Interior
                    if piece.is_interior():
                        if (
                            top_piece.get_faces()[3] == piece.get_faces()[1]
                            and left_piece.get_faces()[2] == piece.get_faces()[0]
                        ):
                            return True
                        for _ in range(3):
                            piece.rotate()
                            if (
                                top_piece.get_faces()[
                                    3] == piece.get_faces()[1]
                                and left_piece.get_faces()[2] == piece.get_faces()[0]
                            ):
                                return True
        return False
