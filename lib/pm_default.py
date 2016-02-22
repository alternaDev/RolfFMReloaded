from playing_mode import PlayingMode
from rp_default import DefaultRepeat
from random_file_provider import RandomFileProvider
from props import Properties
import time


class DefaultMode(PlayingMode):

    last_speech = Properties.DEFAULT_SPEECH_COUNT

    def __init__(self, name, source,  speech):
        PlayingMode.__init__(self, name, source)
        self.repeat_pattern = DefaultRepeat()
        self.name = "DefaultMode " + str(name)
        self.content_provider = RandomFileProvider(False, source)
        self.speech_provider = RandomFileProvider(True, speech)
        self.priority = 1
        self.time_counter = 0
        self._playing_time = 0
        self.start_time = 0

    def next(self):
        PlayingMode.next(self)
        if DefaultMode.last_speech >= Properties.DEFAULT_SPEECH_COUNT:
            next_song = self.speech_provider.next()
            DefaultMode.last_speech = 0
        else:
            next_song = self.content_provider.next()
            DefaultMode.last_speech += 1
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
