import tkinter as tk


# Write a GUI program that displays a name and addres when a button is pressed.
# You should show the text at the top with two horizontally stacked buttons below
# labelled "Show info" and "Quit". When the "Show info" button is pressed, the label's
# text should change to show your name and address. When the "Quit" button is pressed,
# the program should terminate.


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

        self.is_visible = False

    def create_widgets(self):
        self.label = tk.Label(self, text="Hello World")
        self.label.pack(side="top", padx=8, pady=8)

        self.show_info = tk.Button(self, text="Show info", command=self.show_info_click)
        self.show_info.pack(side="left", padx=8, pady=8)

        self.quit_btn = tk.Button(self, text="Quit", command=self.quit)
        self.quit_btn.pack(side="right", padx=8, pady=8)

    def show_info_click(self):
        if self.is_visible:
            self.label.config(text="")
            self.is_visible = False
        else:
            self.label.config(
                text="""Nadhim Zahawi
3 Trinity Street
Stratford-upon-Avon
CV37 6BL"""
            )
            self.is_visible = True


root = tk.Tk()
app = App(root)
app.mainloop()
