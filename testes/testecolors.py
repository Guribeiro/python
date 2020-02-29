from tkinter import *

menu_init = Tk()
menu_init.title("titlestring")
menu_init.geometry("500x300")

label1 = Label(menu_init, text='Label 1', font='Arial 20 bold', fg='red') 
label1.pack()

label2 = Label(menu_init, text='Label 2', font='Arial 20 bold', fg='red') 
label2.pack()

label3 = Label(menu_init, text='Label 3', font='Arial 20 bold', fg='red') 
label3.pack()

menu_init.mainloop()

