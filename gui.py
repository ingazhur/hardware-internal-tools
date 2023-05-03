'''
create a GUI window, where you can select an image file from your computer
- there is a window and a side bar (200px) on the left side of the window
- the selected image shows up in the GUI window and is resized to fit the window
- the previous image is replaced with the new one if a new image is selected
- there is a button on the side bar that allows you to select an image file
- user can then select a point on the image
- once the user clicks on the point, the point coordinates are displayed on the side bar of the GUI window
'''

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

# create a window
window = tk.Tk()
window.title("Hardware internal tools")

# create a side bar
side_bar = tk.Frame(window, width=200, bg="grey")
side_bar.pack(side="left", fill="both")

# create a canvas
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack(side="right", fill="both", expand=True)

# create a panel
panel = None
image = None

# create a button that selects an image file
def select_image():
    # select an image from file and display it in the canvas
    # if a new image is selected, the previous image is deleted and replaced with the new image
    global panel
    global image

    # open a file dialog and allow the user to select an input image
    path = filedialog.askopenfilename()

    # ensure a file path was selected
    if len(path) > 0:
        # load the image from disk using PIL
        image = Image.open(path)
        # resize the image to fit the canvas
        image = image.resize((800, 600), Image.ANTIALIAS)
        # convert the images to PIL format...
        image = ImageTk.PhotoImage(image)
        # ...and then to ImageTk format
        #image = ImageTk.PhotoImage(image)
        # if the panel is not None, we need to initialize it
        if panel is None:
            panel = tk.Label(canvas, image=image)
            panel.image = image
            panel.pack(side="bottom", fill="both", expand="yes")
        # otherwise, simply update the panel
        else:
            panel.configure(image=image)
            panel.image = image

# when you click on the canvas, display the coordinates of the point at the side bar
def click(event):
    x = event.x
    y = event.y
    print(x, y)

canvas.bind("<Button-1>", click)
        
# display the button
btn = tk.Button(side_bar, text="Select an image", command=select_image)
btn.pack(side="top", fill="both", padx=10, pady=10)

window.mainloop()
