import threading
import re
from tkinter import *
from tkinter.ttk import *
import time
import Definations

win=Tk()
win.title("streamDownload")


url=StringVar()
File_name=StringVar()
resol=StringVar()
resolutions=[]


def res_buttons(arg):
    progres_label.config(text='')
    win.update_idletasks()   
    temp = re.findall(r'\d+', arg)
    result = list(map(int, temp))
    download_thread=threading.Thread(target=Definations.download,args=(url.get(),result[0]))
    download_thread.start()
    bar = [
            "               ",
            " D             ",
            " Do            ",
            " Dow           ",
            " Down          ",
            " Downl         ",
            " Downlo        ",
            " Downloa       ",
            " Download      ",
            " Downloadi     ",
            " Downloadin    ",
            " Downloading   ",
            " Downloading.   ",
            " Downloading.. ",
            " Downloading...",
            "  ownloading...",
            "   wnloading...",
            "    nloading...",
            "     loading...",
            "      oading...",
            "       ading...",
            "        ding...",
            "         ing...",
            "          ng...",
            "           g...",
            "            ...",
            "             ..",
            "              .",
            "               ",
            "               ",


    ]
    i = 0
        
    while download_thread.is_alive():
        progres_label.config(text=bar[i % len(bar)]+'\r')
        time.sleep(.2)
        i += 1
        win.update_idletasks()
    progres_label.config(text='Download Complete')
    win.update_idletasks()
    Definations.res=[]

def sort(res):
    win2=Tk()
    row=0
    col=0
    for i in res:
        res_button=Button(win2,text=i,command=lambda i=i:[win2.destroy(),threading.Thread(target=res_buttons(i[0]),daemon=True)])
        res_button.grid(row=row,column=col,pady=5,padx=10)
        col+=1
        if col==3:
            row+=1
            col=0
    win2.mainloop()


def Search():
    res=threading.Thread(target=Definations.searching_resolution,args=(url.get(),),daemon=True)
    res.start()

    bar = [
            "             ",
            " S           ",
            " Se          ",
            " Sea         ",
            " Sear        ",
            " Searc       ",
            " Search      ",
            " Searchi     ",
            " Searchin    ",
            " Searching   ",
            " Searching.  ",
            " Searching.. ",
            " Searching...",
            "  earching...",
            "   arching...",
            "    rching...",
            "     ching...",
            "      hing...",
            "       ing...",
            "        ng...",
            "         g...",
            "          ...",
            "           ..",
            "            .",
            "             ",
            "             ",

    ]
    i = 0
        
    while res.is_alive():
        progres_label.config(text=bar[i % len(bar)]+'\r')
        time.sleep(.2)
        i += 1
        win.update_idletasks()
    progres_label.config(text='Search Complete')
    win.update_idletasks()
    sort(Definations.res)


def main_threads():
    main_thread=threading.Thread(target=Search)
    main_thread.setDaemon=True
    main_thread.start()   

#contents
progres_label=Label(win)
progres_label.pack()
frame1=Frame(win)
frame1.pack()

label1=Label(frame1,text="url:")
label1.grid(row=0,column=1,pady=40,padx=5)
link_url=Entry(frame1,width=50,textvariable=url)
link_url.grid(row=0,column=2,pady=40,padx=5)

botton1=Button(win,text="Search",command=main_threads)
botton1.pack(pady=10)




win.mainloop()