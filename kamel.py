from tkinter import *
from yt_dlp import YoutubeDL

def hight_quality():
    try:
       url= Entry.get()
 
       ydl_opts = {
           
             'format':'best',
             'outtmpl':'downloads%(titles)s.%(ext)s'
       }
       with YoutubeDL(ydl_opts) as ydl:
         ydl.download([url])
         print("the vedio has been downloaded")

    except Exception as e:
        print("error downloading")



def low_quality():
    try:
       url= Entry.get()
 
       ydl_opts = {
           
             'format':'worst',
             'outtmpl':'downloads%(titles)s.%(ext)s'
       }
       with YoutubeDL(ydl_opts) as ydl:
         ydl.download([url])
         print("the vedio has been downloaded")

    except Exception as e:
        print("error downloading")

def audio():
    try:
       url= Entry.get()
 
       ydl_opts = {
           
             'format':'bestaudio',
             'outtmpl':'downloads%(titles)s.%(ext)s'
       }
       with YoutubeDL(ydl_opts) as ydl:
         ydl.download([url])
         print("the vedio has been downloaded")

    except Exception as e:
        print("error downloading")






window = Tk()
window.title("kamel")
window.configure(bg="aqua")
window.geometry("600x400")
Label=Label( window,text="add your link here",font="bold",bg=window['bg'])
Label.place(x=200,y=30)
Entry=Entry(window,width=50)
Entry.place(x=150,y=100)
hight=Button(window,text="hight quality",command=hight_quality,font="bold",activeforeground="blue")
hight.place(x=100,y=200)
low=Button(window,text="low quality",command=low_quality,font="bold",activeforeground="blue")
low.place(x=250,y=200)
audio=Button(window,text="audio quality",command=audio,font="bold",activeforeground="blue")
audio.place(x=400,y=200)
window.mainloop()