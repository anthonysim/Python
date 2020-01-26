# imports sqlite from python
import sqlite3

# creates domain_db.sqlite if it doesn't exist or connects to it if it
# exists. cursor() is like "opening" the file, but it opens the DB.
connect_db = sqlite3.connect('domain_db.sqlite')
cursor_db = connect_db.cursor()

# erases the TABLE Counts if EXISTS
# CREATES a table called Counts
cursor_db.execute('DROP TABLE IF EXISTS Counts')
cursor_db.execute('''
CREATE TABLE Counts(
  org TEXT,
  count INTEGER)''')

# prompts user for the file, then opens it 
fname = input('File name: ')
fhandle = open(fname)

# for loop through the file, looks for everything that starts with
# From: splits the line, picks up the email, then splits from the @
# then picks up only the domain.
for line in fhandle:
    if not line.startswith('From: '):
        continue
    line = line.split()
    email = line[1]
    email = email.split('@')
    org = email[1]
    cursor_db.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cursor_db.fetchone()
    if row is None:
        cursor_db.execute('''INSERT INTO Counts (org, count)
                          VALUES (?, 1)''', (org, ))
    else:
        cursor_db.execute('''UPDATE Counts
                          SET count = count + 1
                          WHERE org = ?''', (org, ))
    connect_db.commit()

sqlstr = '''SELECT org, count FROM Counts ORDER BY count DESC'''

for row in cursor_db.execute(sqlstr):
    print(str(row[0]), row[1])

cursor_db.close()
