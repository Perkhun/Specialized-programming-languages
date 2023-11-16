from tkinter import filedialog, messagebox, Tk

class FileOperations:
    @staticmethod
    def save_representation(representation: str, representation_type: str):
        #Save the representation to a file

        try:
            # Create a Tkinter root window (invisible)
            root = Tk()
            root.withdraw()

            # Prompt the user to select a file for saving
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                title=f"Save {representation_type} representation as"
            )

            # Check if the user canceled the file selection
            if not file_path:
                return

            # Write the representation to the selected file
            with open(file_path, "w") as file:
                file.write(representation)

            # Display a success message
            messagebox.showinfo("Success", f"{representation_type} representation saved successfully to {file_path}")
        except (PermissionError, FileNotFoundError) as e:
            # Display an error message if an exception occurs during file saving
            messagebox.showerror("Error", str(e))
        finally:
            # Destroy the Tkinter root window to free resources
            root.destroy()
