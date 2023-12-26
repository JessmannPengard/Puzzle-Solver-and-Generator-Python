# puzzle_piece.py

class PuzzlePiece:
    def __init__(self, piece_id, faces):
        """
        PuzzlePiece class constructor.

        Args:
            piece_id: Identifier for the puzzle piece.
            faces: List of faces for the puzzle piece.
        """
        self.id = piece_id
        self.faces = faces

    def get_id(self):
        """
        Get the identifier of the puzzle piece.

        Returns:
            Identifier of the puzzle piece.
        """
        return self.id

    def set_id(self, piece_id):
        """
        Set the identifier of the puzzle piece.

        Args:
            piece_id: Identifier to set.
        """
        self.id = piece_id

    def get_faces(self):
        """
        Get the faces of the puzzle piece.

        Returns:
            List of faces for the puzzle piece.
        """
        return self.faces

    def set_faces(self, faces):
        """
        Set the faces of the puzzle piece.

        Args:
            faces: List of faces to set.
        """
        self.faces = faces

    def rotate(self):
        """
        Rotate the puzzle piece.
        """
        current_faces = self.get_faces()
        rotated_faces = current_faces[-1:] + current_faces[:-1]
        self.set_faces(rotated_faces)

    def rotate_to_corner(self, position):
        """
        Rotate the puzzle piece to a corner position.

        Args:
            position: Target corner position.
        """
        target_pattern = []

        if position == "top-left":
            target_pattern = [0, 0, -1, -1]
        elif position == "top-right":
            target_pattern = [-1, 0, 0, -1]
        elif position == "bottom-right":
            target_pattern = [-1, -1, 0, 0]
        elif position == "bottom-left":
            target_pattern = [0, -1, -1, 0]
        elif position == "left":
            target_pattern = [0, 0, -1, 0]
        elif position == "right":
            target_pattern = [-1, 0, 0, 0]
        elif position == "top":
            target_pattern = [0, 0, 0, -1]
        elif position == "bottom":
            target_pattern = [0, -1, 0, 0]
        else:
            raise ValueError("Invalid position")

        while not self.matches_pattern(self.get_faces(), target_pattern):
            self.rotate()

    def rotate_to_edge(self, position):
        """
        Rotate the puzzle piece to an edge position.

        Args:
            position: Target edge position.
        """
        target_pattern = []

        if position == "left":
            target_pattern = [0, -1, -1, -1]
        elif position == "top":
            target_pattern = [-1, 0, -1, -1]
        elif position == "right":
            target_pattern = [-1, -1, 0, -1]
        elif position == "bottom":
            target_pattern = [-1, -1, -1, 0]
        else:
            raise ValueError("Invalid position")

        while not self.matches_pattern(self.get_faces(), target_pattern):
            self.rotate()

    def matches_pattern(self, faces, pattern):
        """
        Check if the puzzle piece matches a given pattern.

        Args:
            faces: List of faces for the puzzle piece.
            pattern: Target pattern to match.

        Returns:
            True if the puzzle piece matches the pattern, False otherwise.
        """
        return all(pattern[i] == -1 or faces[i] == pattern[i] for i in range(4))

    def is_corner(self):
        """
        Check if the puzzle piece is a corner.

        Returns:
            True if the puzzle piece is a corner, False otherwise.
        """
        num_borders = self.count_borders()
        return num_borders == 2

    def is_linear_corner(self):
        """
        Check if the puzzle piece is a linear corner.

        Returns:
            True if the puzzle piece is a linear corner, False otherwise.
        """
        num_borders = self.count_borders()
        return num_borders == 3

    def is_edge(self):
        """
        Check if the puzzle piece is an edge.

        Returns:
            True if the puzzle piece is an edge, False otherwise.
        """
        num_borders = self.count_borders()
        return num_borders == 1

    def is_double_edge(self):
        """
        Check if the puzzle piece is a double edge.

        Returns:
            True if the puzzle piece is a double edge, False otherwise.
        """
        num_borders = self.count_borders()
        return num_borders == 2

    def is_interior(self):
        """
        Check if the puzzle piece is an interior piece.

        Returns:
            True if the puzzle piece is an interior piece, False otherwise.
        """
        num_borders = self.count_borders()
        return num_borders == 0

    def count_borders(self):
        """
        Count the number of borders on the puzzle piece.

        Returns:
            Number of borders on the puzzle piece.
        """
        return sum(face == 0 for face in self.faces)
