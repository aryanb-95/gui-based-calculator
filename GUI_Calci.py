"""
    Project Name: GUI based Calculator
    Created by: Aryan Bhatt
"""
from tkinter import *
from PIL import Image, ImageTk, ImageSequence

root=Tk()
# note this is the only part in this code where i have used a LLM is animation effect for '=' button
# Load the raw GIF file
gif_file = Image.open("gradient_orange.gif")
frames = []
gif_resized = False

def loop(i=0):
    global gif_resized, frames
    try:
        # 1. Dynamically match the size of your text buttons automatically
        if not gif_resized:
            # We use your 'btn_equal' grid cell size to get the exact layout pixels
            root.update_idletasks() 
            w = btn_equal.winfo_width()
            h = btn_equal.winfo_height()
            
            # Re-populate frames with the perfect pixel dimensions
            frames = [ImageTk.PhotoImage(f.copy().resize((w, h))) for f in ImageSequence.Iterator(gif_file)]
            gif_resized = True

        # 2. Animate the button
        btn_equal.config(image=frames[i])
        root.after(100, loop, (i + 1) % len(frames))
        
    except (NameError, IndexError):
        # If the button isn't built yet, wait 50ms and try again
        root.after(30, loop, i)

# Start the automated sizing and loop sequence
loop()



# # The rest of the implementation is independently written by me without using any LLM.
num1=num2=res=None

root.title("Calculator")
root.geometry("380x650")
root.resizable(0,0)
root.configure(bg="black")

result_label = Label(root,text="",bg="black",fg="white")
result_label.config(font=("Helvetica",39,'bold'))
result_label.grid(row=0,column=0,columnspan=5,pady=(65,25),padx=(10),sticky='w')

def get_digit(digit):
    result_label["text"]+=str(digit)
def display_op(opr):
    global op,num1
    op=opr
    num1=int(result_label["text"])
    result_label["text"]+=opr

def operation():
    if op=="+":
        num2=int(result_label["text"].split("+")[1])
        res=num1+num2
        clear()
        result_label["text"]+=str(res)
    
    elif op=="-":
        num2=int(result_label["text"].split("-")[1])
        res=num1-num2
        clear()
        result_label["text"]+=str(res)

    elif op=="x":
        num2=int(result_label["text"].split("x")[1])
        res=num1*num2
        clear()
        result_label["text"]+=str(res)
    
    else:
        num2=int(result_label["text"].split("÷")[1])
        if num2==0:
            clear()
            result_label["text"]+="Error"
        else:
            clear()
            res=round(num1/num2,3)
            result_label["text"]+=str(res)

def backspace():
    txt=result_label["text"]
    if txt:
        result_label["text"]=result_label["text"][:-1]

def clear():
    result_label["text"]=""

btn7=Button(root,text="7",bg="#2E2F38",fg="white",width=4,height=2,padx=8.5,command=lambda: get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=("Helvetica",22))

btn8=Button(root,text="8",bg="#2E2F38",fg="white",width=4,height=2,padx=9.2,command=lambda: get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=("Helvetica",22))

btn9=Button(root,text="9",bg="#2E2F38",fg="white",width=4,height=2,padx=9.8,command=lambda: get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=("Helvetica",22))

btn_add=Button(root,text="+",bg="#FF9F0A",fg="white",width=4,height=2,padx=9, command=lambda: display_op("+"))
btn_add.grid(row=1,column=3)
btn_add.config(font=("Helvetica",22))

btn4=Button(root,text="4",bg="#2E2F38",fg="white",width=4,height=2,padx=8.5,command=lambda: get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=("Helvetica",22))

btn5=Button(root,text="5",bg="#2E2F38",fg="white",width=4,height=2,padx=9.2,command=lambda: get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=("Helvetica",22))

btn6=Button(root,text="6",bg="#2E2F38",fg="white",width=4,height=2,padx=9.8,command=lambda: get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=("Helvetica",22))

btn_sub=Button(root,text="-",bg="#FF9F0A",fg="white",width=4,height=2,padx=9, command=lambda: display_op("-"))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=("Helvetica",22))

btn1=Button(root,text="1",bg="#2E2F38",fg="white",width=4,height=2,padx=8.5,command=lambda: get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=("Helvetica",22))

btn2=Button(root,text="2",bg="#2E2F38",fg="white",width=4,height=2,padx=9.2,command=lambda: get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=("Helvetica",22))

btn3=Button(root,text="3",bg="#2E2F38",fg="white",width=4,height=2,padx=9.8,command=lambda: get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=("Helvetica",22))

btn_mul=Button(root,text="x",bg="#FF9F0A",fg="white",width=4,height=2,padx=9, command=lambda: display_op("x"))
btn_mul.grid(row=3,column=3)
btn_mul.config(font=("Helvetica",22))

btn0=Button(root,text="0",bg="#2E2F38",fg="white",width=4,height=2,padx=8.5,command=lambda: get_digit(0))
btn0.grid(row=4,column=0)
btn0.config(font=("Helvetica",22))

btn_equal = Button(root, text="=", compound="center", bg="#4E505F", fg="white", command=operation)
btn_equal.grid(row=5, column=2, columnspan=2, sticky="nsew")
btn_equal.config(font=("Helvetica", 22))

btn_div=Button(root,text="÷",bg="#FF9F0A",fg="white",width=4,height=2,padx=9, command=lambda: display_op("÷"))
btn_div.grid(row=4,column=3)
btn_div.config(font=("Helvetica",22))

btn_cut=Button(root,text="⌫",bg="#4E505F",fg="white",width=8,height=2,padx=9.2,command=backspace)
btn_cut.grid(row=5,column=0,columnspan=2,sticky="nsew")
btn_cut.config(font=("Helvetica",22))

btn_C=Button(root,text="C",bg="#4E505F",fg="white",width=8,height=2,padx=9.2,command=clear)
btn_C.grid(row=4,column=1,columnspan=2,sticky="nsew")
btn_C.config(font=("Helvetica",22))



root.mainloop()
