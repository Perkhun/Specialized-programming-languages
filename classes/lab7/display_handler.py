import tkinter as tk
from tkinter import ttk, messagebox

class DisplayHandler:
    """
    DisplayHandler is a utility class for creating and managing the display
    of tables and lists in Tkinter GUI applications.

    Methods:
    - display_table(root, data, header_color, table_bg_color):
        Display a table using Tkinter Treeview.

    - display_list(root, data, item_color, list_bg_color):
        Display a list using Tkinter Listbox.

    - sort_treeview(tree, col, reverse):
        Sort a Tkinter Treeview by a specific column.

    Usage:
    - Create an instance of DisplayHandler and use its methods to display tables and lists.

    Example:
    ```python
    root = tk.Tk()
    
    # Example data for table
    table_data = [{"Name": "John", "Age": 30, "City": "New York"},
                  {"Name": "Alice", "Age": 25, "City": "London"}]
    DisplayHandler.display_table(root, table_data, 'blue', 'white')

    # Example data for list
    list_data = ["Item 1", "Item 2", "Item 3"]
    DisplayHandler.display_list(root, list_data, 'black', 'lightgrey')

    root.mainloop()
    ```
    """
    @staticmethod
    def display_table(root, data, header_color, table_bg_color):
        """
        Display a table using Tkinter Treeview.

        Args:
        - root: Tkinter root window.
        - data (list): List of dictionaries representing table data.
        - header_color (str): Color of table headers.
        - table_bg_color (str): Background color of the table.

        Raises:
        - Exception: If an error occurs during table display.
        """
        try:
            if not data:
                messagebox.showinfo("Result", "No data.")
                return

            headers = list(data[0].keys())

        except Exception as e:
            messagebox.showerror("Error", f'Error displaying table: {e}')

        # Створення вікна Tkinter
        table_window = tk.Toplevel(root)
        table_window.title("Data table")

        # Розгортання вікна на повний екран
        table_window.state('zoomed')

        # Створення Treeview для таблиці
        tree = ttk.Treeview(table_window, columns=headers, show='headings', height=10,
                            xscrollcommand=lambda x: scrollbar_x.set(x))
        tree.pack(fill=tk.BOTH, expand=True)

        # Додаємо горизонтальний скролер
        scrollbar_x = tk.Scrollbar(tree, orient=tk.HORIZONTAL, command=tree.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        tree.configure(xscrollcommand=scrollbar_x.set)

        # Встановлення заголовків таблиці
        for header in headers:
            tree.heading(header, text=header, anchor=tk.CENTER, command=lambda h=header: DisplayHandler.sort_treeview(tree, h, False))
            tree.column(header, anchor=tk.CENTER)

        # Додаємо тег для заголовків
        tree.tag_configure('header', foreground=header_color, background=table_bg_color)

        # Вставка даних в таблицю
        for row in data:
            values = [row[header] for header in headers]
            tree.insert("", tk.END, values=values, tags=('header',))

    @staticmethod
    def display_list(root, data, item_color, list_bg_color):
        """
        Display a list using Tkinter Listbox.

        Args:
        - root: Tkinter root window.
        - data (list): List of items.
        - item_color (str): Color of list items.
        - list_bg_color (str): Background color of the list.

        Raises:
        - Exception: If an error occurs during list display.
        """
        try:
            if not data:
                messagebox.showinfo("Result", "No data.")
                return

        except Exception as e:
            messagebox.showerror("Error", f'Error displaying list: {e}')

        # Створення вікна Tkinter
        list_window = tk.Toplevel(root)
        list_window.title("Data list")

        # Розгортання вікна на повний екран
        list_window.state('zoomed')

        # Створення Listbox для списку
        listbox = tk.Listbox(list_window, bg=list_bg_color, fg=item_color, width=80)

        # Додаємо горизонтальний скролер
        scrollbar_x = tk.Scrollbar(list_window, orient=tk.HORIZONTAL, command=listbox.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        listbox.configure(xscrollcommand=scrollbar_x.set)

        # Вставка даних в список
        for item in data:
            listbox.insert(tk.END, item)

        listbox.pack(fill=tk.BOTH, expand=True)

    @staticmethod
    def sort_treeview(tree, col, reverse):
        """
        Sort a Tkinter Treeview by a specific column.

        Args:
        - tree: Tkinter Treeview.
        - col: Column to sort.
        - reverse (bool): Whether to sort in reverse order.

        Note:
        - This method modifies the Treeview in-place.

        Raises:
        - None
        """
        data = [(tree.set(child, col), child) for child in tree.get_children('')]
        data.sort(reverse=reverse)
        for ix, item in enumerate(data):
            tree.move(item[1], '', ix)
        tree.heading(col, command=lambda: DisplayHandler.sort_treeview(tree, col, not reverse))
