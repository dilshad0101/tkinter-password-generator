#password is generated using 'calc' module 
#now we have to display it in GUI


import calc
from calc import main1
from tkinter import Text , Button,Tk,filedialog, font
from tkinter import ttk

window = Tk()
window.title("Password Generator")
window.configure(bg = "black")
window.geometry("200x300")


def display_txt():
    main1()
    bt2['font'] = font.Font(size = 10,weight='bold')
    bt2.pack(ipadx = 50,side = 'top')
    global t
    t = Text(window,height = 0,width = 15,borderwidth=0)
    t.insert(2.0,calc.vpw)
    t.pack(pady = 3)
    t.configure(state="disabled")


def save():
    savedpw = calc.vpw
    files = [('Text Documents','*.txt')]
    file = filedialog.asksaveasfile(initialfile =  "password.txt" ,filetypes = files, defaultextension = "*.txt")
    if file :
        file.write(savedpw)
        file.close()
    

bt1 = Button(window, borderwidth= 0,activebackground= '#101010',activeforeground= "white",bg = "black",fg = 'white',text = "CREATE" ,command = display_txt)
bt1['font'] = font.Font(size = 10,weight='bold')
bt1.pack(ipadx = 50,side = "top")
bt2 = Button(window,text = " SAVE ",borderwidth= 0,activebackground= '#101010',activeforeground= "white",bg = "black",fg = 'white',command  = lambda:save())

window.mainloop()
