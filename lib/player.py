import subprocess
import os
import logging

logger = logging.getLogger(__name__)

class Player(object):

    def __init__(self):
        self.DEVNULL = open(os.devnull, 'wb')
        self.current_playback_process = None

    def play(self, path):
        logger.info("Playing " + path + ".")
        self.current_playback_process = subprocess.Popen(["play", path], stdout=self.DEVNULL, stderr=self.DEVNULL)

    def is_playing(self):
        if not self.current_playback_process:
            return False
        if self.current_playback_process.poll() == None:
            return True
        else:
            return False
