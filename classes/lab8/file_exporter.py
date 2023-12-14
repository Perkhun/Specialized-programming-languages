from tkinter import filedialog
from tkinter import messagebox

class FileExporter:
    """Utility class for exporting Matplotlib plots as images."""
    @staticmethod
    def export_plot_as_image(figure):
        """
        Export the given Matplotlib figure as an image.

        Parameters:
        - figure (matplotlib.figure.Figure): The Matplotlib figure to be exported.

        Returns:
        - None
        """
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            figure.savefig(file_path)
            messagebox.showinfo("Success", "Plot successfully saved as an image.")
