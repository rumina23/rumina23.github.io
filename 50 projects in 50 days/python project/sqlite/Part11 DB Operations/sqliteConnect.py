import sqlite3  # import the sqlite molude/library



"create a variable conn and pass sqlite connect method to it"

"create a database file if it does not exists, otherwise it will just use the existing db file"



conn = sqlite3.connect("Part11 DB Operations/SQLite/c11SQLite.db")

"cursor method iterates through the database/tables"

cursor = conn.cursor()