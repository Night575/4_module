from tkinter import *
import random

window = Tk()
window.geometry("600x600")
window.title("Алхимия")


class Dust:
    image = PhotoImage(file=r'C:\PycharmProject\1221\3_les_7\dust.png').subsample(4, 4)


class Steam:
    image = PhotoImage(file=r'C:\PycharmProject\1221\3_les_7\aroma.png').subsample(4, 4,)


class Water:
    image = PhotoImage(file=r'C:\PycharmProject\1221\3_les_7\water.png').subsample(4, 4,)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam


class Fire:
    image = PhotoImage(file=r'C:\PycharmProject\1221\3_les_7\fire.png').subsample(4, 4,)

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam


class Wind:
    image = PhotoImage(file=r'C:\PycharmProject\1221\3_les_7\wind.png').subsample(4, 4,)

    def __add__(self, other):
        if isinstance(other, Ground):
            return Dust

class Ground:
    image = PhotoImage(file=r'C:\PycharmProject\1221\3_les_7\ground.png').subsample(4, 4,)

    def __add__(self, other):
        if isinstance(other, Wind):
            return Dust


canvas = Canvas(width=600, height=600)
canvas.pack()

elements = [Wind(), Fire(), Water(), Ground()]

for elem in elements:
    canvas.create_image(random.randint(50, 550), random.randint(50, 550), image=elem.image)


def move(event):
    images_ids = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    if len(images_ids) == 2:
        elem_id_1, elem_id_2 = images_ids[0], images_ids[1]
        elem_id_3, elem_id_4 = images_ids[2], [3]
        elem_1 = elements[elem_id_1 - 1]
        elem_2 = elements[elem_id_2 - 1]
        elem_3 = elements[elem_id_3 - 1]
        elem_4 = elements[elem_id_4 - 1]

        new_elem = elem_1 + elem_2
        new_elem2 = elem_3 + elem_4
        if new_elem not in elements:
            elements.append(new_elem, new_elem2)
            canvas.create_image(event.x, event.y, image=new_elem.image)
    canvas.coords(images_ids, event.x, event.y)


window.bind("B1-Motion", move)

window.mainloop()