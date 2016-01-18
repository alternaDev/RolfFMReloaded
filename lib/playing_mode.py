from repeat_pattern import RepeatPattern
from content_provider import ContentProvider
class PlayingMode(object):

    def __init__(self, name, source):
        self.repeat_pattern = RepeatPattern()
        self.name = name
        self.source = source
        self.priority = 10000
        self.provider = ContentProvider()

    @property
    def repeat_pattern(self):
        return self.repeat_pattern

    @property
    def priority(self):
        return self.priority

    @property
    def source(self):
        return self.source

    @property
    def name(self):
        return self.name

    def next(self):
        return None

    def invalidate(self):
        return None
