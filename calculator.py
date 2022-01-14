from tkinter import *

root = Tk()
root.title("Simple Calculator")
# entry widget 
e = Entry(root, width = 40, borderwidth=5)
e.grid(row = 0, column=0, columnspan=8, rowspan=1, padx=20, pady=10)

def buttonClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def buttonAdd():
    firstNumber = e.get()
    global fNum
    fNum = int(firstNumber)
    global math
    math = "addition"
   
    e.delete(0, END)

def buttonEqual():
    secondNum = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, fNum + int(secondNum))
    
    if math == "subtraction":
        e.insert(0, fNum - int(secondNum))
    
    if math == "multiplication":
        e.insert(0, fNum * int(secondNum))

    if math == "division":
        e.insert(0, fNum / int(secondNum))

    
def buttonClear():
    e.delete(0, END)
def buttonDivide():
    firstNumber = e.get()
    global fNum
    fNum = int(firstNumber)
    global math
    math = "division"
    e.delete(0, END)
def buttonMultiply():
    firstNumber = e.get()
    global fNum
    fNum = int(firstNumber)
    global math
    math = "multiplication"
    e.delete(0, END)
def buttonSubtract():
    firstNumber = e.get()
    global fNum
    fNum = int(firstNumber)
    global math
    math = "subtraction"
    e.delete(0, END)

button1 = Button(root, text="1", bg='black', fg='white', padx=40, pady=20, command=lambda: buttonClick(1))
button2 = Button(root, text="2", bg='black', fg='white',padx=40, pady=20, command=lambda: buttonClick(2))
button3 = Button(root, text="3", bg='black', fg='white',padx=40, pady=20, command=lambda: buttonClick(3))
button4 = Button(root, text="4", bg='black', fg='white',padx=40, pady=20, command=lambda: buttonClick(4))
button5 = Button(root, text="5", bg='black', fg='white',padx=40, pady=20, command=lambda: buttonClick(5))
button6 = Button(root, text="6", bg='black', fg='white',padx=40, pady=20, command=lambda: buttonClick(6))
button7 = Button(root, text="7", bg='black', fg='white',padx=40, pady=20, command=lambda: buttonClick(7))
button8 = Button(root, text="8", bg='black', fg='white',padx=40, pady=20, command=lambda: buttonClick(8))
button9 = Button(root, text="9", bg='black', fg='white',padx=40, pady=20, command=lambda: buttonClick(9))
button0 = Button(root, text="0", bg='black', fg='white',padx=40, pady=20, command=lambda: buttonClick(0))
buttonMultiply = Button(root, text="x", bg="#231F20", fg="white", padx=40, pady=20, command=buttonMultiply)
buttonSubtract = Button(root, text="-", bg="#231F20", fg="white",padx=40, pady=20, command=buttonSubtract)
buttonAdd = Button(root, text="+", bg="#231F20", fg="white",padx=40, pady=20, command = buttonAdd)
buttonEqual = Button(root, text = "=", bg="#231F20", fg="white",padx=40, pady=20, command=buttonEqual)
buttonDivide = Button(root, text="÷", bg="#231F20", fg="white", padx=40, pady=20, command=buttonDivide)
buttonClear = Button(root, text = "CE", bg="#1F2322", fg="white", padx=40, pady=20, command=buttonClear)

# place button on screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
buttonDivide.grid(row=1, column=3)
buttonMultiply.grid(row=2, column=3)
buttonAdd.grid(row=3, column=3)
buttonEqual.grid(row=4, column=3)
buttonSubtract.grid(row=4, column=2)
buttonClear.grid(row=4, column=1)

root.mainloop()