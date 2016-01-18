from playing_mode import PlayingMode
from rp_default import DefaultRepeat
from random_file_provider import RandomFileProvider

class DefaultMode(PlayingMode):
    def __init__(self, name, source):
        PlayingMode.__init__(self, name, source)
        self.repeat_pattern = DefaultRepeat()
        self.name = "DefaultMode " + str(name)
        self.content_provider = RandomFileProvider(False, source)
        self.priority = 1
        self.time_counter = 0

    def next(self):
        next_song = self.content_provider.next()
        return next_song
