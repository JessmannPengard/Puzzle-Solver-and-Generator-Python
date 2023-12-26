class PuzzlePiece:
    def __init__(self, piece_id, faces):
        self.id = piece_id
        self.faces = faces

    def get_id(self):
        return self.id

    def set_id(self, piece_id):
        self.id = piece_id

    def get_faces(self):
        return self.faces

    def set_faces(self, faces):
        self.faces = faces

    def rotate(self):
        current_faces = self.get_faces()
        rotated_faces = current_faces[-1:] + current_faces[:-1]
        self.set_faces(rotated_faces)

    def rotate_to_corner(self, position):
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
        return all(pattern[i] == -1 or faces[i] == pattern[i] for i in range(4))

    def is_corner(self):
        num_borders = self.count_borders()
        return num_borders == 2

    def is_linear_corner(self):
        num_borders = self.count_borders()
        return num_borders == 3

    def is_edge(self):
        num_borders = self.count_borders()
        return num_borders == 1

    def is_double_edge(self):
        num_borders = self.count_borders()
        return num_borders == 2

    def is_interior(self):
        num_borders = self.count_borders()
        return num_borders == 0

    def count_borders(self):
        return sum(face == 0 for face in self.faces)
