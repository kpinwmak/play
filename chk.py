import tkinter as tk
from tkinter import ttk 
from tkinter.scrolledtext import ScrolledText



def chkclicked():
    st.delete('1.0','end')
    thetext=f"{varchk1.get()}\n{varchk2.get()}\n{varchk3.get()}\n"
    st.insert('1.0',thetext)


def rdoClicked():
    st2.delete('1.0','end')	
    thetext=f"{varSize.get()} {varTop.get()}"
    st2.insert('1.0',thetext)




root = tk.Tk()
root.title("Test Combo")
root.geometry("500x300+600+200")

varchk1 = tk.StringVar()
chk1=ttk.Checkbutton(root,text='หมูแดง',onvalue='ใส่หมูแดง'
                     ,offvalue='ไม่ใส่หมูแดง',
                     variable=varchk1,
                     command=chkclicked)
chk1.place(x=10,y=10)
# varchk1.set('ใส่หมูแดง') #มันจะติ๊กไว้ให้เลย

varchk2 = tk.StringVar()
chk2=ttk.Checkbutton(root,text='หมูกรอบ',onvalue='ใส่หมูกรอบ'
                     ,offvalue='ไม่ใส่หมูกรอบ',
                     variable=varchk2,
                     command=chkclicked)
chk2.place(x=10,y=50)
# varchk2.set('ใส่หมูแดง') #มันจะติ๊กไว้ให้เลย

varchk3 = tk.StringVar()
chk3=ttk.Checkbutton(root,text='กุนเชียง',onvalue='ใส่กุนเชียง'
                     ,offvalue='ไม่ใส่กุนเชียง',
                     variable=varchk3,
                     command=chkclicked)
chk3.place(x=10,y=100)
# varchk3.set('ใส่หมูแดง') #มันจะติ๊กไว้ให้เลย

# ----------------------------------------------------------------------------------------------------------
varSize=tk.StringVar() # Radio ชุดเดียวกัน ใช้ Widget Variable เดียวกัน
rdo1=ttk.Radiobutton(root,text='ธรรมดา',value='จานธรรมดา',variable=varSize,command=rdoClicked)
rdo1.place(x=10,y=150)
rdo2=ttk.Radiobutton(root,text='พิเศษ',value='แบบพิเศษ',variable=varSize,command=rdoClicked)
rdo2.place(x=110,y=150)
varSize.set('จานธรรมดา')

# Radio คนละชุดจะเรียก Function เดียวกัน หรือคนละ Fuctionก็ได้
varTop=tk.StringVar() # Radio ชุดเดียวกัน ใช้ Widget Variable เดียวกัน
rdo3=ttk.Radiobutton(root,text='ไม่ราดน้ำ',value='ไม่ต้องราดน้ำ',variable=varTop,command=rdoClicked)
rdo3.place(x=10,y=200)
rdo4=ttk.Radiobutton(root,text='ราดน้ำ',value='ราดน้ำด้วย',variable=varTop,command=rdoClicked)
rdo4.place(x=110,y=200)

st2=ScrolledText(root, width=20 ,height=5)
st2.place(x=200,y=150)
# -----------------------------------------------------------------------------------------------------------



st=ScrolledText(root, width=20 , height=5)
st.place(x=200,y=10)



root.mainloop()