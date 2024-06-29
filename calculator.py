from tkinter import *
# ------ window ------

root = Tk()
root.title('Calculator')
root.geometry('420x550')
root.resizable(False, False)
root.configure(background='black')

# ------ functionality ------

num_getted= ""
equation_text= ""
def num_setter(num):                    # shows digits you are clicking on screen 
    global equation_text
    global num_getted
    num_getted = num_getted + str(num)
    live.set(num_getted)

def addition():                         # " + " operation
    global num_getted
    global equation_text
    equation_text = equation_text + num_getted
    equation_text = equation_text + "+"
    num_getted=""

def subtraction():                      # " - " operation
    global num_getted
    global equation_text
    equation_text = equation_text + num_getted
    equation_text = equation_text + "-"
    num_getted=""

def multiply():                         # " * " operation
    global num_getted
    global equation_text
    equation_text = equation_text + num_getted
    equation_text = equation_text + "*"
    num_getted=""

def divition():                         # " / " opperation
    global num_getted
    global equation_text
    equation_text = equation_text + num_getted
    equation_text = equation_text + "/"
    num_getted=""

def reslut():                           # shows reslut
    global equation_text
    global num_getted
    equation_text = equation_text + num_getted

    try:
        if equation_text == "":
            live.set("")
        else:
            res = str(eval(equation_text))
            live.set(res)
            equation_text=str(res)
            num_getted=""
    except SyntaxError:
        live.set("Error !")
        equation_text=""
    except ZeroDivisionError:
        live.set("Error  !")
        equation_text=""
        num_getted=""

def AC():                               # it reset's calculator
    global num_getted
    global equation_text
    num_getted = ""
    equation_text = ""
    live.set(num_getted)

# ------ calculator num screen ------

live=StringVar()
pr = Label(root, textvariable=live, font='Arial 40 ', fg="white", bg="black", anchor=S )
pr.place(x=5, y=35, )

# ------ num pad ------

numPad = Frame(root, background='black', height=430, width=350)
numPad.place(x=10, y=130)

num7 = Button(numPad, text='7', font='Helvetica 20 ', padx=24, pady=24,
              bg='gray20', fg='white', width=3, command=lambda: num_setter(7))
num7.grid(row=1, column=1)

num8 = Button(numPad, text='8', font='Helvetica 20 ', padx=24, pady=24,
              bg='gray20', fg='white', width=3, command=lambda: num_setter(8))
num8.grid(row=1, column=2)

num9 = Button(numPad, text='9', font='Helvetica 20 ', padx=24, pady=24,
              bg='gray20', fg='white', width=3, command=lambda: num_setter(9))
num9.grid(row=1, column=3)

num4 = Button(numPad, text='4', font='Helvetica 20 ', padx=24, pady=24,
              bg='gray20', fg='white', width=3, command=lambda: num_setter(4))
num4.grid(row=2, column=1)

num5 = Button(numPad, text='5', font='Helvetica 20 ', padx=24, pady=24,
              bg='gray20', fg='white', width=3, command=lambda: num_setter(5))
num5.grid(row=2, column=2)

num6 = Button(numPad, text='6', font='Helvetica 20 ', padx=24, pady=24,
              bg='gray20', fg='white', width=3, command=lambda: num_setter(6))
num6.grid(row=2, column=3)

num1 = Button(numPad, text='1', font='Helvetica 20 ', padx=24, pady=24,
              bg='gray20', fg='white', width=3, command=lambda: num_setter(1))
num1.grid(row=3, column=1)

num2 = Button(numPad, text='2', font='Helvetica 20 ', padx=24, pady=24,
              bg='gray20', fg='white', width=3, command=lambda: num_setter(2))
num2.grid(row=3, column=2)

num3 = Button(numPad, text='3', font='Helvetica 20 ', padx=24, pady=24,
              bg='gray20', fg='white', width=3, command=lambda: num_setter(3))
num3.grid(row=3, column=3)

num0 = Button(numPad, text='0', font='Helvetica 20 ', padx=24, pady=24,
              bg='gray20', fg='white', width=3, command=lambda: num_setter(0))
num0.place(x=0, y=306)

pointBtn = Button(numPad, text='.', font='Helvetica 20 ', padx=24, pady=24,
                  bg='gray20', fg='white', width=3, command=lambda: num_setter("."))
pointBtn.grid(row=5, column=2)

resBtn = Button(numPad, text='=', font='Helvetica 20 ', padx=24, pady=24,
                bg='orange', fg='white', width=3, command=lambda: reslut())
resBtn.grid(row=5, column=3)

# ------ func pad ------

funcPad = Frame(root, background='orange', height=430, width=80)
funcPad.place(x=325, y=129)

AC_Btn = Button(funcPad, text='AC', font='Helvetica 20 ', padx=15, pady=14,
                bg='gray60', fg='black', width=3, command=lambda : AC())
AC_Btn.pack(side=TOP)

devBtn = Button(funcPad, text='/', font='Helvetica 20 ', padx=15, pady=13,
                bg='orange', fg='white', width=3,command=lambda :divition())
devBtn.pack(side=TOP)

mulBtn = Button(funcPad, text='X', font='Helvetica 20 ', padx=15, pady=14,
                bg='orange', fg='white', width=3, command=lambda : multiply())
mulBtn.pack(side=TOP)

subBtn = Button(funcPad, text='-', font='Helvetica 20 ', padx=15, pady=14,
                bg='orange', fg='white', width=3, command=lambda : subtraction())
subBtn.pack(side=TOP)

plsBtn = Button(funcPad, text='+', font='Helvetica 20 ', padx=15, pady=14,
                bg='orange', fg='white', width=3, command= lambda : addition())
plsBtn.pack(side=TOP)

root.mainloop()
