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
        'https://theflyinyoursoup.files.wordpress.com/2016/08/avatar-1st.jpeg',
        'https://youtu.be/uZNHIU3uHT4')
    movies = [toy_story, avatar]
    return template('fresh_tomatoes', movies=movies)