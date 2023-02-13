import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry("400x400")

def show():
    my_label = tk.Label(root, text=var.get()).pack()
    
    
    
#var = tk.IntVar()
var = tk.StringVar()

c = tk.Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off")
c.pack()



my_button = tk.Button(root, text="Show Selection", command=show).pack()



root.mainloop()