from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

master = tk.Tk()
master.geometry('500x200') 

def func():
    messagebox.showinfo( "Hello Educba", "Click on the tabs to view the content")  
      
b1 = Button( master, text='Click me for next step', background = 'Red', fg = '#000000', command = func)
b1.pack()
tc = ttk.Notebook(master) 

t1 = ttk.Frame(tc) 
t2 = ttk.Frame(tc) 
tc.add(t1, text ='Notebook tab1') 
tc.add(t2, text ='Notebook tab2') 
tc.pack(expand = 1, fill ="both") 
ttk.Label(t1, 
		text ="Hello Educba Technology Institute").grid(column = 3, 
							row = 3)				     
ttk.Label(t2, 
		text ="Notebook widget demonstration").grid(column = 3, 
									row = 3) 
master.mainloop()