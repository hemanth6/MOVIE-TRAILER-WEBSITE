import webbrowser


class Movie():  # class with instance variables
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 movie_poster,
                 movie_trailer):
        self.title = movie_title
        self.story_line = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):  # method used to show youtube video
        webbrowser.open(self.trailer_youtube_url)

