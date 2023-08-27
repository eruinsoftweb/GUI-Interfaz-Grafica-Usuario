from tkinter import *

def pre():
    global inp
    global app
    app = Tk()
    app.geometry('370x550')
    app.resizable(False, False)
    app.title('Calculadora')
    app.iconbitmap('o.ico')

    L1 = Label(app, text='Calculadora', font=('Century Gothic', 14))# bg='#F5F5F5', fg='white'
    L1.pack(fill='x')


    inp = Entry(app, font=('Century Gothic', 17), justify='center')
    inp.place(x=35, y=80, width='300')
    # inp.insert (0, '')
 


def aff(x):
    L1 = Label(app, text=x, font=('Century Gothic', 13, 'bold'), anchor='e')
    L1.place(x=35, y=50, width='300')


val = ['0', '0']
def adds(a, b): return a+b
def souss(a, b): return a-b
def muls(a, b): return a*b
def divs(a, b):
    if b == 0: return 'ERROR'
    else: return a/b

def add():
    global val
    if val[0] == 'ERROR': cls()
    print("val i ", val)
    if val[0] != '0':
        if len(inp.get())>0 :
            if val[1] == '+':
                res = adds(val[0], float(inp.get()))
                aff(str(res)+ ' + ')
                val = [res, '+']
            elif val[1] == '-':
                res = souss(val[0], float(inp.get()))
                aff(str(res)+ ' + ')
                val = [res, '+']
            elif val[1] == 'x':
                res = muls(val[0], float(inp.get()))
                aff(str(res)+ ' + ')
                val = [res, '+']
            elif val[1] == '/':
                res = divs(val[0], float(inp.get()))
                aff(str(res)+ ' + ')
                val = [res, '+']
            elif val[1] == '^':
                res = pow(float(val[0]), float(inp.get()))
                aff(str(res)+ ' + ')
                val = [res, '+']
            elif val[1] == 'mod':
                res = pow(int(val[0]), 1, int(inp.get()))
                aff(str(res)+ ' + ')
                val = [res, '+']
        else:
            aff(str(val[0])+' + ')
            val[1] = '+'
    else:
        if len(inp.get())>0 :
            aff(str(inp.get())+' + ')
            val[0] = float(inp.get()); val[1] = '+'
        else:
            aff('0 + ')
            val[0] = 0; val[1] = ' + '
    inp.delete(0, END)

    print("val f ", val)
    print("\n")
    
def sous():
    global val
    if val[0] == 'ERROR': cls()
    print("val i ", val)
    if val[0] != '0':
        if len(inp.get())>0 :
            if val[1] == '+':
                res = adds(val[0], float(inp.get()))
                aff(str(res)+ ' - ')
                val = [res, '-']
            elif val[1] == '-':
                res = souss(val[0], float(inp.get()))
                aff(str(res)+ ' - ')
                val = [res, '-']
            elif val[1] == 'x':
                res = muls(val[0], float(inp.get()))
                aff(str(res)+ ' - ')
                val = [res, '-']
            elif val[1] == '/':
                res = divs(val[0], float(inp.get()))
                aff(str(res)+ ' - ')
                val = [res, '-']
            elif val[1] == '^':
                res = pow(float(val[0]), float(inp.get()))
                aff(str(res)+ ' - ')
                val = [res, '-']
            elif val[1] == 'mod':
                res = pow(int(val[0]), 1, int(inp.get()))
                aff(str(res)+ ' - ')
                val = [res, '-']
        else:
            aff(str(val[0])+' - ')
            val[1] = '-'
    else:
        if len(inp.get())>0 :
            aff(str(inp.get())+' - ')
            val[0] = float(inp.get()); val[1] = '-'
        else:
            aff('0 - ')
            val[0] = 0; val[1] = '-'
    inp.delete(0, END)

    print("val f ", val)
    print("\n")
    
def mul():
    global val
    if val[0] == 'ERROR': cls()
    print("val i ", val)
    if val[0] != '0':
        if len(inp.get())>0 :
            if val[1] == '+':
                res = adds(val[0], float(inp.get()))
                aff(str(res)+ ' x ')
                val = [res, 'x']
            elif val[1] == '-':
                res = souss(val[0], float(inp.get()))
                aff(str(res)+ ' x ')
                val = [res, 'x']
            elif val[1] == 'x':
                res = muls(val[0], float(inp.get()))
                aff(str(res)+ ' x ')
                val = [res, 'x']
            elif val[1] == '/':
                res = divs(val[0], float(inp.get()))
                aff(str(res)+ ' x ')
                val = [res, 'x']
            elif val[1] == '^':
                res = pow(float(val[0]), float(inp.get()))
                aff(str(res)+ ' x ')
                val = [res, 'x']
            elif val[1] == 'mod':
                res = pow(int(val[0]), 1, int(inp.get()))
                aff(str(res)+ ' x ')
                val = [res, 'x']
        else:
            aff(str(val[0])+' x ')
            val[1] = 'x'
    else:
        if len(inp.get())>0 :
            aff(str(inp.get())+' x ')
            val[0] = float(inp.get()); val[1] = 'x'
        else:
            aff('0 x ')
            val[0] = 0; val[1] = 'x'
    inp.delete(0, END)

    print("val f ", val)
    print("\n")

def div():
    global val
    if val[0] == 'ERROR': cls()
    print("val i ", val)
    if val[0] != '0':
        if len(inp.get())>0 :
            if val[1] == '+':
                res = adds(val[0], float(inp.get()))
                aff(str(res)+ ' / ')
                val = [res, '/']
            elif val[1] == '-':
                res = souss(val[0], float(inp.get()))
                aff(str(res)+ ' / ')
                val = [res, '/']
            elif val[1] == 'x':
                res = muls(val[0], float(inp.get()))
                aff(str(res)+ ' / ')
                val = [res, '/']
            elif val[1] == '/':
                res = divs(val[0], float(inp.get()))
                aff(str(res)+ ' / ')
                val = [res, '/']
            elif val[1] == '^':
                res = pow(float(val[0]), float(inp.get()))
                aff(str(res)+ ' / ')
                val = [res, '/']
            elif val[1] == 'mod':
                res = pow(int(val[0]), 1, int(inp.get()))
                aff(str(res)+ ' / ')
                val = [res, '/']
        else:
            aff(str(val[0])+' / ')
            val[1] = '/'
    else:
        if len(inp.get())>0 :
            aff(str(inp.get())+' / ')
            val[0] = float(inp.get()); val[1] = '/'
        else:
            aff('0 / ')
            val[0] = 0; val[1] = '/'
    inp.delete(0, END)

    print("val f ", val)
    print("\n")
    
def puissance():
    global val
    if val[0] == 'ERROR': cls()
    print("val i ", val)
    if val[0] != '0':
        if len(inp.get())>0 :
            if val[1] == '^':
                res = adds(val[0], float(inp.get()))
                aff(str(res)+ ' ^ ')
                val = [res, '^']
            elif val[1] == '-':
                res = souss(val[0], float(inp.get()))
                aff(str(res)+ ' ^ ')
                val = [res, '^']
            elif val[1] == 'x':
                res = muls(val[0], float(inp.get()))
                aff(str(res)+ ' ^ ')
                val = [res, '^']
            elif val[1] == '/':
                res = divs(val[0], float(inp.get()))
                aff(str(res)+ ' ^ ')
                val = [res, '^']
            elif val[1] == 'mod':
                res = pow(int(val[0]), 1, int(inp.get()))
                aff(str(res)+ ' ^ ')
                val = [res, '^']
        else:
            aff(str(val[0])+' ^ ')
            val[1] = '^'
    else:
        if len(inp.get())>0 :
            aff(str(inp.get())+' ^ ')
            val[0] = float(inp.get()); val[1] = '^'
        else:
            aff('0 ^ ')
            val[0] = 0; val[1] = '^'
    inp.delete(0, END)

    print("val f ", val)
    print("\n")

def mod():
    global val
    if val[0] == 'ERROR': cls()
    print("val i ", val)
    if val[0] != '0':
        if len(inp.get())>0 :
            if val[1] == '+':
                res = adds(val[0], float(inp.get()))
                aff(str(res)+ ' mod ')
                val = [res, 'mod']
            elif val[1] == '-':
                res = souss(val[0], float(inp.get()))
                aff(str(res)+ ' mod ')
                val = [res, 'mod']
            elif val[1] == 'x':
                res = muls(val[0], float(inp.get()))
                aff(str(res)+ ' mod ')
                val = [res, 'mod']
            elif val[1] == '/':
                res = divs(val[0], float(inp.get()))
                aff(str(res)+ ' mod ')
                val = [res, 'mod']
            elif val[1] == '^':
                res = pow(float(val[0]), float(inp.get()))
                aff(str(res)+ ' mod ')
                val = [res, 'mod']
        else:
            aff(str(val[0])+' mod ')
            val[1] = 'mod'
    else:
        if len(inp.get())>0 :
            aff(str(inp.get())+' mod ')
            val[0] = float(inp.get()); val[1] = 'mod'
        else:
            aff('0 mod ')
            val[0] = 0; val[1] = ' mod '
    inp.delete(0, END)

    print("val f ", val)
    print("\n")

def virg():
    global val
    if inp.get() != '':
        if str(inp.get()).count('.') == 0:
            inp.insert(len(inp.get()), '.')
    else:
        inp.insert(len(inp.get()), '0.')

def inv():
    global val
    if val[0] == 'ERROR': cls()
    if str(inp.get()) != '':
        if float(inp.get())==0:
            val[0] = 'ERROR'
        else:
            val[0] = 1/float(inp.get())
    else:
        if len(str(val[0]))>0:
            if float(val[0])==0:
                val[0] = 'ERROR'
            else:
                val[0] = 1/float(val[0])
    aff(str(val[0]))
    inp.delete(0, END)

def percent():
    global val
    if str(inp.get()) != '':
        val[0] = float(inp.get())/100
    else:
        if len(str(val[0]))>1:
            val[0] = val[0]/100
        else:
            val[0] = 0
    aff(str(val[0]))
    inp.delete(0, END)

def cls():
    global val
    val = ['0', '0']

def clear():
    global val
    val = ['0', '0']
    inp.delete(0, END)
    aff(str(''))

def ce():
    inp.delete(0, END)

def clearX():
    l = len(inp.get())
    inp.delete(l-1, END)

def eq():
    global val
    if val[1] == '+':
        if len(str(inp.get()))==0: inp0 = 0
        else: inp0 = inp.get()
        aff(str(adds(val[0], float(inp0))))
        val = [adds(val[0], float(inp0)), '0']
    elif val[1] == '-':
        if len(str(inp.get()))==0: inp0 = 0
        else: inp0 = inp.get()
        aff(str(souss(val[0], float(inp0))))
        val = [souss(val[0], float(inp0)), '0']
    elif val[1] == 'x':
        if len(str(inp.get()))==0: inp0 = 0
        else: inp0 = inp.get()
        aff(str(muls(val[0], float(inp0))))
        val = [muls(val[0], float(inp0)), '0']
    elif val[1] == '/':
        if len(str(inp.get()))==0: inp0 = 0
        else: inp0 = inp.get()
        aff(str(divs(val[0], float(inp0))))
        val = [divs(val[0], float(inp0)), '0']
    elif val[1] == '^':
        if len(str(inp.get()))==0: inp0 = 0
        else: inp0 = inp.get()
        aff(str(pow(float(val[0]), float(inp0))))
        val = [pow(float(val[0]), float(inp0)), '0']
    elif val[1] == 'mod':
        if len(str(inp.get()))==0: inp0 = 0
        else: inp0 = inp.get()
        print((val[0], 1, int(inp0)))
        aff(str(pow(int(val[0]), 1, int(inp0))))
        val = [pow(int(val[0]), 1, int(inp0)), '0']
    elif val[1]=='0':
        val[0] = float(inp.get())
        aff(str(val[0]))
    print(val)
    inp.delete(0, END)

def sign():
    global val
    if str(inp.get()) != '':
        if len(str(val[0]))>1:
            if val[1] == '+':
                res = -adds(val[0], float(inp.get()))
                aff(str(res))
                val = [res, '0']
            elif val[1] == '-':
                res = -souss(val[0], float(inp.get()))
                aff(str(res))
                val = [res, '0']
            elif val[1] == 'x':
                res = -muls(val[0], float(inp.get()))
                aff(str(res))
                val = [res, '0']
            elif val[1] == '/':
                res = -divs(val[0], float(inp.get()))
                aff(str(res))
                val = [res, '0']
            elif val[1] == '^':
                res = -pow(float(val[0]), float(inp.get()))
                aff(str(res))
                val = [res, '0']
        else:
            res = -float(inp.get())
            aff(str(res))
            val = [res, '0']
    else:
        if len(str(val[0]))>1:
            res = -float(val[0])
            aff(str(res))
            val = [res, '0']
        else:
            val[0] = 0
    aff(str(val[0]))
    inp.delete(0, END)


def f0(): inp.insert(len(inp.get()), 0)
def f1(): inp.insert(len(inp.get()), 1)
def f2(): inp.insert(len(inp.get()), 2)
def f3(): inp.insert(len(inp.get()), 3)
def f4(): inp.insert(len(inp.get()), 4)
def f5(): inp.insert(len(inp.get()), 5)
def f6(): inp.insert(len(inp.get()), 6)
def f7(): inp.insert(len(inp.get()), 7)
def f8(): inp.insert(len(inp.get()), 8)
def f9(): inp.insert(len(inp.get()), 9)


    
def buttons():

    xVar = 35; yVar = 150
    btn = Button(app, text='%', font=('Century Gothic', 13), height=2, width=7, command=percent)
    btn.place(x=int(xVar), y=int(yVar)); xVar+=75
    btn = Button(app, text='C', font=('Century Gothic', 13), height=2, width=7, command=clear)
    btn.place(x=int(xVar), y=int(yVar)); xVar+=75
    btn = Button(app, text='CE', font=('Century Gothic', 13), height=2, width=7, command=ce)
    btn.place(x=int(xVar), y=int(yVar)); xVar+=75
    btn = Button(app, text='<-', font=('Century Gothic', 13), height=2, width=7, command=clearX)
    btn.place(x=int(xVar), y=int(yVar))

    xVar = 35; yVar += 55
    btn = Button(app, text='1/x', font=('Century Gothic', 13), height=2, width=7, command=inv)
    btn.place(x=int(xVar), y=int(yVar)); xVar+=75
    btn = Button(app, text='^', font=('Century Gothic', 13), height=2, width=7, command=puissance)
    btn.place(x=int(xVar), y=int(yVar)); xVar+=75
    btn = Button(app, text='Mod', font=('Century Gothic', 13), height=2, width=7, command=mod)
    btn.place(x=int(xVar), y=int(yVar)); xVar+=75
    btn = Button(app, text='/', font=('Century Gothic', 13), height=2, width=7, command=div)
    btn.place(x=int(xVar), y=int(yVar))

    xVar = 35; yVar += 55
    btn = Button(app, text='7', font=('Century Gothic', 13), height=2, width=7, command=f7)
    btn.place(x=int(xVar), y=int(yVar)); xVar+=75
    btn = Button(app, text='8', font=('Century Gothic', 13), height=2, width=7, command=f8)
    btn.place(x=int(xVar), y=int(yVar)); xVar+=75
    btn = Button(app, text='9', font=('Century Gothic', 13), height=2, width=7, command=f9)
    btn.place(x=int(xVar), y=int(yVar)); xVar+=75
    btn = Button(app, text='x', font=('Century Gothic', 13), height=2, width=7, command=mul)
    btn.place(x=int(xVar), y=int(yVar))

    xVar = 35; yVar += 55
    btn = Button(app, text='4', font=('Century Gothic', 13), height=2, width=7, command=f4)
    btn.place(x=int(xVar), y=int(yVar)); xVar+=75
    btn = Button(app, text='5', font=('Century Gothic', 13), height=2, width=7, command=f5)
    btn.place(x=int(xVar), y=int(yVar)); xVar+=75
    btn = Button(app, text='6', font=('Century Gothic', 13), height=2, width=7, command=f6)
    btn.place(x=int(xVar), y=int(yVar)); xVar+=75
    btn = Button(app, text='-', font=('Century Gothic', 13), height=2, width=7, command=sous)
    btn.place(x=int(xVar), y=int(yVar))

    xVar = 35; yVar += 55
    btn = Button(app, text='1', font=('Century Gothic', 13), height=2, width=7, command=f1)
    btn.place(x=int(xVar), y=int(yVar)); xVar+=75
    btn = Button(app, text='2', font=('Century Gothic', 13), height=2, width=7, command=f2)
    btn.place(x=int(xVar), y=int(yVar)); xVar+=75
    btn = Button(app, text='3', font=('Century Gothic', 13), height=2, width=7, command=f3)
    btn.place(x=int(xVar), y=int(yVar)); xVar+=75
    btn = Button(app, text='+', font=('Century Gothic', 13), height=2, width=7, command=add)
    btn.place(x=int(xVar), y=int(yVar))

    xVar = 35; yVar += 55
    btn = Button(app, text='+/-', font=('Century Gothic', 13), height=2, width=7, command=sign)
    btn.place(x=int(xVar), y=int(yVar)); xVar+=75
    btn = Button(app, text='0', font=('Century Gothic', 13), height=2, width=7, command=f0)
    btn.place(x=int(xVar), y=int(yVar)); xVar+=75
    btn = Button(app, text=',', font=('Century Gothic', 13), height=2, width=7, command=virg)
    btn.place(x=int(xVar), y=int(yVar)); xVar+=75
    btn = Button(app, text='=', font=('Century Gothic', 13), height=2, width=7, command=eq)
    btn.place(x=int(xVar), y=int(yVar))

def Menu():
    pre()
    buttons()
    app.mainloop()
Menu()
