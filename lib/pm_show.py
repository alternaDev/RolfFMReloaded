from playing_mode import PlayingMode
from random_file_provider import RandomFileProvider
import Queue

class ShowMode(PlayingMode):

    def __init__(self, name, source, rp):
        PlayingMode.__init__(self, name)
        self.repeat_pattern = rp
        self.name = "ShowMode " + str(name)
        self.priority = 1
        self.queue = Queue.Queue()
        self.content_provider = RandomFileProvider(False, source)

    def add_random(self):
        self.queue.put(self.content_provider.next())

    def add_random_from(self, source):
        temp_provider = RandomFileProvider(False, source)
        self.queue.put(temp_provider.next())

    def add_specific(self, path):
        self.queue.put(path)

    def on_stop(self):
        if self.queue.empty():
            self.priority = 10000
        else:
            self.priority = -1

    def next(self):
        if not self.queue.empty():
            return self.queue.get()
