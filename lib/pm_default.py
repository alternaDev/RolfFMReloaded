from playing_mode import PlayingMode

class DefaultMode(PlayingMode):
    def __init__(self, source):
        PlayingMode.__init__(self)
        self.repeat_pattern = DefaultRepeat()
        self.name = "DefaultMode " + str(source)
        self.content_provider = RandomFileProvider(False, source)
        self.priority = 1
        self.time_counter = 0

    def next(self):
        next_song = self.content_provider.next()        
        return next_song
