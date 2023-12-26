import unittest
from puzzle.puzzle_piece import PuzzlePiece


class PuzzlePieceTest(unittest.TestCase):
    def test_constructor_and_getters(self):
        faces = [1, 2, 3, 4]
        piece = PuzzlePiece(1, faces)

        self.assertEqual(1, piece.get_id())
        self.assertEqual(faces, piece.get_faces())

    def test_setters(self):
        faces = [1, 2, 3, 4]
        piece = PuzzlePiece(1, faces)

        piece.set_id(2)
        piece.set_faces([5, 6, 7, 8])

        self.assertEqual(2, piece.get_id())
        self.assertEqual([5, 6, 7, 8], piece.get_faces())

    def test_rotate(self):
        initial_faces = [1, 2, 3, 4]
        piece = PuzzlePiece(1, initial_faces)

        piece.rotate()

        expected_faces = [4, 1, 2, 3]
        self.assertEqual(expected_faces, piece.get_faces())

    def test_rotate_to_corner(self):
        top_left_pattern = [0, 0, -1, -1]
        test_faces = [1, 2, 0, 0]
        piece = PuzzlePiece(1, test_faces)
        piece.rotate_to_corner("top-left")
        self.assertTrue(self.check_pattern(piece, top_left_pattern))

        top_right_pattern = [-1, 0, 0, -1]
        test_faces = [1, 2, 0, 0]
        piece = PuzzlePiece(1, test_faces)
        piece.rotate_to_corner("top-right")
        self.assertTrue(self.check_pattern(piece, top_right_pattern))

        bottom_left_pattern = [0, -1, -1, 0]
        test_faces = [1, 2, 0, 0]
        piece = PuzzlePiece(1, test_faces)
        piece.rotate_to_corner("bottom-left")
        self.assertTrue(self.check_pattern(piece, bottom_left_pattern))

        bottom_right_pattern = [-1, -1, 0, 0]
        test_faces = [0, 1, 2, 0]
        piece = PuzzlePiece(1, test_faces)
        piece.rotate_to_corner("bottom-right")
        self.assertTrue(self.check_pattern(piece, bottom_right_pattern))

        top_pattern = [0, 0, 0, -1]
        test_faces = [1, 0, 0, 0]
        piece = PuzzlePiece(1, test_faces)
        piece.rotate_to_corner("top")
        self.assertTrue(self.check_pattern(piece, top_pattern))

        bottom_pattern = [0, -1, 0, 0]
        test_faces = [1, 0, 0, 0]
        piece = PuzzlePiece(1, test_faces)
        piece.rotate_to_corner("bottom")
        self.assertTrue(self.check_pattern(piece, bottom_pattern))

        left_pattern = [0, 0, -1, 0]
        test_faces = [1, 0, 0, 0]
        piece = PuzzlePiece(1, test_faces)
        piece.rotate_to_corner("left")
        self.assertTrue(self.check_pattern(piece, left_pattern))

        right_pattern = [-1, 0, 0, 0]
        test_faces = [0, 1, 0, 0]
        piece = PuzzlePiece(1, test_faces)
        piece.rotate_to_corner("right")
        self.assertTrue(self.check_pattern(piece, right_pattern))

    def test_rotate_to_edge(self):
        left_pattern = [0, -1, -1, -1]
        test_faces = [1, 2, 3, 0]
        piece = PuzzlePiece(1, test_faces)
        piece.rotate_to_edge("left")
        self.assertTrue(self.check_pattern(piece, left_pattern))

        right_pattern = [-1, -1, 0, -1]
        test_faces = [1, 2, 3, 0]
        piece = PuzzlePiece(1, test_faces)
        piece.rotate_to_edge("right")
        self.assertTrue(self.check_pattern(piece, right_pattern))

        top_pattern = [-1, 0, -1, -1]
        test_faces = [1, 2, 3, 0]
        piece = PuzzlePiece(1, test_faces)
        piece.rotate_to_edge("top")
        self.assertTrue(self.check_pattern(piece, top_pattern))

        bottom_pattern = [-1, -1, -1, 0]
        test_faces = [1, 2, 3, 0]
        piece = PuzzlePiece(1, test_faces)
        piece.rotate_to_edge("bottom")
        self.assertTrue(self.check_pattern(piece, bottom_pattern))

    def test_is_corner(self):
        test_faces = [0, 0, 1, 2]
        piece = PuzzlePiece(1, test_faces)
        self.assertTrue(piece.is_corner())

        test_faces = [0, 1, 2, 3]
        piece = PuzzlePiece(1, test_faces)
        self.assertFalse(piece.is_corner())

        test_faces = [1, 2, 3, 4]
        piece = PuzzlePiece(1, test_faces)
        self.assertFalse(piece.is_corner())

        test_faces = [0, 0, 0, 1]
        piece = PuzzlePiece(1, test_faces)
        self.assertFalse(piece.is_corner())

    def test_is_linear_corner(self):
        test_faces = [0, 1, 0, 0]
        piece = PuzzlePiece(1, test_faces)
        self.assertTrue(piece.is_linear_corner())

        test_faces = [0, 1, 2, 3]
        piece = PuzzlePiece(1, test_faces)
        self.assertFalse(piece.is_linear_corner())

        test_faces = [1, 2, 3, 4]
        piece = PuzzlePiece(1, test_faces)
        self.assertFalse(piece.is_linear_corner())

        test_faces = [0, 0, 1, 2]
        piece = PuzzlePiece(1, test_faces)
        self.assertFalse(piece.is_linear_corner())

    def test_is_edge(self):
        test_faces = [0, 1, 2, 3]
        piece = PuzzlePiece(1, test_faces)
        self.assertTrue(piece.is_edge())

        test_faces = [0, 1, 0, 0]
        piece = PuzzlePiece(1, test_faces)
        self.assertFalse(piece.is_edge())

        test_faces = [1, 2, 3, 4]
        piece = PuzzlePiece(1, test_faces)
        self.assertFalse(piece.is_edge())

        test_faces = [0, 0, 1, 2]
        piece = PuzzlePiece(1, test_faces)
        self.assertFalse(piece.is_edge())

    def test_is_double_edge(self):
        test_faces = [0, 1, 0, 2]
        piece = PuzzlePiece(1, test_faces)
        self.assertTrue(piece.is_double_edge())

        test_faces = [0, 1, 0, 0]
        piece = PuzzlePiece(1, test_faces)
        self.assertFalse(piece.is_double_edge())

        test_faces = [1, 2, 3, 4]
        piece = PuzzlePiece(1, test_faces)
        self.assertFalse(piece.is_double_edge())

        test_faces = [0, 1, 2, 3]
        piece = PuzzlePiece(1, test_faces)
        self.assertFalse(piece.is_double_edge())

    def test_is_interior(self):
        test_faces = [1, 2, 3, 4]
        piece = PuzzlePiece(1, test_faces)
        self.assertTrue(piece.is_interior())

        test_faces = [0, 1, 0, 0]
        piece = PuzzlePiece(1, test_faces)
        self.assertFalse(piece.is_interior())

        test_faces = [1, 0, 3, 0]
        piece = PuzzlePiece(1, test_faces)
        self.assertFalse(piece.is_interior())

        test_faces = [0, 1, 2, 3]
        piece = PuzzlePiece(1, test_faces)
        self.assertFalse(piece.is_interior())

    def check_pattern(self, piece, target_pattern):
        reflection_class = type(piece)
        reflection_method = reflection_class.__dict__['matches_pattern']
        reflection_method = reflection_method.__get__(piece, reflection_class)
        return reflection_method(piece.get_faces(), target_pattern)


if __name__ == '__main__':
    unittest.main()
