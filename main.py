from tkinter import *
import tkinter.messagebox

root = Tk()

# ===== TODO ======
# add zero devision error
# add error for blank place
# make ui better

# ===================== Variables =====================
res_val = StringVar()
color = '#bababa'
f_num = StringVar()


# ===================== Settings =====================
root.title('calculator')
root.geometry('350x410')
root.resizable(height=False, width=False)
root.config(bg=color)


# ===================== Functions =====================
def errorMsg(msg):
    if msg == 'error':
        tkinter.messagebox.showerror(title='Error', message='Something went wrong')
    elif msg == 'ZeroDivision':
        tkinter.messagebox.showerror(title='ZeroDivision Error', message='can not divide by zero')


def click_btn(number):
    current = inputBox.get()
    inputBox.delete(0, END)
    inputBox.insert(0, str(current) + str(number))


def clear_button():
    inputBox.delete(0, END)


def plus():
    global f_num
    first_value = inputBox.get()
    f_num = float(first_value)
    inputBox.delete(0, END)


def equal():
    second_number = inputBox.get()
    inputBox.delete(0, END)
    inputBox.insert(0, f_num + float(second_number))



# ===================== Frames =====================
inputFrame = Frame(root, bg=color, height=83.33, width=400)
inputFrame.pack()


row1 = Frame(root, bg=color, height=83.33, width=400)
row1.pack()

row2 = Frame(root, bg=color, height=83.33, width=400)
row2.pack()

row3 = Frame(root, bg=color, height=83.33, width=400)
row3.pack()

row4 = Frame(root, bg=color, height=400, width=500)
row4.pack()

# ===================== Entry =====================
inputBox = Entry(inputFrame, width=20, font=('Arial', 30))
inputBox.pack(side=LEFT, padx=7, pady=7)


# ===================== Buttons =====================
num1 = Button(row1, text='1', height=3, width=4, command=lambda: click_btn(1))
num1.pack(side=LEFT, padx=7, pady=7)

num2 = Button(row1, text='2', height=3, width=4, command=lambda: click_btn(2))
num2.pack(side=LEFT, padx=7, pady=7)

num3 = Button(row1, text='3', height=3, width=4, command=lambda: click_btn(3))
num3.pack(side=LEFT, padx=7, pady=7)


num4 = Button(row2, text='4', height=3, width=4, command=lambda: click_btn(4))
num4.pack(side=LEFT, padx=7, pady=7)

num5 = Button(row2, text='5', height=3, width=4, command=lambda: click_btn(5))
num5.pack(side=LEFT, padx=7, pady=7)

num6 = Button(row2, text='6', height=3, width=4, command=lambda: click_btn(6))
num6.pack(side=LEFT, padx=7, pady=7)

num7 = Button(row3, text='7', height=3, width=4, command=lambda: click_btn(7))
num7.pack(side=LEFT, padx=7, pady=7)

num8 = Button(row3, text='8', height=3, width=4, command=lambda: click_btn(8))
num8.pack(side=LEFT, padx=7, pady=7)

num9 = Button(row3, text='9', height=3, width=4, command=lambda: click_btn(9))
num9.pack(side=LEFT, padx=7, pady=7)

num0 = Button(row4, text='0', height=3, width=12, command=lambda: click_btn(0))
num0.pack(side=LEFT, padx=7, pady=7)



clearBtn = Button(row3, text='clear', height=3, width=2, command=clear_button)
clearBtn.pack(side=LEFT, padx=7, pady=7)

resultBtn = Button(row2, text='=', height=3, width=2, command=equal)
resultBtn.pack(side=LEFT, padx=7, pady=7)

plusBtn = Button(row1, text='+', height=3, width=2, command=lambda: plus())
plusBtn.pack(side=LEFT, padx=7, pady=7)



root.mainloop()
