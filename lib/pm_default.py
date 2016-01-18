from playing_mode import PlayingMode

class DefaultMode(PlayingMode):
    def __init__(self):
        PlayingMode.__init__(self)
        self.repeat_pattern = DefaultRepeat()
        self.name = "DefaultMode " + str(self.source)
        self.content_provider = RandomFileProvider()
        self.priority = 1


    def next(self):
        return None
