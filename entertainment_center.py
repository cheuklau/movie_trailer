# entertainment_center.py
# Author: Cheuk Lau
# Project: Movie Trailer Website
# Date: 5/2/2018

import media


def get_movies():
    ''' Fetches list of movie objects.

    Retrieves a list of movie objects for use in open_movies_page().

    Args:
        None

    Returns:
        List of movie objects
    '''

    # Create instance of The Fast and the Furious
    ff1 = media.Movie('https://www.youtube.com/watch?v=2TAOizOnNPo',
    'The Fast and the Furious',
    'https://upload.wikimedia.org/wikipedia/en/5/54/Fast_and_the_furious_poster.jpg')  # NOQA

    # Create instance of The Fast and the Furious 2
    ff2 = media.Movie('https://www.youtube.com/watch?v=ZZGkV_xWGw4',
    '2 Fast 2 Furious',
    'https://upload.wikimedia.org/wikipedia/en/9/9d/Two_fast_two_furious_ver5.jpg')  # NOQA

    # Create instance of The Fast and the Furious: Tokyo Drift
    ff3 = media.Movie('https://www.youtube.com/watch?v=p8HQ2JLlc4E',
    'The Fast and the Furious: Tokyo Drift',
    'https://upload.wikimedia.org/wikipedia/en/4/4f/Poster_-_Fast_and_Furious_Tokyo_Drift.jpg')  # NOQA

    # Note: Removed Fast and Furious 4 and 5 trailers as they are required
    # to be played on Youtube, and therefore will not appear on the website.

    # Create instance of Fast and Furious 6
    ff4 = media.Movie('https://www.youtube.com/watch?v=C_puVuHoR6o',
    'Fast and Furious 6',
    'https://upload.wikimedia.org/wikipedia/en/f/fd/FastandFurious6-teaserposter.jpg')  # NOQA

    # Create instance of Fast and Furious 7
    ff5 = media.Movie('https://www.youtube.com/watch?v=Skpu5HaVkOc',
    'Fast and Furious 7',
    'https://upload.wikimedia.org/wikipedia/en/b/b8/Furious_7_poster.jpg')  # NOQA

    # Create instance of Fast and Furious 8
    ff6 = media.Movie('https://www.youtube.com/watch?v=uisBaTkQAEs',
    'The Fate of the Furious',
    'https://upload.wikimedia.org/wikipedia/en/2/2d/The_Fate_of_The_Furious_Theatrical_Poster.jpg')  # NOQA

    # Store movie objects in a list
    result = [ff1, ff2, ff3, ff4, ff5, ff6]

    return result
