from SQliteConnect import *

import read

import time




def deleteSongs():

    # songID of the record to be updated

    idField = input("Enter the songID of the song to be deeted : ")



    cursor.execute(f"DELETE FROM songs WHERE SongID={idField}")

    conn.commit()



    print(f"Record {idField} deleted")

    time.sleep(3)

    read.readSongs()  # invoke readSongs subroutine from the read app




deleteSongs()
