from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def downloadVideo(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_streams = streams.get_highest_resolution()
        highest_res_streams.download(output_path = save_path)
        print("Video downloaded successfully!")

    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder


if __name__ == "__main__":  #make sure that you are directly running this python file before it eceuted anything that happens under this
    root = tk.Tk()   #instantiate the tk module and creates a window to enter
    root.withdraw()  #hide the window that won't be apperaring on the screen


    video_url = input("Please enter a url: ")
    save_dir = open_file_dialog()

    if  save_dir:
        print("Started download...")
        downloadVideo(video_url, save_dir)
        
    else:
         print("Invalid save location")