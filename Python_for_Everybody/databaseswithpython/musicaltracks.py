# imports ET and sql
import xml.etree.ElementTree as ET
import sqlite3

# creates and connect to 'trackdb.sqlite'
connect_db = sqlite3.connect('trackdb.sqlite')
# creates a cursor object
cursor_db = connect_db.cursor()

# erases artist, genre, album, & track tables if they exist
# creates tables for artist, genre, album & track shortly after
cursor_db.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    artist_id  INTEGER,
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# prompts file name
fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) :
        continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre = lookup(entry, 'Genre')

    if name is None or artist is None or album is None :
        continue

    # print(name, artist, album, count, rating, length)

    cursor_db.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    cursor_db.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cursor_db.fetchone()[0]

    cursor_db.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', (genre, ) )
    cursor_db.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cursor_db.fetchone()[0]

    cursor_db.execute('''INSERT OR IGNORE INTO Album (name)
        VALUES ( ? )''', (album, ) )
    cursor_db.execute('SELECT id FROM Album WHERE name = ? ', (album, ))
    album_id = cursor_db.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ? )''',
        ( name, album_id, length, rating, count ) )

    conn.commit()

cursor_db.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track JOIN Genre JOIN Album JOIN Artist
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3''')
