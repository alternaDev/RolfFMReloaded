class PlayingMode(object):

    def __init__(self, name, source):
        self.repeat_pattern = RepeatPattern()
        self.name = name
        self.source = source

    @property
    def repeat_pattern(self):
        return self.repeat_pattern

    @property
    def source(self):
        return self.source

    @property
    def name(self):
        return self.name

    def next(self):
        return None
