import tkinter as tk
from tkinter import ttk,messagebox,Label
from tkinter.scrolledtext import ScrolledText

# Function Insert ScrollText
def orderfood():
    stfood.insert('1.0',cmfood.get()+'\n')

# Function Clear ScrollText
def clearorder():
    stfood.delete('1.0','end')

# Function แสดงรายละเอียดและการจ่ายเงิน
def changeitem():
    stitem.delete('1.0','end')
    thetext=f"{varw.get()}+{varb.get()}+{vars.get()} \n {varpay.get()}"
    stitem.insert('1.0',thetext)

# Main Program
root = tk.Tk()
root.title("Food Order")
root.geometry('600x400+200+100')

# สร้าง ComboBox
foodlist=['ข้าวขาหมู','ข้าวหมูแดง','ข้าวมันไก่']
cmfood=ttk.Combobox(root)
cmfood['values']=foodlist
cmfood.place(x=10,y=10)


# สร้างปุ่มบันทึกรายการอาหาร
btnorder=ttk.Button(root,text="บันทึกรายการ",command=orderfood)
btnorder.place(x=180,y=10)

# สร้างปุ่มล้างรายการอาหาร
btnclear = ttk.Button(root,text="ล้างรายการ",command=clearorder)
btnclear.place(x=180,y=60)

# สร้าง ScrolledText รายการอาหาร
stfood = ScrolledText(root,width=30,height=10)
stfood.place(x=300,y=10)

# สร้าง Checkbox รายละเอียด
varw=tk.StringVar()
ckw=ttk.Checkbutton(root,text="อุ่น",variable=varw,onvalue='อุ่น',offvalue='',command=changeitem)
ckw.place(x=10,y=210)

varb=tk.StringVar()
ckb=ttk.Checkbutton(root,text="ใส่ถุง",variable=varb,onvalue='ใส่ถุง',offvalue='',command=changeitem)
ckb.place(x=60,y=210)

vars=tk.StringVar()
cks=ttk.Checkbutton(root,text="ช้อนส้อม",variable=vars,onvalue='ช้อนส้อม',offvalue='',command=changeitem)
cks.place(x=110,y=210)

# สร้าง Radio การจ่ายเงิน
varpay=tk.StringVar()
rdc=ttk.Radiobutton(root,text="จ่ายเงินสด",variable=varpay,value="เงินสด")
rdc.place(x=10,y=250)
rdt=ttk.Radiobutton(root,text="โอน",variable=varpay,value="โอน")
rdt.place(x=110,y=250)




# สร้าง ScrolledText รายละเอียด
stitem=ScrolledText(root,width=30,height=5)
stitem.place(x=300,y=210)

tk.mainloop()
