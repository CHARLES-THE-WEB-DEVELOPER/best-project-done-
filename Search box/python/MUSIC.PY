import os
import tkinter as tk
from pygame import mixer
from tkinter import filedialog

# Initialize the mixer
mixer.init()

# Create the App Window
root = tk.Tk()  # Main window
root.title("Music Player")
root.geometry("400x350")
root.config(bg='black')

# Create the Listbox widget
playlist = tk.Listbox(
    root, 
    bg="black",
    fg="white",
    width=50,
    selectbackground="gray",
    selectforeground="white"
)
playlist.pack(pady=20)

# Playback functions
def play_music():
    song = playlist.get(tk.ACTIVE)
    mixer.music.load(song)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def resume_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

# Load music function
def load_music():
    directory = filedialog.askdirectory()
    if directory:
        os.chdir(directory)
        songs = os.listdir(directory)
        playlist.delete(0, tk.END)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(tk.END, song)

# Control Buttons
control_frame = tk.Frame(root, bg="#1e1e1e")
control_frame.pack()

tk.Button(control_frame, text="Play", 
          command=play_music, width=10,
          bg="green").grid(row=0, column=0, padx=5)

tk.Button(control_frame, text="Pause", 
          command=pause_music, width=10,
          bg="orange").grid(row=0, column=1, padx=5)

tk.Button(control_frame, text="Resume", 
          command=resume_music, width=10,
          bg="blue").grid(row=0, column=2, padx=5)

tk.Button(control_frame, text="Stop", 
          command=stop_music, width=10,
          bg="red").grid(row=0, column=3, padx=5)

tk.Button(root, text="Load Music Folder", 
          command=load_music, width=20,
          bg="#444").pack(pady=10)

# Run the APP
root.mainloop()