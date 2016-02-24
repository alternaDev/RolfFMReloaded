import cherrypy

from logger import logger
from lib.pm_default import DefaultMode
from lib.player import Player
import time
import json
import importlib
import argparse

logger.info("RolfFM is starting.")

parser = argparse.ArgumentParser(description="RolfFM Music Playback Service")
parser.add_argument("-c", "--config", help="Path to config file (default 'default_config.json')")

args = parser.parse_args()

def class_for_name(module_name, class_name):
    # load the module, will raise ImportError if module cannot be loaded
    m = importlib.import_module(module_name)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, class_name)
    return c

# PRIORITIES
#  -1: interrupts current playing mode and clears the current playlist
#   0: clears the current playlist after the current played element has finished and then plays
#   1: default played, queued in a playlist with other priority 1 modes
# >=2: never played as long as there are lower priorities, otherwise same procedure as 1

# The different playing modes
modes = []

configPath = 'default_config.json'
if args.config:
    configPath = args.config

with open(configPath) as configFile:
    config = json.load(configFile)

for mode in config:
    clazz = class_for_name('lib.pm_' + mode['type'], mode['type'].title() + "Mode")
    m = clazz(mode)
    modes.append(m)

for mode in modes:
    clazz = mode.web()
    if clazz is not None:
        cherrypy.tree.mount(clazz(), '/modes/' + mode.name)

class BasicWeb(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        names = []
        for mode in modes:
            names.append(mode.name)

        return {
            'modes': names,
            'currentSong': {}
        }

cherrypy.tree.mount(BasicWeb(), '/info')

cherrypy.engine.start()


# the player
player = Player()

logger.info("Entering Main-Loop")

# main loop
while True:
    for mode in modes:
        mode.invalidate() # give them the chance to update priority
    modes.sort(key=lambda x: x.priority, reverse=False)

    play_list = []  # enter all playing modes
    current_mode = None  # the current mode playing sound

    for mode in modes:
        play_list.append(mode)

    for mode in play_list:
        new_loop = False

        while player.is_playing():
            for m in modes:
                m.invalidate()

            modes.sort(key=lambda x: x.priority, reverse=False)
            if modes[0].priority == -1 and modes[0].repeat_pattern.can_play():
                new_loop = True
                break

            time.sleep(0.05)

        if new_loop:
            if current_mode is not None:
                current_mode.on_stop()
            player.stop()
            break

        if mode.repeat_pattern.can_play():
            if current_mode is not None:
                current_mode.on_stop()
            current_mode = mode
            current_mode.on_play()
            player.play(current_mode.next())
