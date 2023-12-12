import tkinter as tk
from tkinter import ttk, messagebox

class DisplayHandler:
    @staticmethod
    def display_table(root, data, header_color, table_bg_color):
        try:
            # Check if there is any data to display
            if not data:
                messagebox.showinfo("Result", "No data available for display.")
                return

            # Extract headers from the first row of data
            headers = list(data[0].keys())

        except Exception as e:
            # Display an error message if there is an exception
            messagebox.showerror("Error", f'Error displaying table: {e}')

        # Create a Tkinter window
        table_window = tk.Toplevel(root)
        table_window.title("Data Table")

        # Maximize the window
        table_window.state('zoomed')

        # Create a Treeview for the table
        tree = ttk.Treeview(table_window, columns=headers, show='headings', height=10,
                            xscrollcommand=lambda x: scrollbar_x.set(x))
        tree.pack(fill=tk.BOTH, expand=True)

        # Add horizontal scrollbar
        scrollbar_x = tk.Scrollbar(tree, orient=tk.HORIZONTAL, command=tree.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        tree.configure(xscrollcommand=scrollbar_x.set)

        # Set table headers
        for header in headers:
            tree.heading(header, text=header, anchor=tk.CENTER, command=lambda h=header: DisplayHandler.sort_treeview(tree, h, False))
            tree.column(header, anchor=tk.CENTER)

        # Add tags for headers
        tree.tag_configure('header', foreground=header_color, background=table_bg_color)

        # Insert data into the table
        for row in data:
            values = [row[header] for header in headers]
            tree.insert("", tk.END, values=values, tags=('header',))

    @staticmethod
    def display_list(root, data, item_color, list_bg_color):
        try:
            # Check if there is any data to display
            if not data:
                messagebox.showinfo("Result", "No data available for display.")
                return
            
        except Exception as e:
            # Display an error message if there is an exception
            messagebox.showerror("Error", f'Error displaying list: {e}')

        # Create a Tkinter window
        list_window = tk.Toplevel(root)
        list_window.title("Data List")

        # Maximize the window
        list_window.state('zoomed')

        # Create a Listbox for the list
        listbox = tk.Listbox(list_window, bg=list_bg_color, fg=item_color, width=80)

        # Add horizontal scrollbar
        scrollbar_x = tk.Scrollbar(list_window, orient=tk.HORIZONTAL, command=listbox.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        listbox.configure(xscrollcommand=scrollbar_x.set)

        # Insert data into the list
        for item in data:
            listbox.insert(tk.END, item)

        listbox.pack(fill=tk.BOTH, expand=True)

    @staticmethod
    def sort_treeview(tree, col, reverse):
        # Function to sort the Treeview columns
        data = [(tree.set(child, col), child) for child in tree.get_children('')]
        data.sort(reverse=reverse)
        for ix, item in enumerate(data):
            tree.move(item[1], '', ix)
        tree.heading(col, command=lambda: DisplayHandler.sort_treeview(tree, col, not reverse))
