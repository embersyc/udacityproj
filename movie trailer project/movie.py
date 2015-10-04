import webbrowser

# this class contains the data for a movie

class Movie():
    """
    Use this class to store data related to a movie.
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
        Movie class constructor.
        @param self: This is a special parameter used by Python to refer to instance variables.
                     Similar to 'this' keyword in other languages.
                     Do not pass this parameter to constructor.
        @param movie_title: The title of the movie.
        @param movie_storyline: A brief description of the movie
        @param poster_image: The URL of the Movie's poster image.
        @param trailer_youtube: The URL of the Movie's trailer on youtube.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Use this method to open a browser and play the youtube trailer.
        @param self: This is a special parameter used by Python to refer to instance variables.
                     Similar to 'this' keyword in other languages.
                     Do not pass this parameter to method.
        """
        webbrowser.open(self.trailer_youtube_url);
