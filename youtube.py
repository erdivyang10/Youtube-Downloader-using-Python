#Welcome to the Github Page
#Author: Divyang Goswami
#email: erdivyang10@gmail.com
#Linkedin: https://in.linkedin.com/in/divyang-goswami-a0885246
#website: https://divyanggoswami.github.io/

#Description: Download Youtube Video Instatly using this downloader


from tkinter import *
from pytube import YouTube


root = Tk()
root.geometry("500x500")
root.title("Youtube Downloader")


Label(root, text="Youtube Downloader", font="Helvtica 24 bold", height=2).pack(pady=20)

Label(root, text="Paste YouTube Video Link: ", font="Helvtica 10 ").pack(pady=10)
entry = Entry(root,width=70)
entry.pack()

def youtube_download():
    Label(root,text="Downloading......").pack()
    yt_video = entry.get()

    if yt_video == '':
        Label(root,text="Field should not be blank").pack()

    else:

        yt =YouTube(yt_video)      
        yt.streams.filter(progressive=True).first().download()

        
        Label(root,text="Done...Your file has been Downloaded").pack()


def close_window():
    root.destroy()
           

download = Button(root,text="Download ",command=youtube_download, font = 'arial 14 bold' ,bg = 'white', padx = 2)
download.pack(pady=20)

close = Button(root,text="Quit",command=close_window,font = 'arial 12 bold' ,bg = 'white', padx = 2)
close.pack(pady=10)



author = Label(root, text= "GUI Application By Divyang Goswami")
author.place(relx = 0.0,  rely = 1.0, anchor ='sw')
root.mainloop()