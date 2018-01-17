"""Provides a Movie class for holding movie data.
"""
import webbrowser


class Movie(object):
    """Holding data for a movie.
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        # A movie has four properties: title, storyline, poster and trailer.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens a web page of the movie's trailer.
        """
        webbrowser.open(self.trailer_youtube_url)