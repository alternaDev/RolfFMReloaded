import random
import subprocess
import os
import logging
import platform
import time

logger = logging.getLogger(__name__)


class Player(object):

    def __init__(self):
        self.DEVNULL = open(os.devnull, 'wb')
        self.current_playback_process = None
        self.last_playback = 0

    def play(self, path):
        logger.info("Playing " + path + ".")
        try:
            self.current_playback_process = subprocess.Popen(["omxplayer", path], stdout=self.DEVNULL, stderr=self.DEVNULL)
        except Exception as e:
            logger.error("Could not play Audio File " + path + ".")

        if platform.system() == "Windows":
            self.last_playback = time.time()

    def is_playing(self):
        if platform.system() == "Windows":
            return time.time() - self.last_playback < 20 + 10 * random.random()
        if not self.current_playback_process:
            return False
        if self.current_playback_process.poll() is None:
            return True
        else:
            return False

    def stop(self):
        if not self.current_playback_process:
            return True
        self.current_playback_process.kill()
