#!/usr/bin/env python
# coding: utf-8

# In[50]:


def multiplication_table():
    n=int(entry_place.get())
    i=1
    result=""
    while(i<11):
        y=f"{n} x {i} = {n*i}\n"
        i+=1
        result+=y+"\n"
    resultlabel.config(text=result)

# Import library
import tkinter as tn

# Create a window
window=tn.Tk()

# Change title
window.title("Multiplication Table")

# Change size
window.geometry('550x750')
# Add Text label 
tn.Label(window,text="MULTIPLICATION TABLE GENERATOR", bg="red",font=("Times New Roman",15)).place(x=100,y=10)

tn.Label(window,text="Enter a number : ",font=("Times New Roman",15)).place(x=50,y=70)

entry_place=tn.Entry(window,bg="cyan",font=("Times New Roman",14))
entry_place.place(x=220,y=70)


# Button
tn.Button(window,text="GENERATE TABLE",bg="green",width=20,font=("Times New Roman",18),command=multiplication_table).place(x=150,y=130)

resultlabel=tn.Label(window,text="",bg="white",font=("Times New Roman",15))
resultlabel.place(x=220,y=205)



# Display window
window.mainloop()


# ### 
