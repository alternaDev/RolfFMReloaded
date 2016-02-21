import logging
import logging.config

logger = logging.getLogger(__name__)

logging.config.fileConfig('logging.ini', disable_existing_loggers=False)

from lib.pm_default import DefaultMode
from lib.player import Player
import time

logger.info("RolfFM is starting.")

# PRIORITIES
#  -1: interrupts current playing mode and clears the current playlist
#   0: clears the current playlist after the current played element has finished and then plays
#   1: default played, queued in a playlist with other priority 1 modes
# >=2: never played as long as there are lower priorities, otherwise same procedure as 1

# The different playing modes
modes = []

default_a = DefaultMode("Christian C", "C:\Users\Jan-Henrik\Music\Massive Attack")
default_b = DefaultMode("JHB", "C:\Users\Jan-Henrik\Music\The Black Keys")

modes.append(default_a)
modes.append(default_b)

# the player
player = Player()

logger.info("Entering Main-Loop")

# main loop
while True:
    for mode in modes:
        mode.invalidate() # give them the chance to update priority
    modes.sort(key=lambda x: x.priority, reverse=False)

    lowest_priority = modes[0].priority
    play_list = [] # enter all playing modes

    for mode in modes:
        if mode.priority == lowest_priority:
            play_list.append(mode)

    for mode in play_list:
        new_loop = False

        while player.is_playing():

            for mode in modes:
                mode.invalidate()
            modes.sort(key=lambda x: x.priority, reverse=False)
            if modes[0].priority == -1 and modes[0].repeat_pattern.can_play():
                new_loop = True
                break
            if modes[0].priority < lowest_priority :
                new_loop = True
            time.sleep(0.05)

        if new_loop:
            break

        if mode.repeat_pattern.can_play():
            player.play(mode.next())
