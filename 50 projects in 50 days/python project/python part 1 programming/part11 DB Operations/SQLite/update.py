from SQliteConnect import *

import read

import time



def updateSongs():

    #songID of the record to be updated

    idField = input("Enter the songID of the song to be updated : ")

    # enter the name of the field to be updated

    fieldName = input("Which field would you like to update(Title, Artist, Genre?): ")

    #Enter the new field value

    newfieldValue = input(f"Enter the new field value for {fieldName}")

    print(f"The new field value enteed is {newfieldValue}")



    # add single quotes around the field value entered by the user

    # name =  Anna . now name = " ' " +  Anna + "  ' ""



    newfieldValue = "'" + newfieldValue + "'"

    print(f"The new field value enteed is {newfieldValue}")



    # update the song in songs table

    "UPDATE songs SET Title/Artist/Genre = newfieldValue(Bad/MJ/pop) "

    cursor.execute(f"UPDATE songs SET {fieldName} = {newfieldValue} WHERE SongID = {idField}")

    conn.commit()



    print(f"Record {idField} updated")

    time.sleep(3)

    read.readSongs() #invoke readSongs subroutine from the read app



updateSongs() # call/invoke update songs subroutine