import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry("400x400")

clicked = tk.StringVar()
clicked.set("Monday")


drop = tk.OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

drop.pack()



root.mainloop()