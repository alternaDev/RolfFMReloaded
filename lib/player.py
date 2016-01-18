import subprocess

class Player(object):

    def __init__(self, path):
        self.DEVNULL = open(os.devnull, 'wb')
        self.current_playback_process = None

    def play(self):
        self.current_playback_process = subprocess.Popen(["play", path], stdout=DEVNULL, stderr=DEVNULL)

    def is_playing(self):
        if self.current_playback_process.poll() == None:
            return True
        else:
            return False
