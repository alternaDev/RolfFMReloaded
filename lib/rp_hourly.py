from repeat_pattern import RepeatPattern
import datetime


class HourlyRepeat(RepeatPattern):
    def __init__(self):
        self.last_play_hour = -1
        
    def can_play(self):
        if datetime.datetime.now().minute == 0:
            if self.last_play_hour != datetime.datetime.now().hour:
                self.last_play_hour = datetime.datetime.now().hour
                return True
        return False
