from lab_5.figures.figure3d import Figure3D, Colors

class Cube(Figure3D):
    def __init__(self, length: int, character: str, color: Colors):
        #Initialize a Cube object

        if length <= 0:
            raise ValueError("Length must be greater than 0")
        super().__init__(character, color)
        self.__length = length
        self.__offset = int(length / 2 + 1)
        self.__horizontal_offset = 0
        self.__vertical_offset = 0

    def change_offsets(self, horizontal_offset: int, vertical_offset: int) -> None:
        #Change the horizontal and vertical offsets

        self.__horizontal_offset = horizontal_offset
        self.__vertical_offset = vertical_offset

    def get_2d_representation(self) -> list:
        #Get the 2D representation of the cube

        result = ""
        for _ in range(self.__vertical_offset):
            result += "\n"
        for row in range(self.__length):
            for _ in range(self.__horizontal_offset):
                result += "   "
            for col in range(self.__length):
                result += f"{self._character}  "
            result += "\n"
        return f"{self._color.value}\n{result}\033[0m"

    def get_3d_representation(self, scale: float = 1.0) -> str:
        #Get the 3D representation of the cube
      
        modified_length = int(self.__length * scale) if self.__length * scale >= 2 else self.__length
        modified_offset = int((self.__length + modified_length) / 4)
        result = ""

        for _ in range(self.__vertical_offset):
            result += "\n"

        # Top view
        for row in range(modified_offset - 1):
            for _ in range(self.__horizontal_offset):
                result += "   "
            for col in range(modified_length + modified_offset - 1):
                if (row + col == modified_offset - 1) or (row == 0 and col > modified_offset - 1):
                    result += f"{self._character}" + ("" if col == modified_length + modified_offset - 2 and row == 0 else "  ")
                elif modified_length + modified_offset - row == col + 2:
                    result += f"{self._character}"
                elif col == modified_length + modified_offset - 2:
                    result += f"  {self._character}"
                else:
                    result += "   "
            result += "\n"

        # Side view
        for row in range(modified_length):
            for _ in range(self.__horizontal_offset):
                result += "   "
            for col in range(modified_length + modified_offset):
                if ((row == 0 or row == modified_length - 1) and col < modified_length or (
                        col == 0 or col == modified_length - 1) and row < modified_length and col < modified_length):
                    result += f"{self._character}" + ("" if row == modified_length - 1 and col == modified_length - 1 else "  ")
                elif row + col == (modified_length - 1) * 2 and col < modified_length + modified_offset - 1:
                    result += "   " * (modified_length - row - 2) + f"{self._character}"
                elif col < modified_length and row < modified_length:
                    result += "   "
                elif row < modified_length - modified_offset and col > modified_length:
                    if col == modified_offset + modified_length - 1:
                        result += f"{self._character}"
                    else:
                        result += "   "
            result += "\n"

        return f"{self._color.value}\n{result}\033[0m"
