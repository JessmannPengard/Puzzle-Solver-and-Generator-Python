# generate.py

from random import shuffle, randint
import sys
import os
from typing import List


def main():
    """
    Main function to generate a puzzle file, based on user specs.
    """

    try:
        num_cols, num_rows = map(int, sys.argv[1:3])

        if num_cols < 1 or num_rows < 1:
            raise ValueError("Columns and Rows must be positive integers.")

        faces_range_min, faces_range_max = map(int, sys.argv[3].split("-"))
        if faces_range_min < 1 or faces_range_max < faces_range_min:
            raise ValueError("Incorrect range values.")

        destiny_file = sys.argv[4]

        if os.path.exists(destiny_file):
            user_response = input(
                f"The file '{destiny_file}' already exists. Do you want to overwrite it? (y/n): ").lower()
            if user_response != 'y':
                print("Operation canceled. Choose a different filename.")
                sys.exit(1)

    except (IndexError, ValueError) as e:
        print("Error:", e)
        print("Usage: generate [cols] [rows] [faces_range] [filename]")
        print("\ncols:\t\ta positive integer.")
        print("rows:\t\ta positive integer.")
        print("faces_range:\ta range of positive integers. For example: 1-9")
        print("filename:\tpath of destiny file.\n")
        print("Example: generate 4 4 1-9 new_puzzle.txt\n")
        sys.exit(1)

    # First line (cols rows)
    first_line = f"{num_cols} {num_rows}\n"

    # Generate puzzle pieces
    pieces = [[0] * num_cols for _ in range(num_rows)]
    for row in range(num_rows):
        for col in range(num_cols):
            pieces[row][col] = generate_piece(
                col, row, faces_range_min, faces_range_max, pieces)

    # Shuffle and rotate pieces before writing to file
    shuffled_pieces = shuffle_pieces(pieces)

    # Write file
    with open(destiny_file, 'w') as file:
        # Write first line
        file.write(first_line)
        # Write pieces
        for col in range(num_cols):
            for row in range(num_rows):
                file.write(
                    " ".join(map(str, shuffled_pieces[row][col])) + "\n")

    print(f"Puzzle file '{destiny_file}' successfully generated.")


def generate_piece(col: int, row: int, faces_range_min: int, faces_range_max: int, pieces: List[List[List[int]]]) -> List[int]:
    """
    Function to generate a valid piece based on its position in the puzzle
    - Piece format [left_face, top_face, right_face, bottom_face]
    - Borders of the puzzle are represented by 0 in the face value
    """
    col_length = len(pieces[0])
    row_length = len(pieces)

    left_face = pieces[row][col-1][2] if col > 0 else 0
    top_face = pieces[row-1][col][3] if row > 0 else 0
    right_face = randint(
        faces_range_min, faces_range_max) if col < col_length-1 else 0
    bottom_face = randint(
        faces_range_min, faces_range_max) if row < row_length-1 else 0

    return [left_face, top_face, right_face, bottom_face]


def shuffle_pieces(pieces: List[List[List[int]]]) -> List[List[List[int]]]:
    """
    Shuffle and randomly rotate the puzzle pieces.
    """
    shuffled_pieces = [piece.copy() for piece in pieces]
    shuffle(shuffled_pieces)

    for col in shuffled_pieces:
        for piece in col:
            rotations = randint(0, 3)
            piece[:] = piece[-rotations:] + piece[:-rotations]

    return shuffled_pieces


if __name__ == "__main__":
    main()
