from bottle import route, template

@route('/')
def index():
    movies = [{
        'movie_title': 'Toy Story',
        'poster_image_url': 'http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg',
        'trailer_url': 'https://youtu.be/vwyZH85NQC4'
    },{
        'movie_title': 'Avatar',
        'poster_image_url': 'http://img.csfd.cz/files/images/user/profile/159/129/159129345_9e5fe4.jpg',
        'trailer_url': 'https://youtu.be/uZNHIU3uHT4'
    }]
    return template('fresh_tomatoes', movies=movies)