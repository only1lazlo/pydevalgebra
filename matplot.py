import tkinter as tk
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = tk.Tk()
root.geometry("400x400")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()

mybutton = tk.Button(root, text="Graph", command=graph)
mybutton.pack()

root.mainloop()