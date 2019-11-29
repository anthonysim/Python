# A function that iterates through attributes of a 
# movie, but only pulls out the title and director.
# checks if the value is a string, if it is it gets printed.

movie = {
    'title': 'a',
    'releaseYear': 2018,
    'rating': 4.5,
    'director': 'b'
}

for key in movie:
    if type(movie[key]) == str:
        print(key + ": " + str(movie[key]))
