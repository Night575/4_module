from tkinter import *
import random


window = Tk()
window.geometry("600x600")
canvas = Canvas(window, width=600, height=600)
canvas.pack()

background = PhotoImage(file=r"C:\PycharmProject\1221\Lesson_4\bg_2 (1).png")


class Knight:
    def __init__(self):
        self.x = 150
        self.y = 350
        self.v = 0
        self.v1 = 0
        self.photo = PhotoImage(file=r"C:\PycharmProject\1221\Lesson_4\knight (1).png")

    def up(self, event):
        self.v = -3
        if knight.y < 50:
            self.v = 0

    def down(self, event):
        self.v = 3
        if knight.y > 550:
            self.v = 0

    def stop(self, event):
        self.v = 0; self.v1 = 0

    def left(self, event):
        self.v1 = -3

    def right(self, event):
        self.v1 = 3


knight = Knight()


class Dragon:
    def __init__(self):
        self.x = random.randint(550, 600)
        self.y = random.randint(50, 550)
        self.v = random.randint(1, 3)
        self.photo = PhotoImage(file=r"C:\PycharmProject\1221\Lesson_4\dragon (1).png")


dragons = []
for i in range(5):
    dragons.append(Dragon())


def game():
    canvas.delete("all")
    canvas.create_image(300, 300, image=background)
    canvas.create_image(knight.x, knight.y, image=knight.photo)

    for dragon in dragons:
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)

        dragon.x -= dragon.v

        if ((knight.x - dragon.x) ** 2 + (knight.y - dragon.y) ** 2) ** 0.5 < 50:
            dragons.remove(dragon)

        if dragon.x < 50:
            return lose()
        if knight.y < 55:
            knight.y = 55
        if knight.y > 550:
            knight.y = 550
        if knight.x < 40:
            knight.x = 40
        if knight.x > 560:
            knight.x = 560

    knight.y += knight.v
    knight.x += knight.v1
    print(f"{knight.y}  {knight.x}")

    if len(dragons) == 0:
        return win()

    window.after(10, game)


def win():
    canvas.create_text(300, 300, text="Вы победили!", font="Verdana 42")


def lose():
    canvas.create_text(300, 300, text="Вы проиграли!", font="Verdana 42")


window.bind("<Key-Up>", knight.up)
window.bind("<Key-Down>", knight.down)
window.bind("<KeyRelease>", knight.stop)
window.bind("<Key-Left>", knight.left)
window.bind("<Key-Right>", knight.right)

game()
window.mainloop()
