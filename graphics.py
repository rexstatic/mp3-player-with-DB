"""testst"""
import tkinter as tk

class GraphicSetup:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = tk.Label(master, text="This is our first GUI!")
        self.label.pack()

        self.back_button = tk.Button(master, text="Greet", command=self.greet)
        self.back_button.pack(side=tk.LEFT)

        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.pack(side=tk.LEFT)

    def greet(self):
        print("grettings!")
root = tk.Tk()
my_gui = GraphicSetup(root)
root.mainloop()

