from tkinter import Tk, Frame, Label, Button, StringVar, Entry, OptionMenu, filedialog, messagebox, simpledialog
from lab_5.figures.cube import Cube, Figure3D, Colors
from lab_5.operations.file_operations import FileOperations

class FigureApp:
    def __init__(self):
        #Initialize the FigureApp

        self.root = Tk()
        self.root.title("Figure App")

        self.figure = None
        self.is_2d_representation_available = False
        self.is_3d_representation_available = False

        self.create_widgets()

    #Create and layout the Tkinter widgets
    def create_widgets(self):
        
       # Frame for figure creation
        self.creation_frame = Frame(self.root)
        self.creation_frame.pack(pady=10)

        # Label and Entry for Character input
        Label(self.creation_frame, text="Character:").grid(row=0, column=0, padx=10)
        self.character_entry = Entry(self.creation_frame)
        self.character_entry.grid(row=0, column=1, padx=10)

        # Label and OptionMenu for Color selection
        Label(self.creation_frame, text="Color:").grid(row=0, column=2, padx=10)
        self.color_var = StringVar(self.root)
        self.color_var.set(Colors.RED.name)  # Default color
        self.color_dropdown = OptionMenu(self.creation_frame, self.color_var, *Colors.__members__.keys())
        self.color_dropdown.grid(row=0, column=3, padx=10)

        # Label and Entry for Length input
        Label(self.creation_frame, text="Length:").grid(row=0, column=4, padx=10)
        self.length_entry = Entry(self.creation_frame)
        self.length_entry.grid(row=0, column=5, padx=10)

        # Button to create the figure based on the provided inputs
        Button(self.creation_frame, text="Create Figure", command=self.create_figure).grid(row=0, column=6, padx=10)

        # Frame for figure display and saving
        self.display_frame = Frame(self.root)
        self.display_frame.pack(pady=10)

        # Buttons to trigger 2D and 3D display and saving
        Button(self.display_frame, text="Display 2D", command=self.display_2d).grid(row=0, column=0, padx=10)
        Button(self.display_frame, text="Display 3D", command=self.display_3d).grid(row=0, column=1, padx=10)
        Button(self.display_frame, text="Save 2D", command=self.save_2d).grid(row=0, column=2, padx=10)
        Button(self.display_frame, text="Save 3D", command=self.save_3d).grid(row=0, column=3, padx=10)

        # Frame for figure modification
        self.modification_frame = Frame(self.root)
        self.modification_frame.pack(pady=10)

        # Buttons to trigger color, character, and offset modifications
        Button(self.modification_frame, text="Change Color", command=self.change_color).grid(row=0, column=0, padx=10)
        Button(self.modification_frame, text="Change Character", command=self.change_character).grid(row=0, column=1, padx=10)
        Button(self.modification_frame, text="Change Offsets", command=self.change_offsets).grid(row=0, column=2, padx=10)


    def create_figure(self):
        #Create a Cube figure based on user input

        character = self.character_entry.get()
        color = Colors[self.color_var.get()]

        # Check if the length input is a valid integer
        length_entry_value = self.length_entry.get()
        try:
            length = int(length_entry_value)
        except ValueError:
            messagebox.showerror("Error", "Invalid value for length. Please enter a valid integer.")
            return

        try:
            self.figure = Cube(length, character, color)
            messagebox.showinfo("Success", "Figure created successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def display_2d(self):
        #Display the 2D representation of the figure

        if self.figure:
            representation_2d = self.figure.get_2d_representation()
            print(representation_2d)
            self.is_2d_representation_available = True
        else:
            messagebox.showerror("Error", "There is no figure available!")

    def display_3d(self):
        #Display the 3D representation of the figure

        if self.figure:
            scale = 1.0  # You can add an Entry for scale and get it here
            representation_3d = self.figure.get_3d_representation(scale=scale)
            print(representation_3d)
            self.is_3d_representation_available = True
        else:
            messagebox.showerror("Error", "There is no figure available!")

    def save_2d(self):
        #Save the 2D representation of the figure to a file

        if self.is_2d_representation_available:
            representation_2d = self.figure.get_2d_representation()
            FileOperations.save_representation(representation_2d, "2D")
        else:
            messagebox.showerror("Error", "There is no 2D representation available!")

    def save_3d(self):
        #Save the 3D representation of the figure to a file

        if self.is_3d_representation_available:
            scale = 1.0  # Default scale
            representation_3d = self.figure.get_3d_representation(scale=scale)
            FileOperations.save_representation(representation_3d, "3D")
        else:
            messagebox.showerror("Error", "There is no 3D representation available!")

    def change_color(self):
        #Change the color of the figure based on user input

        if self.figure:
            color_names = [color.name for color in Colors]
            color_name = simpledialog.askstring("Input", f"Enter a name of color or choose from {', '.join(color_names)}:")
            if color_name is not None:
                try:
                    color = Colors[color_name.upper()]
                    self.figure.change_color(color)
                except KeyError:
                    messagebox.showerror("Error", "Invalid color name!")
        else:
            messagebox.showerror("Error", "There is no figure available!")

    def change_character(self):
        #Change the character representation of the figure based on user input

        if self.figure:
            character = simpledialog.askstring("Input", "Enter a character to represent in the shape:")
            if character is not None:
                if self.figure.is_appropriate_character(character):
                    self.figure.change_character(character)
                else:
                    messagebox.showerror("Error", "Invalid character. It should be a single character.")
        else:
            messagebox.showerror("Error", "There is no figure available!")

    def change_offsets(self):
        #Change the horizontal and vertical offsets of the figure based on user input

        if self.figure:
            horizontal_offset = simpledialog.askinteger("Input", "Enter horizontal offset:")
            if horizontal_offset is not None:
                vertical_offset = simpledialog.askinteger("Input", "Enter vertical offset:")
                if vertical_offset is not None:
                    self.figure.change_offsets(horizontal_offset, vertical_offset)
        else:
            messagebox.showerror("Error", "There is no figure available!")

    def run(self):
        #Start the Tkinter main loop

        self.root.mainloop()

if __name__ == "__main__":
    app = FigureApp()
    app.run()
