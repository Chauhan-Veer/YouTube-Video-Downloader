
from tkinter import *
from tkinter import messagebox
from pytube.__main__ import YouTube
root = Tk()
root.title("Video Downloder by Veer Chauhan")
root.geometry("350x500")
root.maxsize(350, 500)
root.minsize(350, 500)

def link_get():
    url= YouTube(str(video_list.get()))

    video = url.streams.first()

    video = url.streams.filter(file_extension=' ')
    # video.download("/home/veer/Desktop")
    messagebox.showinfo("info", "Video has been Downloded")




video_list = StringVar()


Name = Label(root, text="")
link = Label(root, text="Paste the link here").pack()

link_entry = Entry(root,textvariable=video_list , width=30)
link_entry.pack()



Button(root, text="Download", command=link_get).pack()

root.mainloop()