import tkinter as tk
window=tk.Tk()
window.title('Calculator')
window.iconbitmap('calc.ico')
window.geometry('455x575')
window.configure(bg='#0fe9a0')
window.resizable(width=False,height=False)
expression=''
ans=0
def press(num):
    global expression
    expression = expression+str(num)
    equation.set(expression)
def clear():
    global expression
    expression=''
    equation.set(expression)
    equation.set('0')
def equalpress():
    global expression
    global ans
    try:
        equation.set(str(eval(expression)))
        expression=str(eval(expression))
        ans=eval(expression)
        expression=''
    except:
        equation.set('error')
        expression=''
def backspace():
    global expression
    try:
        expression=expression[0:(len(expression)-1)]
        if len(expression)>0:
            equation.set(expression)
        else:
            equation.set(0)
    except:
        pass
buttonframe=tk.Frame(master=window,bg='#0fe9a0')

equation=tk.StringVar()
equation.set('0')


entrybox= tk.Entry(master=buttonframe,justify='right',textvariable= equation,font=('arial',20,'bold'))
button1=tk.Button(master=buttonframe, text='1',font=('times new roman',12),relief='ridge',bd=1,bg='#b8fee6',width=8,height=3,command=lambda:press(1))
button2=tk.Button(master=buttonframe, text='2',font=('times new roman',12),relief='ridge',bd=1,bg='#b8fee6',width=8,height=3,command=lambda:press(2))
button3=tk.Button(master=buttonframe, text='3',font=('times new roman',12),relief='ridge',bd=1,bg='#b8fee6',width=8,height=3,command=lambda:press(3))
button4=tk.Button(master=buttonframe, text='4',font=('times new roman',12),relief='ridge',bd=1,bg='#b8fee6',width=8,height=3,command=lambda:press(4))
button5=tk.Button(master=buttonframe, text='5',font=('times new roman',12),relief='ridge',bd=1,bg='#b8fee6',width=8,height=3,command=lambda:press(5))
button6=tk.Button(master=buttonframe, text='6',font=('times new roman',12),relief='ridge',bd=1,bg='#b8fee6',width=8,height=3,command=lambda:press(6))
button7=tk.Button(master=buttonframe, text='7',font=('times new roman',12),relief='ridge',bd=1,bg='#b8fee6',width=8,height=3,command=lambda:press(7))
button8=tk.Button(master=buttonframe, text='8',font=('times new roman',12),relief='ridge',bd=1,bg='#b8fee6',width=8,height=3,command=lambda:press(8))
button9=tk.Button(master=buttonframe, text='9',font=('times new roman',12),relief='ridge',bd=1,bg='#b8fee6',width=8,height=3,command=lambda:press(9))
button0=tk.Button(master=buttonframe, text='0',font=('times new roman',12),relief='ridge',bd=1,bg='#b8fee6',width=8,height=3,command=lambda:press(0))
buttonplus=tk.Button(master=buttonframe, text='+',font=('times new roman',12),relief='ridge',bd=1,bg='#b8fee6',width=8,height=3,command=lambda:press('+'))
buttonminus=tk.Button(master=buttonframe, text='-',font=('times new roman',12),relief='ridge',bd=1,bg='#b8fee6',width=8,height=3,command=lambda:press('-'))
buttonmult=tk.Button(master=buttonframe, text='x',font=('times new roman',12),relief='ridge',bd=1,bg='#b8fee6',width=8,height=3,command=lambda:press('*'))
buttonpoint=tk.Button(master=buttonframe, text='.',font=('times new roman',12),relief='ridge',bd=1,bg='#b8fee6',width=8,height=3,command=lambda:press('.'))
buttondiv=tk.Button(master=buttonframe, text='/',font=('times new roman',12),relief='ridge',bd=1,bg='#b8fee6',width=8,height=3,command=lambda:press('/'))
buttonclear=tk.Button(master=buttonframe, text='C',font=('times new roman',12),relief='ridge',bd=1,bg='#b8fee6',width=8,height=3,command=lambda:clear())
buttonequal=tk.Button(master=buttonframe, text='=',font=('times new roman',12),relief='ridge',bd=1,bg='#b8fee6',width=17,height=3,command=lambda:equalpress())
buttonbs=tk.Button(master=buttonframe, text='<-',font=('times new roman',12),relief='ridge',bd=1,bg='#b8fee6',width=8,height=3,command=lambda:backspace())
buttonans=tk.Button(master=buttonframe, text='Ans',font=('times new roman',12),relief='ridge',bd=1,bg='#b8fee6',width=8,height=3,command=lambda:press(ans))

buttonframe.pack()
entrybox.grid(row=0,column=0,columnspan=4,pady=15,ipadx=8,ipady=25)
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
buttonplus.grid(row=1,column=3)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
buttonminus.grid(row=2,column=3)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
buttonmult.grid(row=3,column=3)
buttonpoint.grid(row=4,column=0)
button0.grid(row=4,column=1)
buttonclear.grid(row=4,column=2)
buttondiv.grid(row=4,column=3)
buttonbs.grid(row=5,column=3)
buttonans.grid(row=5,column=2)
buttonequal.grid(row=5,column=0,columnspan=2)



window.mainloop()
