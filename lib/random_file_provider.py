from props import Properties
from content_provider import ContentProvider
import os
import random
import time

class RandomFileProvider(ContentProvider):

    def __init__(self, is_repeat_allowed, source):
        self.is_repeat_allowed = is_repeat_allowed
        self.source = source
        self.history = {}


    def recursive_files(self, dir):
        for path, _, fnames in os.walk(dir, True):
            for fname in fnames:
                if not fname.startswith(".") and fname.endswith(".mp3") or fname.endswith(".wav") or fname.endswith(".m4a"): #optimize me with properties
                    yield os.path.join(path, fname)

    def random_choice(self, iterable):
        l = list(iterable)
        pick = ""
        picked = random.randrange(len(l))
        pick = l[picked]

        while self.is_old_song(pick):
            picked = random.randrange(len(l))
            pick = l[picked]

        return pick

    def is_old_song(self, songname):

        if self.is_repeat_allowed == True:
            return False

        if songname in self.history:
            last_played = time.time() - self.history[songname]

            if(last_played < Properties.SONG_REPEAT_TIME):
                return True
            else:
                self.history[songname] = time.time();
                return False
        else:
            self.history[songname] = time.time()
            return False

    def next(self):
        return self.random_choice(self.recursive_files(self.source))
