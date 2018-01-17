"""Rendering local movie data in html.
"""

# Uses udacity provided library for html rendering.
import fresh_tomatoes
import media

WIKI_URL = 'https://upload.wikimedia.org/wikipedia/en/'

YOUTH = media.Movie(
    'Youth',
    'A story of a man and four women in the old days of China.',
    WIKI_URL + '3/34/Bloom_of_Youth.jpg',
    'https://youtu.be/lmXSOeb270Y')

FAREWELL_TO_MY_CONCUBINE = media.Movie(
    'Farewell to my concubine',
    'Two gay man in China during political turmoil time.',
    WIKI_URL + 'c/c5/Farewell_My_Concubine_poster.jpg',
    'https://youtu.be/cC-_SLiRnJE')

INTERSTELLAR = media.Movie(
    'Interstellar',
    'A father travles in time to save the earth.',
    WIKI_URL + 'b/bc/Interstellar_film_poster.jpg',
    'https://youtu.be/0vxOhd4qlnA')

# Defines a list of movies
MOVIES = [YOUTH, FAREWELL_TO_MY_CONCUBINE, INTERSTELLAR]

fresh_tomatoes.open_movies_page(MOVIES)
