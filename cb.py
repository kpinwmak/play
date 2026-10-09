import tkinter as tk
from tkinter import ttk 
from tkinter.scrolledtext import ScrolledText

def btn1click():
    st.insert('end',cmSubj.get()+'\n')








sublisst= ['English','Calculus','Football']

root = tk.Tk()
root.title("Test Combo")
root.geometry("500x300+600+200")






cmSubj=ttk.Combobox(root)
cmSubj['values']=sublisst
cmSubj.place(x=10,y=10)


btn1= ttk.Button(root,text="ลงทะเบียน",command=btn1click)
btn1.place(x=200,y=10)

st= ScrolledText(root,width=20,height=5)
st.place(x=300,y=10)


# ent1=ttk.Entry(root)
# ent1.place









root.mainloop()


