import tkinter as tk
from tkinter import ttk 
from tkinter.scrolledtext import ScrolledText

def addcombo(event):
    sublisst.append(ent1.get())#ใช้gentเพื่ออ่านค่าในent1
    cmSubj["values"]=sublisst
    ent1.delete(0,'end')#พิมในent1แล้วข้อความจะหายไปเราไม่ต้องมาลบเอง
    ent1.focus()



# sublisst= ['English','Calculus','Football']

root = tk.Tk()
root.title("Test Combo")
root.geometry("500x300+600+200")




ent1=ttk.Entry(root)
ent1.place(x=10,y=10)
ent1.focus()
ent1.bind('<Return>',addcombo)

sublisst=[]
cmSubj=ttk.Combobox(root)
cmSubj.place(x=250,y=10)








root.mainloop()


