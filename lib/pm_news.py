import cherrypy

from playing_mode import PlayingMode
from rp_hourly import HourlyRepeat
from news_file_provider import NewsFileProvider

class NewsMode(PlayingMode):
    def __init__(self, data):
        source = data.get('source', '')
        PlayingMode.__init__(self, "NewsMode")
        self.repeat_pattern = HourlyRepeat()
        self.name = "NewsMode"
        self.content_provider = NewsFileProvider(source)
        self.priority = -1
        self.time_counter = 0

    def next(self):
        PlayingMode.next(self)
        next_song = self.content_provider.next()
        return next_song

    def web(self):
        class NewsWeb(object):
            @cherrypy.expose
            def index(self):
                return "Hello World!"

        return NewsWeb