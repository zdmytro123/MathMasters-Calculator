from tkinter import *
import tkinter as tk

# Create the root window
root = tk.Tk()
root.geometry("1920x1080")
root.configure(background="lime green")
root.title("MATHMASTERS CALCULATOR")


def click_number(num):
    # Handle numeric button clicks here
    output.config(text=output.cget("text") + str(num))
    pass

def click_plus():
    # Handle "+" button clicks here
    output.config(text=output.cget("text") + "+")
    pass

def click_minus():
    # Handle "-" button clicks here
    output.config(text=output.cget("text") + "-")
    pass
def click_multiply():
    # Handle "*" button clicks here
    output.config(text=output.cget("text") + "*")
    pass
def click_divide():
    # Handle "/" button clicks here
    output.config(text=output.cget("text") + "/")
    pass
def click_power():
    # Handle "^" button clicks here
    output.config(text=output.cget("text") + "^")
    pass
def click_comma():
    # Handle "," button clicks here
    output.config(text=output.cget("text") + ".")
    pass
def click_equals():
    # Handle "=" button clicks here
    output.config(text=eval(output.cget("text")))
    
    pass
def click_clear():
    # Handle "C" button clicks here
    output.config(text="")
    pass
def  clear_last():
    # Handle "CL" button clicks here
    output.config(text=output.cget("text")[:-1])
    pass




# Create the numeric buttons
for i in range(9):
    button = tk.Button(root, text=str(i+1), width=5, height=2,cursor="hand2",background="pink",foreground="green", font=("Arial", 12), borderwidth=2, relief="groove", command=lambda i=i: click_number(i+1))
    button.place(x=20 + 50 * (i % 3), y=50 + 50 * (i // 3))
for label in [ "zero_button","plus_button", "minus_button", "multiply_button", "divide_button", "power_button", "equals-button", "clear_buton", "clear_last_button","comma_button","RBrachet_button","LBrachet_button"]:
    globals()[label] = tk.Button(root, width=5, height=2,cursor="hand2",background="pink")
   

zero_button = tk.Button(root, text="0",width=5, height=2,cursor="hand2",background="pink",foreground="green", font=("Arial", 12), borderwidth=2, relief="groove", command=lambda: click_number(0))
zero_button.place(x=20 + 50 * (7 % 3), y=200)

plus_button = tk.Button(root, text="+",width=5, height=2,cursor="hand2",background="pink",foreground="green", font=("Arial", 12), borderwidth=2, relief="groove", command=click_plus)
plus_button.place(x=170, y=50)

minus_button = tk.Button(root, text="-",width=5, height=2,cursor="hand2",background="pink",foreground="green", font=("Arial", 12), borderwidth=2, relief="groove", command=click_minus)
minus_button.place(x=170, y=100)

multiply_button = tk.Button(root, text="*",width=5, height=2,cursor="hand2",background="pink",foreground="green", font=("Arial", 12), borderwidth=2, relief="groove", command=click_multiply)
multiply_button.place(x=170, y=150)

divide_button = tk.Button(root, text="/",width=5, height=2,cursor="hand2",background="pink",foreground="green", font=("Arial", 12), borderwidth=2, relief="groove", command=click_divide)
divide_button.place(x=170, y=200)

power_button = tk.Button(root, text="^",width=5, height=2,cursor="hand2",background="pink",foreground="green", font=("Arial", 12), borderwidth=2, relief="groove", command=click_power)
power_button.place(x=20 + 50 * (9 % 3), y=300)

equals_button = tk.Button(root, text="=",width=5, height=2,cursor="hand2",background="pink",foreground="green", font=("Arial", 12), borderwidth=2, relief="groove", command=click_equals)
equals_button.place(x=170, y=250)

clear_button = tk.Button(root, text="C",width=5, height=2,cursor="hand2",background="pink",foreground="green", font=("Arial", 12), borderwidth=2, relief="groove", command=click_clear)
clear_button.place(x=20 + 50 * (9 % 3), y=250)

clear_last_button = tk.Button(root,text="CL",width=5, height=2,cursor="hand2",background="pink",foreground="green", font=("Arial", 12), borderwidth=2, relief="groove", command=clear_last)
clear_last_button.place(x=20 + 50 * (7 % 3), y=250)

comma_button = tk.Button(root, text=",",width=5, height=2,cursor="hand2",background="pink",foreground="green", font=("Arial", 12), borderwidth=2, relief="groove", command=lambda: click_number(".") )
comma_button.place(x=20 + 50 * (8 % 3), y=250)

RBrachet_button = tk.Button(root, text=")",width=5, height=2,cursor="hand2",background="pink",foreground="green", font=("Arial", 12), borderwidth=2, relief="groove", command=lambda: click_number(")"))
RBrachet_button.place(x=20 + 50 * (8 % 3), y=200)

LBrachet_button = tk.Button(root, text="(",width=5, height=2,cursor="hand2",background="pink",foreground="green", font=("Arial", 12), borderwidth=2, relief="groove", command=lambda: click_number("("))
LBrachet_button.place(x=20 + 50 * (9 % 3), y=200)


# Create the output label
output = tk.Label(root, text="", width=30, height=2, bg="pink", fg="black", font= 16, relief="sunken", borderwidth=2, anchor="e")
output_frame = tk.Frame(root, width=200, height=50, bg="green")
output_frame.config(highlightbackground="black", highlightcolor="black", highlightthickness=1)
output.place(x=20, y=200)



output.pack()
root.mainloop()
