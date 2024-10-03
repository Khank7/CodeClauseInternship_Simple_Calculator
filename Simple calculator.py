import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x400")
        self.root.resizable(False, False)

        # Create a frame for the entry field
        self.entry_frame = tk.Frame(self.root, bg="#f0f0f0", highlightbackground="gray", highlightthickness=1)
        self.entry_frame.pack(fill="x", padx=10, pady=10)

        # Create the entry field
        self.entry = tk.Entry(self.entry_frame, width=35, borderwidth=5, font=("Arial", 20), justify="right")
        self.entry.pack(fill="x", padx=10, pady=10)

        # Create a frame for the buttons
        self.button_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.button_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create the buttons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 0
        col_val = 0

        for button in buttons:
            tk.Button(self.button_frame, text=button, width=5, font=("Arial", 16), command=lambda button=button: self.click_button(button), bg="#e0e0e0", fg="black", activebackground="#c0c0c0", activeforeground="black").grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Create a clear button
        tk.Button(self.button_frame, text="Clear", width=22, font=("Arial", 16), command=self.clear_entry, bg="#e0e0e0", fg="black", activebackground="#c0c0c0", activeforeground="black").grid(row=row_val, column=0, columnspan=4, padx=5, pady=5)

    def click_button(self, button):
        if button == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            self.entry.insert(tk.END, button)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()