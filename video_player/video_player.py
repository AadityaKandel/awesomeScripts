import cv2
import os
from pathlib import Path
from ffpyplayer.player import MediaPlayer
from tkinter import filedialog
from tkinter import *
import tkinter.messagebox as msg
# New Way Of Opening File

root = Tk()
root.title('Video_Player By Deepak Raj')
root.geometry('400x200')

def ask_dir():

    b1.config(text="Exit Video",command=exitter)

    video_directory_path = filedialog.askopenfilename(initialdir="")

    def PlayVideo():

        video = cv2.VideoCapture(video_directory_path)
        player = MediaPlayer(video_directory_path)

        while True:
            root.update()
            grabbed, frame = video.read()
            audio_frame, val = player.get_frame()
            if not grabbed:
                msg.showwarning('Warning',"Video File Is Needed")
                os.system('cls')
                break
            if cv2.waitKey(28) & 0xFF == ord("q"):
                break
            cv2.imshow("Video", frame)
            if val != "eof" and audio_frame is not None:
                img, t = audio_frame
        video.release()
        cv2.destroyAllWindows()

    try:

        PlayVideo()

    except:

        msg.showwarning('Warning',"Video File Is Needed")

def exitter():
    os.system('taskkill /PID python.exe /F')
    b1.config(text="Play Video",command=ask_dir)

def emp():
    Label(bg='black',fg="black").pack()

emp()
emp()
emp()    

b1 = Button(text="Play Video",bg="white",fg="black",font="comicsansms 20 italic",relief=SUNKEN,command=ask_dir,justify=CENTER)
b1.pack()


# print (video_directory_path)


root.config(bg="black")
root.mainloop()
