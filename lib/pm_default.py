from playing_mode import PlayingMode
from rp_default import DefaultRepeat
from random_file_provider import RandomFileProvider
import time

class DefaultMode(PlayingMode):
    def __init__(self, name, source):
        PlayingMode.__init__(self, name, source)
        self.repeat_pattern = DefaultRepeat()
        self.name = "DefaultMode " + str(name)
        self.content_provider = RandomFileProvider(False, source)
        self.priority = 1
        self.time_counter = 0
        self._playing_time = 0
        self.start_time = 0

    def next(self):
        PlayingMode.next(self)
        next_song = self.content_provider.next()
        return next_song

    def on_play(self):
        self.start_time = time.time()

    def on_stop(self):
        self.playing_time += (time.time() - self.start_time)

    @property
    def playing_time(self):
        return self._playing_time

    @playing_time.setter
    def playing_time(self, val):
        self._playing_time = val
