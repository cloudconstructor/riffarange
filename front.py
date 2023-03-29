from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import filedialog
import functions as fn
# from tkinter.messagebox import showinfo

#styling def
DarkBg = "#333"
DarkBg2 = "#222"
DarkBg3 = "#111"
DarkFg = "#fff"
defaultFont = "verdana"
defaultFontSize_tab = 13
defaultFontSize_title = 15
defaultFontSize = 12
buttonFontSize = 10
buttonBg = "#555"
buttonBgSel_red = "#fc0000"
buttonBgSel_yellow = "yellow"
buttonBgSel_orange = "#ffc847"
buttonBgSel_green = "green"
buttonBgSel_gray= "#555"
buttonBgSel_blue= "#4867aa"
buttonFg = "#fff"
fieldBg = "#555"
fieldFg = "#fff"
treeBg = "#333"
scrollBg = "#222"
scrollFg = "#555"



def initWindow():
    global root
    root = tk.Tk()
    root.geometry('800x480')
    root.resizable(False, False)
    root.title('RiffArange v0.55')
    root.configure(background=DarkBg)
    return(root)

def theme():
    global style
    style = Style(root)
    style.theme_create( 
        "mytheme", parent="alt", settings={
            "TNotebook": {
                "configure": {
                    "tabmargins": [2, 5, 2, 0] 
                    } 
                },
            "TNotebook.Tab": {
                "configure": {
                    "padding": [5, 1],
                    "background": buttonBg, 
                    "foreground": buttonFg,
                    "font": (defaultFont, defaultFontSize_tab)
                    },
                "map": {
                    "background": [("selected", buttonBgSel_red)],
                    "expand": [("selected", [1, 1, 1, 0])] 
                    } 
                },

            "Treeview":{
                "configure":{
                    "highlightthickness": 1,
                    "borderwidth": 0,
                    "background": treeBg,
                    "fieldbackground": treeBg,
                    "foreground": "#fff",
                    },
                "map": {
                    "background": [("selected", buttonBgSel_red)], 
                    } 
                },
            "Treeview.Heading":{
                "configure":{
                    "font": ('Calibri', 13,'bold'),
                    "background": "#000",
                    "foreground": "#fff",
                    }
                },
            "TButton":{
                "configure":{
                    "background": "#000",
                    "foreground": "#fff",
                    }
                },
            "TScrollbar":{
                "configure":{
                    "troughcolor": scrollBg,
                    "background": scrollFg,
                    "relief": INSIDE,
                    }
                },
            # "Entry":{
            #     "configure":{
            #         "background": fieldBg,
            #         "foreground": fieldFg,
            #         "relief": SOLID,
            #         "highlightthickness": 1,
            #         "font": defaultFontSize,
            #         "highlightbackground": "white",
            #         "highlightcolor": "white"
            #         }
            #     },
            
        } 
    )

    style.theme_use('mytheme')
    style.configure('Dark.TFrame', background=DarkBg)
    style.configure('Dark2.TFrame', background=DarkBg2)
    style.configure('Dark3.TFrame', background=DarkBg3)

    return style


def tab1(frame1):
    nsl = ttk.Label(frame1, text="Song Arrangements", font=("Arial Bold",defaultFontSize), background=DarkBg, foreground=DarkFg)
    nsl.place(relx=0,rely=0.01)

    # songlist ---------------------------------
    columns = ('name', 'desc', 'tuning')
    tree = ttk.Treeview(frame1, columns=columns, show='headings',style="mytheme.Treeview", height="15",  selectmode="extended")


    # define headings
    tree.heading('name', text='Name', anchor="w")
    tree.heading('desc', text='Description', anchor="w")
    tree.heading('tuning', text='Tuning', anchor="w")

    tree.column('name', width=250)
    tree.column('desc', width=315)
    tree.column('tuning', width=60)

    # generate sample data -----------------------------------------------------
    # contacts = []
    # for n in range(1, 100):
    #     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

    # # add data to the treeview
    # for contact in contacts:
    #     tree.insert('', tk.END, values=contact)

    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            # show a message
            # showinfo(title='Information', message=','.join(record))

    # --------------------------------------------------------------------------

    tree.bind('<<TreeviewSelect>>', item_selected)
    tree.place(relx=0.002 ,rely=0.08)

    testfolder = "C:/Users/dclou/Music/Black Stone Machine - One With the Horde EP/One With The Horde EP/"

    test = fn.getFileList(testfolder)
    # print(test)
    

    # add a scrollbar
    scrollbar = ttk.Scrollbar(frame1, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.place(relx=0.81 ,rely=0.08, height=308+20)

    nsb = Button(frame1, text="Create new", fg="white", bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    nsb.place(relx=0.85,rely=0.08)

    psb = Button(frame1, text="Edit", fg=buttonFg, bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    psb.place(relx=0.85,rely=0.18)

    psb = Button(frame1, text="Delete", fg=buttonFg, bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    psb.place(relx=0.85,rely=0.28)


    nsb = Button(frame1, text="Play", fg=buttonFg, bg=buttonBgSel_blue, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    nsb.place(relx=0.85,rely=0.66)

    nsb = Button(frame1, text="Stop", fg=buttonFg, bg=buttonBgSel_red, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    nsb.place(relx=0.85,rely=0.76)




def tab2(frame2):
    # allfiles ---------------------------------
    nsl = ttk.Label(frame2, text="Discovered Audio files", font=("Arial Bold",defaultFontSize), background=DarkBg, foreground=DarkFg)
    nsl.place(relx=0,rely=0.01)

    columns = ('col1', 'col2', 'col3')
    tree1 = ttk.Treeview(frame2, columns=columns, show='headings',style="mytheme.Treeview", height="7",  selectmode="extended")

    tree1.heading('col1', text='Name/Filename', anchor="w")
    tree1.heading('col2', text='Description', anchor="w")
    tree1.heading('col3', text='Tuning', anchor="w")

    tree1.column('col1', width=250)
    tree1.column('col2', width=315)
    tree1.column('col3', width=60)

    # tree.bind('<<TreeviewSelect>>', item_selected)
    tree1.place(relx=0.002 ,rely=0.08)

    scrollbar = ttk.Scrollbar(frame2, orient=tk.VERTICAL, command=tree1.yview)
    tree1.configure(yscroll=scrollbar.set)
    scrollbar.place(relx=0.81 ,rely=0.08, height=148+20)

    # validated files ---------------------------------
    nsl2 = ttk.Label(frame2, text="Validated Audio files", font=("Arial Bold",defaultFontSize), background=DarkBg, foreground=DarkFg)
    nsl2.place(relx=0,rely=0.50)

    columns2 = ('col1', 'col2', 'col3')
    tree2 = ttk.Treeview(frame2, columns=columns2, show='headings',style="mytheme.Treeview", height="7",  selectmode="extended")
    
    tree2.heading('col1', text='Name/Filename', anchor="w")
    tree2.heading('col2', text='Description', anchor="w")
    tree2.heading('col3', text='Tuning', anchor="w")

    # minwidth = tree2.column('col1', option='minwidth')
    tree2.column('col1', width=250)
    tree2.column('col2', width=315)
    tree2.column('col3', width=60)

    # tree.bind('<<TreeviewSelect>>', item_selected)
    tree2.place(relx=0.005 ,rely=0.56)

    scrollbar2 = ttk.Scrollbar(frame2, orient=tk.VERTICAL, command=tree2.yview)
    tree2.configure(yscroll=scrollbar2.set)
    scrollbar2.place(relx=0.81 ,rely=0.56 ,height=148+20)
    

    nsb = Button(frame2, text="Hide", fg=buttonFg, bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    nsb.place(relx=0.85,rely=0.08)

    nsb1 = Button(frame2, text="View Hidden", fg=buttonFg, bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    nsb1.place(relx=0.85,rely=0.18)

    nsb2 = Button(frame2, text="Validate", fg=buttonFg, bg=buttonBgSel_green, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    nsb2.place(relx=0.85,rely=0.28)

    nsb3 = Button(frame2, text="Remove", fg=buttonFg, bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    nsb3.place(relx=0.85,rely=0.56)

    nsb2 = Button(frame2, text="Play", fg=buttonFg, bg=buttonBgSel_blue, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    nsb2.place(relx=0.85,rely=0.76)

    nsb3 = Button(frame2, text="Stop", fg=buttonFg, bg=buttonBgSel_red, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    nsb3.place(relx=0.85,rely=0.86)


def tab3(frame3):
    
    #add new directory -------------------------------------------------
    def selectDirectory():
        folder_selected = filedialog.askdirectory()
        directory_entry.delete(0,END)
        directory_entry.insert(0,folder_selected)
        return

    filepath = StringVar()
    ttk.Label(frame3, text="Add Folder", background=DarkBg, foreground=DarkFg, font=("Arial Bold",defaultFontSize) ).place(relx=0,rely=0.01)

    directory_entry = Entry(frame3, width=60, textvariable=filepath, font=defaultFontSize, bg=fieldBg, fg=fieldFg, relief=FLAT, highlightthickness=2)
    directory_entry.place(relx=0.10,rely=0.01)
    directory_entry.focus()

    sd = Button(frame3, text="Browse", fg=buttonFg, bg=buttonBgSel_gray, relief=FLAT,  font=(defaultFont,buttonFontSize), command=selectDirectory)
    sd.place(relx=0.81,rely=0.008)

    ins = Button(frame3, text="Add Folder", fg=buttonFg, bg=buttonBgSel_green, relief=FLAT,  font=(defaultFont,buttonFontSize), command=NONE)
    ins.place(relx=0.89,rely=0.008)

    #dir list --------------------------------------------------------
    nsl = ttk.Label(frame3, text="Added Folders", font=("Arial Bold",defaultFontSize), background=DarkBg, foreground=DarkFg)
    nsl.place(relx=0,rely=0.12)

    columns = ('col1')
    tree1 = ttk.Treeview(frame3, columns=columns, show='headings',style="mytheme.Treeview", height="15",  selectmode="extended")
    tree1.heading('col1', text="Folder", anchor="w")
    tree1.column('col1', width=230)
    # tree.bind('<<TreeviewSelect>>', item_selected)
    tree1.place(relx=0.002 ,rely=0.2)

    scrollbar = ttk.Scrollbar(frame3, orient=tk.VERTICAL, command=tree1.yview)
    tree1.configure(yscroll=scrollbar.set)
    scrollbar.place(relx=0.3 ,rely=0.2, height=308+20)
    
    columns2 = ('col1')
    tree2 = ttk.Treeview(frame3, columns=columns2, show='headings',style="mytheme.Treeview", height="15",  selectmode="extended")
    tree2.heading('col1', text="Files", anchor="w")
    tree2.column('col1', width=370)
    # tree.bind('<<TreeviewSelect>>', item_selected)
    tree2.place(relx=0.33 ,rely=0.2)

    scrollbar2 = ttk.Scrollbar(frame3, orient=tk.VERTICAL, command=tree2.yview)
    tree2.configure(yscroll=scrollbar2.set)
    scrollbar2.place(relx=0.81 ,rely=0.2, height=308+20)

    Button(frame3, text="Select All", fg=buttonFg, bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10).place(relx=0.85,rely=0.2)

    Button(frame3, text="Select None", fg=buttonFg, bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10).place(relx=0.85,rely=0.3)
    

    Button(frame3, text="Add", fg=buttonFg, bg=buttonBgSel_green, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10).place(relx=0.85,rely=0.4)
    

    Button(frame3, text="Play", fg=buttonFg, bg=buttonBgSel_blue, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10).place(relx=0.85,rely=0.76)


    Button(frame3, text="Stop", fg=buttonFg, bg=buttonBgSel_red, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10).place(relx=0.85,rely=0.86)
    


    


