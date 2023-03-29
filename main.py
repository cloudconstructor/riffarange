from tkinter import *
from tkinter import ttk
import front as f

root = f.initWindow()
style = f.theme()

# create a notebook
notebook = ttk.Notebook(root, width=800, height= 480)
notebook.pack(pady=0, expand=True)

# Child frames
frame1 = ttk.Frame(notebook, padding=10, style="Dark.TFrame")
frame1.pack(fill=BOTH, expand=True)

frame2 = ttk.Frame(notebook, padding=10, style="Dark.TFrame")
frame2.pack(fill=BOTH, expand=True)

frame3 = ttk.Frame(notebook, padding=10, style="Dark.TFrame")
frame3.pack(fill=BOTH, expand=True)


# Create the pages
notebook.add(frame1, text='Songs',underline=2)
notebook.add(frame3, text='Folders',underline=2)
notebook.add(frame2, text='Audio files',underline=2)
notebook.pack(expand = 1, fill ="both") 


f.tab1(frame1)
f.tab2(frame2)
f.tab3(frame3)



root.mainloop()