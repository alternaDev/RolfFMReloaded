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

default_a = DefaultMode("Christian C", "W:\Chris", "W:\Speech")
default_b = DefaultMode("JHB", "W:\Chris\Cro - Easy", "W:\Speech")

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
    play_list = []  # enter all playing modes
    basic_play = []  # default mode list
    current_mode = None  # the current mode playing sound

    for mode in modes:
        if mode.priority == lowest_priority:
            play_list.append(mode)
        if isinstance(mode, DefaultMode):
            basic_play.append(mode)

    for mode in play_list:
        new_loop = False

        basic_play.sort(key=lambda x: x.playing_time, reverse=False)
        next_default = basic_play[0]
        basic_play.sort(key=lambda x: x.priority, reverse=False)
        temp_lowest_priority = basic_play[0].priority
        next_default.priority = temp_lowest_priority - 1
        for bp in basic_play:
            bp.playing_time -= next_default.playing_time
            bp.priority += 1

        while player.is_playing():

            for m in modes:
                m.invalidate()

            modes.sort(key=lambda x: x.priority, reverse=False)
            if modes[0].priority == -1 and modes[0].repeat_pattern.can_play():
                new_loop = True
                break
            if modes[0].priority < lowest_priority:
                new_loop = True
            time.sleep(0.05)

        if new_loop:
            break

        if mode.repeat_pattern.can_play():
            if current_mode is not None:
                current_mode.on_stop()
            current_mode = mode
            current_mode.on_play()
            player.play(current_mode.next())
