# media.py
# Author: Cheuk Lau
# Project: Movie Trailer Website
# Date: 5/2/2018


class Movie():
    '''
    Movie objects for use in fresh_tomatoes.py.

    Attributes:
        trailer_youtube_url (str): A string of youtube link to trailer.
        title               (str): A string of movie title.
        poster_image_url    (str): A string of link to movie poster.
	'''
    def __init__(self, trailer, title, poster):
        self.trailer_youtube_url = trailer
        self.title = title
        self.poster_image_url = poster
