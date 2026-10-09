import tkinter as tk
from tkinter import ttk , messagebox , Entry, Button ,Tk
from tkinter.scrolledtext import ScrolledText
def delTopLine():
    st.delete('1.0','2.0')

def clear():
    st.delete('1.0','end')

def copyall():
    thetext = st.get('1.0','end')
    st2.delete('1.0','end')
    st2.insert('1.0',thetext)

def copytext():
    thetext = st.selection_get()
    st2.insert('1.0',thetext)

root = tk.Tk()
root.title("Test Scrolled Text")
root.geometry('300x300+100+200')


st = ScrolledText(root,width=20,height=5)
st.place(x=10,y=10)

st2 = ScrolledText(root,width=20,height=5)
st2.place(x=10,y=100)
# st.insert('1.0',"Line1 col0\n")
# st.insert('1.0',"Line2 col0\n")
# st.insert('1.0',"Line3 col0\n")
# st.insert('1.0',"Line4 col0\n")
# st.insert('1.0',"Line5 col0\n")






btn1 = ttk.Button(root,text='copyall',command=lambda:copyall())
btn1.place(x=200,y=10)

btn2 = ttk.Button(root,text='copytext',command=lambda:copytext())
btn2.place(x=200,y=50)













root.mainloop()