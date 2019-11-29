# A function that iterates through attributes of a 
# movie, but only pulls out the title and director.

movie = {
    'title': 'a',
    'releaseYear': 2018,
    'rating': 4.5,
    'director': 'b'
}

for key in movie:
    if key == 'title' or key == 'director':
        print(key + ": " + str(movie[key]))
