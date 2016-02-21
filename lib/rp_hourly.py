from repeat_pattern import RepeatPattern
import datetime


class HourlyRepeat(RepeatPattern):
    def can_play(self):
        return datetime.datetime.now().minute == 0
