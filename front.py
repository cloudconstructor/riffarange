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
fieldBorderColor = "#666"
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
            "TCombobox":{
                "configure":{
                    "padding": [5, 1],
                    "background": fieldBg, 
                    "selectbackground": fieldBg,
                    "fieldbackground": fieldBg,
                    "foreground": fieldFg,
                    "bordercolor": fieldBorderColor,
                    "arrowsize": 15,
                    "arrowcolor": buttonFg,
                    "relief": FLAT,
                    }
                },
          
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
    tree = ttk.Treeview(frame1, columns=columns, show='headings',style="mytheme.Treeview", height="17",  selectmode="extended")


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

    # testfolder = "C:/Users/dclou/Music/Black Stone Machine - One With the Horde EP/One With The Horde EP/"

    # test = fn.getFileList(testfolder)
    # print(test)
    

    # add a scrollbar
    scrollbar = ttk.Scrollbar(frame1, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.place(relx=0.81 ,rely=0.08, height=348+20)

    nsb = Button(frame1, text="Create new", fg="white", bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    nsb.place(relx=0.85,rely=0.08)

    psb = Button(frame1, text="Edit", fg=buttonFg, bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    psb.place(relx=0.85,rely=0.18)

    psb = Button(frame1, text="Delete", fg=buttonFg, bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    psb.place(relx=0.85,rely=0.28)


    nsb = Button(frame1, text="Play", fg=buttonFg, bg=buttonBgSel_blue, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    nsb.place(relx=0.85,rely=0.76)

    nsb = Button(frame1, text="Stop", fg=buttonFg, bg=buttonBgSel_red, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    nsb.place(relx=0.85,rely=0.86)





def tab2(frame2):

    def showDetailsFrame():
        initPage.pack_forget()
        editPage.pack(fill=BOTH, expand=True)
        
    def showFileListFrame():
        editPage.pack_forget()
        initPage.pack(fill=BOTH, expand=True)

    def saveFileAtts():
        titleVal=name_entry.get()
        descVal=desc.get("1.0","end-1c")
        tuningVal=tuningList.get()
        print(titleVal+" "+descVal+" "+tuningVal)
        

    initPage = ttk.Frame(frame2,padding=0, style="Dark.TFrame")
    
    # allfiles ---------------------------------
    nsl = ttk.Label(initPage, text="Discovered Audio files", font=("Arial Bold",defaultFontSize), background=DarkBg, foreground=DarkFg)
    nsl.place(relx=0,rely=0.01)


    # file list ---------------------------------
    columns = ('name', 'desc', 'tuning')
    tree = ttk.Treeview(initPage, columns=columns, show='headings',style="mytheme.Treeview", height="17",  selectmode="extended")


    # define headings
    tree.heading('name', text='Name/Filename', anchor="w")
    tree.heading('desc', text='Description', anchor="w")
    tree.heading('tuning', text='Rec Tuning', anchor="w")

    tree.column('name', width=250)
    tree.column('desc', width=290)
    tree.column('tuning', width=85)

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

    # testfolder = "C:/Users/dclou/Music/Black Stone Machine - One With the Horde EP/One With The Horde EP/"

    # test = fn.getFileList(testfolder)
    # print(test)
    
    scrollbar = ttk.Scrollbar(initPage, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.place(relx=0.81 ,rely=0.08, height=348+20)

    nsb = Button(initPage, text="Hide", fg=buttonFg, bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    nsb.place(relx=0.85,rely=0.08)

    nsb1 = Button(initPage, text="View Hidden", fg=buttonFg, bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    nsb1.place(relx=0.85,rely=0.18)

    nsb2 = Button(initPage, text="Edit Detais", fg=buttonFg, bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=showDetailsFrame, width=10)
    nsb2.place(relx=0.85,rely=0.28)

    nsb2 = Button(initPage, text="Play", fg=buttonFg, bg=buttonBgSel_blue, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    nsb2.place(relx=0.85,rely=0.76)

    nsb3 = Button(initPage, text="Stop", fg=buttonFg, bg=buttonBgSel_red, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    nsb3.place(relx=0.85,rely=0.86)

    initPage.pack(fill=BOTH, expand=True)

    # PAGE FOR EDITING DETAILS ---------------------------------------------
    editPage = ttk.Frame(frame2,padding=0, style="Dark.TFrame")

    nsl = ttk.Label(editPage, text="Edit Details", font=("Arial Bold",defaultFontSize), background=DarkBg, foreground=DarkFg)
    nsl.place(relx=0,rely=0.01)

    ttk.Label(editPage, text="Title", background=DarkBg, foreground=DarkFg, font=defaultFontSize ).place(relx=0,rely=0.1)
    name_entry = Entry(editPage, width=73, font=defaultFontSize, bg=fieldBg, fg=fieldFg, relief=FLAT, highlightthickness=2, highlightbackground=fieldBorderColor, insertbackground=buttonBgSel_red, selectbackground=buttonBgSel_red)
    name_entry.place(relx=0.13,rely=0.1)
    name_entry.focus()

    ttk.Label(editPage, text="Description", background=DarkBg, foreground=DarkFg, font=defaultFontSize ).place(relx=0,rely=0.2)
    desc = Text(editPage, width=73, height=5, font=defaultFontSize, bg=fieldBg, fg=fieldFg, relief=FLAT, highlightthickness=2, highlightbackground=fieldBorderColor, insertbackground=buttonBgSel_red, selectbackground=buttonBgSel_red)
    desc.place(relx=0.13, rely=0.2)
    
    ttk.Label(editPage, text="Tuned at", background=DarkBg, foreground=DarkFg, font=defaultFontSize ).place(relx=0,rely=0.5)

    # text_font = (defaultFont, 30)
    tunings = ["E Straight","D straight", "C straight", "Drop D", "Drop C"]
    tuningList = ttk.Combobox(editPage, values=tunings, width=71, font=defaultFontSize)

    # tuningList.set("Select the tuning the clip was recorded")
    
    root.option_add('*TCombobox*Listbox.background', fieldBg)
    root.option_add('*TCombobox*Listbox.foreground', fieldFg)
    tuningList.place(relx=0.13,rely=0.5)

    ttk.Label(editPage, text="Select the tuning the clip was recorded", background=DarkBg, foreground=DarkFg, font=defaultFontSize ).place(relx=0.13,rely=0.56)

    Button(editPage, text="Save", fg="white", bg=buttonBgSel_blue, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=saveFileAtts, width=10).place(relx=0.71,rely=0.9)
    Button(editPage, text="Cancel", fg="white", bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=showFileListFrame, width=10).place(relx=0.85,rely=0.9)
    

    


def tab3(frame3):
    
    def selectFolder():
        folder_selected = filedialog.askdirectory()
        directory_entry.delete(0,END)
        directory_entry.insert(0,folder_selected)
        return

    def addFolder():
        folder=directory_entry.get()
        print(folder)

    ttk.Label(frame3, text="New Folder", background=DarkBg, foreground=DarkFg, font=defaultFontSize ).place(relx=0,rely=0.01)

    directory_entry = Entry(frame3, width=59, font=defaultFontSize, bg=fieldBg, fg=fieldFg, relief=FLAT, highlightthickness=2, highlightbackground=fieldBorderColor, insertbackground=buttonBgSel_red, selectbackground=buttonBgSel_red)
    directory_entry.place(relx=0.11,rely=0.01)
    directory_entry.focus()

    sd = Button(frame3, text="Browse", fg=buttonFg, bg=buttonBgSel_gray, relief=FLAT,  font=(defaultFont,buttonFontSize), command=selectFolder)
    sd.place(relx=0.81,rely=0.008)

    ins = Button(frame3, text="Add Folder", fg=buttonFg, bg=buttonBgSel_green, relief=FLAT,  font=(defaultFont,buttonFontSize), command=addFolder)
    ins.place(relx=0.89,rely=0.008)

    #dir list --------------------------------------------------------
    nsl = ttk.Label(frame3, text="Added Folders", font=("Arial Bold",defaultFontSize), background=DarkBg, foreground=DarkFg)
    nsl.place(relx=0,rely=0.12)

    columns = ('col1')
    tree1 = ttk.Treeview(frame3, columns=columns, show='headings',style="mytheme.Treeview", height="15",  selectmode="extended")
    tree1.heading('col1', text="Folder", anchor="w")
    tree1.column('col1', width=230)
    # tree.bind('<<TreeviewSelect>>', item_selected)
    tree1.place(relx=0.002 ,rely=0.18)

    scrollbar = ttk.Scrollbar(frame3, orient=tk.VERTICAL, command=tree1.yview)
    tree1.configure(yscroll=scrollbar.set)
    scrollbar.place(relx=0.3 ,rely=0.18, height=308+20)
    
    columns2 = ('col1')
    tree2 = ttk.Treeview(frame3, columns=columns2, show='headings',style="mytheme.Treeview", height="15",  selectmode="extended")
    tree2.heading('col1', text="Files", anchor="w")
    tree2.column('col1', width=370)
    # tree.bind('<<TreeviewSelect>>', item_selected)
    tree2.place(relx=0.33 ,rely=0.176)

    scrollbar2 = ttk.Scrollbar(frame3, orient=tk.VERTICAL, command=tree2.yview)
    tree2.configure(yscroll=scrollbar2.set)
    scrollbar2.place(relx=0.81 ,rely=0.176, height=308+20)

    Button(frame3, text="Select All", fg=buttonFg, bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10).place(relx=0.85,rely=0.18)

    Button(frame3, text="Select None", fg=buttonFg, bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10).place(relx=0.85,rely=0.28)
    

    Button(frame3, text="Add", fg=buttonFg, bg=buttonBgSel_green, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10).place(relx=0.85,rely=0.38)
    

    Button(frame3, text="Play", fg=buttonFg, bg=buttonBgSel_blue, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10).place(relx=0.85,rely=0.76)


    Button(frame3, text="Stop", fg=buttonFg, bg=buttonBgSel_red, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10).place(relx=0.85,rely=0.86)
    


    

def tab4(frame4):
    ttk.Label(frame4, text="Settings",  font=("Arial Bold",defaultFontSize), background=DarkBg, foreground=DarkFg ).place(relx=0,rely=0.01)
    # nsl = ttk.Label(frame1, text="Song Arrangements", font=("Arial Bold",defaultFontSize), background=DarkBg, foreground=DarkFg)



def tab5(frame5):
    ttk.Label(frame5, text="About", background=DarkBg, foreground=DarkFg, font=defaultFontSize ).place(relx=0,rely=0.01)    