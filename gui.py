import tkinter as tk

def search_song():
	print("Searching for song containing: " + lyric_text.get())
	
win = tk.Tk()
win.title("Algorithms Final Project - Music")

frame = tk.Frame(win)
frame.pack()

tk.Label(frame, text="Enter in the lyrics of a song").pack()
lyric_text = tk.StringVar()
tk.Entry(frame, textvariable=lyric_text).pack()
tk.Button(frame, text="Search", command=search_song).pack()

win.mainloop()