from props import Properties

class RandomFileProvider(object):

    def __init__(self, is_repeat_allowed, source):
        self.is_repeat_allowed = is_repeat_allowed
        self.source = source
        self.history = {}


    def recursive_files(self, dir):
        for path, _, fnames in os.walk(dir, True):
            for fname in fnames:
                if not fname.startswith(".") and fname.endswith(".mp3") or fname.endswith(".wav") or fname.endswith(".m4a"): #optimize me
                    yield os.path.join(path, fname)

    def random_choice(self, iterable):
        l = list(iterable)
        pick = ""
        picked = random.randrange(len(l))
        pick = l[picked]

        while is_old_song(pick):
            picked = random.randrange(len(l))
            pick = l[picked]

        return pick

    def is_old_song(self, songname):

        if is_repeat_allowed == True:
            return False

        if songname in history:
            last_played = time.time() - history[songname]

            if(last_played < Properties.SONG_REPEAT_TIME):
                return True
            else:
                history[songname] = time.time();
                return False
        else:
            history[songname] = time.time()
            return False

    def nextSong(self):
        return random_choice(recursive_files(self.source))
