import tkinter as tk
from algo import longest_common_substring, lcs, dynamic_lcs, LCSubStr
import time
import numpy as np
import pandas as pd
import csv

def mean(nums):
    return float(sum(nums)) / max(len(nums), 1)

def search_song():
	keyword = lyric_text.get()
	print("Searching for song containing: " + lyric_text.get())
	total_matches=0
	searched=0
	readings=np.array([])
	#pd.read_csv("res\\lyrics.csv", encoding="utf8")
	total_time= time.time()
	
	with open("res\\lyrics.csv", encoding="utf8") as csvfile:
		reader = csv.DictReader(csvfile)
		row_num=0
		for row in reader:
			if row['genre'] == chosen_genre.get():
				#reg=lcs(keyword,row['lyrics'],len(keyword),len(row['lyrics']))
				count = 0
				start_time_dynamic = time.time()
				dynamic = LCSubStr(keyword, row['lyrics'], len(keyword), len(row['lyrics']))
				#dynamic=dynamic_lcs(keyword,row['lyrics']) 
				readings = np.append(readings,time.time()-start_time_dynamic)
				avg = np.mean(readings)	
				if dynamic == len(keyword):
					print("match found:",row['song'], row['artist'],dynamic)
					total_matches+=1
				searched+=1
				row_num+=1
		print("Total Searched:",searched,"Total Matches found:",total_matches)
		print("Average time spent on lcs:",avg,"Total Time spent:",time.time()-total_time)



pandas_csv = pd.read_csv("res\\lyrics.csv")
genres = pandas_csv['genre'].unique()





win = tk.Tk()
win.title("Algorithms Final Project - Music")

frame = tk.Frame(win)
frame.pack()

tk.Label(frame, text="Enter in the lyrics of a song").pack()
lyric_text = tk.StringVar()
tk.Entry(frame, textvariable=lyric_text).pack()
tk.Button(frame, text="Search", command=search_song).pack()
chosen_genre = tk.StringVar()
for g in genres:
	tk.Radiobutton(frame,text=g,variable=chosen_genre,value=g).pack()

win.mainloop()