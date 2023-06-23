from tkinter import *

window = Tk()
window.geometry("800x600")


canvas = Canvas(window, width=800, height=600, bg="white")
canvas.pack()


canvas.create_rectangle(250, 400, 300, 300, fill='brown', outline='black')
canvas.create_polygon(150, 300, 275, 30, 400, 300, fill='green', outline='black')


window.mainloop()