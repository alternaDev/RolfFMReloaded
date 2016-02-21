from repeat_pattern import RepeatPattern
from content_provider import ContentProvider

import logging

logger = logging.getLogger(__name__)

class PlayingMode(object):

    def __init__(self, name, source):
        logger.info("Created mode " + name + " (Source: " + source + ").")
        self.repeat_pattern = RepeatPattern()
        self.name = name
        self.source = source
        self.priority = 10000
        self.provider = ContentProvider()

    @property
    def repeat_pattern(self):
        return self._repeat_pattern

    @property
    def priority(self):
        return self._priority

    @property
    def source(self):
        return self._source

    @property
    def name(self):
        return self._name

    @repeat_pattern.setter
    def repeat_pattern(self, val):
        self._repeat_pattern = val

    @priority.setter
    def priority(self, val):
        self._priority = val

    @source.setter
    def source(self, val):
        self._source = val

    @name.setter
    def name(self, val):
        self._name = val

    def next(self):
        logger.info("Selecting Next from " + self.name + ".")
        return None

    def invalidate(self):
        return None

    def on_play(self):
        return None

    def on_stop(self):
        return None
