import media
from bottle import route, template

@route('/')
def index():
    toy_story = media.Movie(
        'Toy Story',
        'Toys come to life',
        'http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg',
        'https://youtu.be/vwyZH85NQC4')
    avatar = media.Movie(
        'Avatar',
        'Pocahontas on an alien planet',
        'http://img.csfd.cz/files/images/user/profile/159/129/159129345_9e5fe4.jpg',
        'https://youtu.be/uZNHIU3uHT4')
    movies = [toy_story, avatar]
    return template('fresh_tomatoes', movies=movies)