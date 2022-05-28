import tkinter as tk
from PIL import ImageTk, Image

path = 'C:/Users/edwin/OneDrive/Escritorio/Tkinter Python/astronauta.jfif'

root = tk.Tk()
img = ImageTk.PhotoImage(Image.open(path))

panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

root.mainloop()