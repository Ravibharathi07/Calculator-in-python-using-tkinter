import tkinter

root= tkinter.Tk()
root.title("calculator🧮")
expression = ""
def add(val):    
    global expression
    expression += val
    lable_result.config(text=expression)

    #print(expression)

def clear():
    global expression
    expression=""
    lable_result.config(text=expression)



def calculate():
    global expression
    result= eval(expression)
    lable_result.config(text=result)
    expression= str(result)





lable_result = tkinter.Label(root,text="Result")
lable_result.grid(row=0,column=0,columnspan=4)
lable_result.config(bg="green")
button_item1 = tkinter.Button(root,text="1",command=lambda:add("1"))
button_item1.grid(row=1,column=0)

button_item2 = tkinter.Button(root,text="2",command=lambda:add("2"))
button_item2.grid(row=1,column=1)

button_item3 = tkinter.Button(root,text="3",command=lambda:add("3"))
button_item3.grid(row=1,column=2)

button_itemDiv = tkinter.Button(root,text="/",command=lambda:add("/"))
button_itemDiv.grid(row=1,column=3)

button_item4 = tkinter.Button(root,text="4",command=lambda:add("4"))
button_item4.grid(row=2,column=0)

button_item5 = tkinter.Button(root,text="5",command=lambda:add("5"))
button_item5.grid(row=2,column=1)

button_item6 = tkinter.Button(root,text="6",command=lambda:add("6"))
button_item6.grid(row=2,column=2)

button_itemMul = tkinter.Button(root,text="*",command=lambda:add("*"))
button_itemMul.grid(row=2,column=3)

button_item7 = tkinter.Button(root,text="7",command=lambda:add("7"))
button_item7.grid(row=3,column=0)

button_item8 = tkinter.Button(root,text="8",command=lambda:add("8"))
button_item8.grid(row=3,column=1)

button_item9 = tkinter.Button(root,text="9",command=lambda:add("9"))
button_item9.grid(row=3,column=2)

button_itemSub = tkinter.Button(root,text="-",command=lambda:add("-"))
button_itemSub.grid(row=3,column=3)

button_clear = tkinter.Button(root,text="C",command=lambda:clear())
button_clear.grid(row=4,column=0)

button_item0 = tkinter.Button(root,text="0",command=lambda:add("0"))
button_item0.grid(row=4,column=1)

button_dot = tkinter.Button(root,text=".",command=lambda:add("."))
button_dot.grid(row=4,column=2)

button_itemAdd = tkinter.Button(root,text="+",command=lambda:add("+"))
button_itemAdd.grid(row=4,column=3)

button_equals = tkinter.Button(root,text="=",command=lambda:calculate())
button_equals.grid(row=5,column=0,columnspan=4)











root.mainloop()