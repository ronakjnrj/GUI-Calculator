from tkinter import *
root = Tk()
root.geometry("570x600")
root.resizable(False,False)
root.title("Calculator")
root.configure(bg="#17161b")

equation = ""
def clear():
    global equation
    equation = ""
    result.config(text=equation)

def show(value):
    global equation
    equation += value
    result.config(text=equation)

def delt():
    if len(equation) > 0:
        return equation[:-1]
    return equation 

def calc():
    global equation
    res = ""
    if equation != "":
        try:
            res = eval(equation)
        except:
            res = "error"
            equation = ""
    result.config(text=res)

result = Label(root, width=25, height=2, text="", font=("arial 30"))
result.pack()

Button(root, text = "C", width=5, height=1, bg="#3697f5", fg="#fff", font=("arial 30"), bd=1, command=lambda: clear()).place(x=10, y=100)
Button(root, text = "<", width=5, height=1, bg="#2a2d36", fg="#fff", font=("arial 30"), bd=1, command=lambda: delt()).place(x=150, y=100)
Button(root, text = "\u00f7", width=5, height=1, bg="#2a2d36", fg="#fff", font=("arial 30"), bd=1, command=lambda: show("/")).place(x=290, y=100)
Button(root, text = "\u00D7", width=5, height=1, bg="#2a2d36", fg="#fff", font=("arial 30"), bd=1, command=lambda: show("*")).place(x=430, y=100)

Button(root, text = "7", width=5, height=1, bg="#2a2d36", fg="#fff", font=("arial 30"), bd=1, command=lambda: show("7")).place(x=10, y=200)
Button(root, text = "8", width=5, height=1, bg="#2a2d36", fg="#fff", font=("arial 30"), bd=1, command=lambda: show("8")).place(x=150, y=200)
Button(root, text = "9", width=5, height=1, bg="#2a2d36", fg="#fff", font=("arial 30"), bd=1, command=lambda: show("9")).place(x=290, y=200)
Button(root, text = "-", width=5, height=1, bg="#2a2d36", fg="#fff", font=("arial 30"), bd=1, command=lambda: show("-")).place(x=430, y=200)

Button(root, text = "4", width=5, height=1, bg="#2a2d36", fg="#fff", font=("arial 30"), bd=1, command=lambda: show("4")).place(x=10, y=300)
Button(root, text = "5", width=5, height=1, bg="#2a2d36", fg="#fff", font=("arial 30"), bd=1, command=lambda: show("5")).place(x=150, y=300)
Button(root, text = "6", width=5, height=1, bg="#2a2d36", fg="#fff", font=("arial 30"), bd=1, command=lambda: show("6")).place(x=290, y=300)
Button(root, text = "+", width=5, height=1, bg="#2a2d36", fg="#fff", font=("arial 30"), bd=1, command=lambda: show("+")).place(x=430, y=300)

Button(root, text = "1", width=5, height=1, bg="#2a2d36", fg="#fff", font=("arial 30"), bd=1, command=lambda: show("1")).place(x=10, y=400)
Button(root, text = "2", width=5, height=1, bg="#2a2d36", fg="#fff", font=("arial 30"), bd=1, command=lambda: show("2")).place(x=150, y=400)
Button(root, text = "3", width=5, height=1, bg="#2a2d36", fg="#fff", font=("arial 30"), bd=1, command=lambda: show("3")).place(x=290, y=400)
Button(root, text = "=", width=5, height=3, bg="#ffa50a", fg="#fff", font=("arial 30"), bd=1, command=lambda: calc()).place(x=430, y=400)

Button(root, text = "0", width=5, height=1, bg="#2a2d36", fg="#fff", font=("arial 30"), bd=1, command=lambda: show("0")).place(x=10, y=500)
Button(root, text = ".", width=5, height=1, bg="#2a2d36", fg="#fff", font=("arial 30"), bd=1, command=lambda: show(".")).place(x=150, y=500)
Button(root, text = "%", width=5, height=1, bg="#2a2d36", fg="#fff", font=("arial 30"), bd=1, command=lambda: show(".")).place(x=290, y=500)

root.mainloop()