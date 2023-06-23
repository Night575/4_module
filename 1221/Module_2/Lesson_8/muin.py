from Lesson_8 import get_course, today
from tkinter import *


window = Tk()
window.geometry('500x500')
window.title('Банк имени меня')
window.resizable(width=False, height=False)


image = PhotoImage(file=r'C:\PycharmProject\1221\Lesson_8\logo.png')

label_img = Label(window, image=image)

label_img.place(x=0, y=0)

label_title = Label(window, text='БАНК 404', font='Arial 32', bg='cyan2')
label_title.place(x=200, y=50)

label_currency = Label(window, text=f'Курсы на {today}:', font='Arial 22')
label_currency.place(x=20, y=180)

dollar_info = f'{get_course("R01235").get("name")} {get_course("R01235").get("value")}'
dollar_label = Label(window, text=dollar_info, font="Arial 18", bg='red')
dollar_label.place(x=40, y=220)

euro_info = f'{get_course("R01239").get("name")} {get_course("R01239").get("value")}'
euro_label = Label(window, text=euro_info, font="Arial 18", bg='yellow')
euro_label.place(x=40, y=260)

yuan_info = f'{get_course("R01375").get("name")} {get_course("R01375").get("value")}'
yuan_label = Label(window, text=yuan_info, font="Arial 18", bg='green')
yuan_label.place(x=40, y=300)

entry = Entry(font='Arial 22')
entry.place(x=40, y=400)

y = 40

def search():
    global y

    currency_id = entry.get()
    currency_info = get_course(currency_id)

    currency_name = currency_info.get('name')
    currency_value = currency_info.get('value')

    currency_str = f'{currency_name} {currency_value}'
    currency_label = Label(window, text=currency_str, font="Arial 18")
    currency_label.place(x=40, y=300 + y)
    y += 40


button = Button(text="Найти", command=search)
button.place(x=400, y=400)


window.mainloop()
