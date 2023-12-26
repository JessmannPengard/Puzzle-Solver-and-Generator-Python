from puzzle.puzzle import Puzzle
from puzzle.puzzle_solver import PuzzleSolver
import sys
import time

if len(sys.argv) < 2:
    print("Usage: solve [filename]")
    sys.exit(1)

file_name = sys.argv[1]
puzzle = Puzzle.load_puzzle(file_name)

if puzzle is not None:
    print(puzzle.to_string())

    print("Solving...")
    solver = PuzzleSolver(puzzle)

    start_time = time.time()
    solver.solve()
    end_time = time.time()

    execution_time = end_time - start_time

    solutions = solver.get_solutions_as_string()
    print(solutions)

    print(f"Solved in {execution_time:.4f} secs.")


# Example usage:
# python solve.py puzzles/2x10.txt
