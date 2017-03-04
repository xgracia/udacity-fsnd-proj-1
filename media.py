class Movie():
    """Movie
    
    Attributes:
        title       (str) : The title of the movie.
        storyline   (str) : The storyline of the movie.
        image_url   (str) : The URL of the movie's poster image.
        trailer_url (str) : The URL of the movie's youtube trailer.
    """
    def __init__(self, title, storyline, image_url, trailer_url):
        self.title = title
        self.storyline = storyline
        self.image_url = image_url
        self.trailer_url = trailer_url
