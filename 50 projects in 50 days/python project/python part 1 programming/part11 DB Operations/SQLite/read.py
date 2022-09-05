from SQliteConnect import *




def readSongs():

    cursor.execute("SELECT * FROM songs")  # select all records from songs table



    row = cursor.fetchall()  # fetch all the songs that was selected in the table



    for (

        record

    ) in (

        row

    ):  # iterate through all the records held in the row variable and print one at a time

        print(record)




# readSongs()  # invoke/call read songs subroutine