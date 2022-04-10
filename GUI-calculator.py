#GUI-calculator.py

from tkinter import *
from tkinter import ttk,messagebox

GUI=Tk()
GUI.title('vat Calculator')
GUI.geometry('500x600')

bg=PhotoImage(file=r'/Users/anne_imac/Desktop/basic python/week05/icon.png')

BG=Label(GUI,image=bg)
BG.pack()


L=Label(GUI,text='payment',font=(None,20))
L.pack()


v_payment=StringVar() #เป็นตัวแปลที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1=ttk.Entry(GUI,textvariable=v_payment, font=(None,20))
E1.pack()

def Cal():
    try:    
        quan=float(v_payment.get())
        calc=quan*0.07
        messagebox.showinfo('vat 7 percent','vat {} บาท'.format(calc))
        v_payment.set('')
        E1.focus()
    except:
        messagebox.showwarning('error','please fill in number')
        v_payment.set('1')
        E1.focus()


B=ttk.Button(GUI,text='calculate')
B.pack(ipadx=30,ipady=20)

GUI.mainloop() #เพื่อให้โปรแกรม run ตลอดเวลา