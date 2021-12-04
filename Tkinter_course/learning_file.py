from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.maxsize(700, 700)
root.minsize(500, 500)
label = Label(text="This is an Label")
label2 = Label(text="This is an Label 2")
# photo = PhotoImage(file="carolyn-christine-D7bmnvGJA2Q-unsplash.jpg")  # cant take .jpg files
image = Image.open("carolyn-christine-D7bmnvGJA2Q-unsplash.jpg")
photo = ImageTk.PhotoImage(image=image)
photo_label = Label(image=photo)
label.pack()
label2.pack()
photo_label.pack()
root.mainloop()
