from SQliteConnect import *

import time

# create a subroutine to add songs to the songs table in the database

def addSongs():

    # create an empty list

    songs = []



    title = input("Enter song title: ")

    artist = input("Enter artist name: ")

    genre = input("Enter song genre: ")



    # append data captured from the user into the song list

    " songs.SongID is set to auto increment and would be added automatically"



    songs.append(title)

    songs.append(artist)

    songs.append(genre)



    # insert data from the list into songs table



    cursor.execute("INSERT INTO songs VALUES(NULL, ?, ?, ?)",songs)

    conn.commit() # commit/write changes permanently to the database

    print(f"{title} added to songs table")



    time.sleep(3)



    cursor.execute("SELECT * FROM songs") # select all records from songs table



    row = cursor.fetchall() # fetch all the songs that was selected in the table



    for record in row: #iterate through all the records held in the row variable and print one at a time

        print(record)



addSongs() # call/invoke the subroutine