import unittest
from puzzle.puzzle import Puzzle
from puzzle.puzzle_piece import PuzzlePiece


class PuzzleTest(unittest.TestCase):
    def test_constructor_and_getters(self):
        puzzle = Puzzle()
        puzzle.set_cols(3)
        puzzle.set_rows(2)

        self.assertEqual(3, puzzle.get_cols())
        self.assertEqual(2, puzzle.get_rows())
        self.assertEqual([], puzzle.get_pieces())

    def test_setters(self):
        puzzle = Puzzle()
        pieces = [PuzzlePiece(1, [1, 2, 3, 4])]

        puzzle.set_cols(3)
        puzzle.set_rows(2)
        puzzle.set_pieces(pieces)

        self.assertEqual(3, puzzle.get_cols())
        self.assertEqual(2, puzzle.get_rows())
        self.assertEqual(pieces, puzzle.get_pieces())

    def test_is_one_dimensional(self):
        puzzle_1dx = Puzzle()
        puzzle_1dx.set_cols(1)
        puzzle_1dx.set_rows(3)

        puzzle_1dy = Puzzle()
        puzzle_1dy.set_cols(3)
        puzzle_1dy.set_rows(1)

        puzzle_2d = Puzzle()
        puzzle_2d.set_cols(4)
        puzzle_2d.set_rows(4)

        self.assertTrue(puzzle_1dx.is_one_dimensional())
        self.assertTrue(puzzle_1dy.is_one_dimensional())
        self.assertFalse(puzzle_2d.is_one_dimensional())


if __name__ == '__main__':
    unittest.main()
