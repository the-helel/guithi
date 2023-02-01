# import tkinter as tk
# from tkinter import filedialog, ttk
# import sys
# from moviepy.editor import *

# def select_video():
#     global file_path
#     file_path = filedialog.askopenfilename()

# def compress_video():
#     global file_path, pb, info_text
#     video = VideoFileClip(file_path)
    

#     video_resized = video.resize(0.9)


#     save_path = filedialog.asksaveasfilename(defaultextension=".mp4")
#     video_resized.write_videofile(save_path)
#     print("Compression complete")

# class StdoutRedirector(object):
#     def __init__(self, widget):
#         self.widget = widget

#     def write(self, string):
#         self.widget.insert(tk.END, string)
#         self.widget.see(tk.END)
#         root.update()

# class StderrRedirector(object):
#     def __init__(self, widget):
#         self.widget = widget

#     def write(self, string):
#         self.widget.insert(tk.END, string)
#         self.widget.see(tk.END)
#         root.update()


# root = tk.Tk()
# root.title("Video Compression")
# root.geometry("800x600")


# info_text = tk.Text(root, height=20, width=100)
# info_text.pack()

# sys.stdout = StdoutRedirector(info_text)
# sys.stderr = StderrRedirector(info_text)


# select_video_btn = tk.Button(root, text="Select Video", command=select_video)
# compress_video_btn = tk.Button(root, text="Compress Video", command=compress_video)

# select_video_btn.pack()
# compress_video_btn.pack()


# root.mainloop()












import tkinter as tk
from tkinter import filedialog, ttk
import sys
from moviepy.editor import *
import time

def select_video():
    global file_path
    file_path = filedialog.askopenfilename()

def compress_video():
    global file_path, pb, info_text
    video = VideoFileClip(file_path)
    

    video_resized = video.resize(0.2)


    save_path = filedialog.asksaveasfilename(defaultextension=".mp4")
    video_resized.write_videofile(save_path)
    print("Compression complete")
    info_text.delete("1.0", tk.END)


class StdoutRedirector(object):
    def __init__(self, widget):
        self.widget = widget

    def write(self, string):
        self.widget.insert(tk.END, string)
        self.widget.see(tk.END)
        root.update()

class StderrRedirector(object):
    def __init__(self, widget):
        self.widget = widget

    def write(self, string):
        self.widget.insert(tk.END, string)
        self.widget.see(tk.END)
        root.update()


root = tk.Tk()
root.title("Video Compression")
root.geometry("900x700")
root.config(bg='#1C1C1E')

frame = tk.Frame(root, bg='#1C1C1E')
frame.pack(pady=100)

info_text = tk.Text(frame, height=20, width=100, bg='#1C1C1E', fg='#FFFFFF')
info_text.pack()

sys.stdout = StdoutRedirector(info_text)
sys.stderr = StderrRedirector(info_text)


select_video_btn = tk.Button(frame, text="Select Video", command=select_video, bg='#FFFFFF', fg='#1C1C1E')
compress_video_btn = tk.Button(frame, text="Compress Video", command=compress_video, bg='lightgreen', fg='#1C1C1E')

select_video_btn.pack(pady=20)
compress_video_btn.pack(pady=20)


root.mainloop()






























