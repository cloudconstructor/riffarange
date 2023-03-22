from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style
from tkinter.messagebox import showinfo

#styling def
DarkBg = "#333"
DarkBg2 = "#222"
DarkBg3 = "#111"
DarkFg = "#fff"
defaultFont = "verdana"
defaultFontSize_tab = 13
defaultFontSize_title = 15
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



def initWindow():
    global root
    root = tk.Tk()
    root.geometry('800x480')
    root.resizable(False, False)
    root.title('RiffArange v0.5')
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
            
        } 
    )

    style.theme_use('mytheme')
    style.configure('Dark.TFrame', background=DarkBg)
    style.configure('Dark2.TFrame', background=DarkBg2)
    style.configure('Dark3.TFrame', background=DarkBg3)

    return style


def tab1(frame1):
    nsl = ttk.Label(frame1, text="Song Arrangements", font=("Arial Bold",defaultFontSize_title), background=DarkBg, foreground=DarkFg)
    nsl.place(relx=0,rely=0.03)

    nsb = Button(frame1, text="Create new", fg="white", bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    nsb.place(relx=0.85,rely=0.13)

    psb = Button(frame1, text="Edit", fg="white", bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    psb.place(relx=0.85,rely=0.23)

    psb = Button(frame1, text="Delete", fg="white", bg=buttonBgSel_gray, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    psb.place(relx=0.85,rely=0.33)


    nsb = Button(frame1, text="Play", fg="white", bg=buttonBgSel_blue, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    nsb.place(relx=0.85,rely=0.70)

    nsb = Button(frame1, text="Stop", fg="white", bg=buttonBgSel_red, relief=FLAT, font=(defaultFont,buttonFontSize), padx=5, pady=5 , command=NONE, width=10)
    nsb.place(relx=0.85,rely=0.80)


    # songlist ---------------------------------
    columns = ('first_name', 'last_name', 'email')
    tree = ttk.Treeview(frame1, columns=columns, show='headings',style="mytheme.Treeview", height="15",  selectmode="extended")


    # define headings
    tree.heading('first_name', text='Name', anchor="w")
    tree.heading('last_name', text='Description', anchor="w")
    tree.heading('email', text='Tuning', anchor="w")

    # generate sample data -----------------------------------------------------
    contacts = []
    for n in range(1, 100):
        contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

    # add data to the treeview
    for contact in contacts:
        tree.insert('', tk.END, values=contact)

    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            # show a message
            # showinfo(title='Information', message=','.join(record))

    # --------------------------------------------------------------------------

    tree.bind('<<TreeviewSelect>>', item_selected)
    tree.place(relx=0.005 ,rely=0.12)

    # add a scrollbar
    scrollbar = ttk.Scrollbar(frame1, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.place(relx=0.78 ,rely=0.12, height=310+20)

def tab2(frame2):
    ttk.Label(frame2, text="Audio Files", font=("Arial Bold",defaultFontSize_title), background=DarkBg, foreground=DarkFg).grid(column = 1,row = 1)

def tab3(frame3):
    ttk.Label(frame3, text="Folders", font=("Arial Bold",defaultFontSize_title), background=DarkBg, foreground=DarkFg).grid(column = 1,row = 1)