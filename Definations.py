from tkinter import messagebox
from pytube import YouTube


res=[]
def download(url,itag):
    yt=YouTube(url)
    try:
        stream=yt.streams.get_by_itag(itag)
        stream.download()
    except:
        messagebox.showerror ('','Dowanload Failed!')

def searching_resolution(url):
    try:
        yt=YouTube(url)
        title=yt.title
        thum=yt.thumbnail_url
        messagebox.showinfo("",'title=:'+title+"\n")
        print(thum)
        ar=yt.streams.filter(file_extension='mp4')
        l=[]
        for item in str(ar).split():
            if 'itag=' in item or 'res=' in item:
                l.append(item)

        first=True   
        for i in l:
            if first:
                x=i
                first=False
            else:
                res.append([x,i])
                first=True
    except:
        messagebox.showerror('','Couldnt find video!')
    