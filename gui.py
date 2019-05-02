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
	for index, row in artist_songs.iterrows():
		#TODO: use pandas_csv.head().iterrows() to compmare the different algorithms and report the average time for each run
		if row['genre'] == chosen_genre.get():
			if row['artist'].lower() == artist.lower():
				start_time_dynamic = time.time()
				try:
					dynamic = LCSubStr(keyword.lower(), row['lyrics'].lower(), len(keyword), len(row['lyrics']))
				except:
					print("error")
				#dynamic=dynamic_lcs(keyword,row['lyrics']) 
				readings = np.append(readings,time.time()-start_time_dynamic)
				avg = np.mean(readings)	
				if dynamic == len(keyword):
					print("match found:",row['song'], row['artist'],dynamic)
					total_matches+=1
				searched+=1
	if total_matches > 0:
		print("Total Searched:",searched,"Total Matches found:",total_matches)
		print("Average time spent on lcs:",avg,"Total Time spent:",time.time()-total_time)

def on_keyrelease(event):

    # get text from entry
    value = event.widget.get()
    value = value.strip().lower()

    # get data from test_list
    if value == '':
        data = pandas_csv[pandas_csv['genre'].str.contains(chosen_genre.get())]['artist'].unique().tolist()
    else:
        data = []
        for item in pandas_csv[pandas_csv['genre'].str.contains(chosen_genre.get())]['artist'].unique().tolist():
            if value in item.lower():
                data.append(item)                

    # update data in listbox
    listbox_update(data)

	
def listbox_update(data):
    # delete previous data
    listbox.delete(0, 'end')

    # sorting data 
    data = sorted(data, key=str.lower)

    # put new data
    for item in data:
        listbox.insert('end', item)


def on_select(event):
    # display element selected on list
	# if event.widget.curselection()
	global artist
	artist = event.widget.get(event.widget.curselection())
	global artist_songs
	artist_songs = pandas_csv[pandas_csv['artist'] == artist]



artist = ""
df = pd.read_csv("res\\lyrics.csv")
#pandas_csv.dropna(axis=0,how="any")
pandas_csv = df[df['lyrics'].notnull()]
#TODO: lowercase the lyrics in database and lowercase all input from user
genres = pandas_csv['genre'].unique()
artists = pandas_csv['artist'].unique().tolist()
artists.sort()



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
tk.Label(frame, text="Optional: Artist").pack()
entry = tk.Entry(win)
entry.pack()
entry.bind('<KeyRelease>', on_keyrelease)
listbox = tk.Listbox(win)
listbox.pack()
listbox.bind('<<ListboxSelect>>', on_select)
listbox_update(artists)


# tk.Listbox(frame,artist,*artists).pack()
win.mainloop()




