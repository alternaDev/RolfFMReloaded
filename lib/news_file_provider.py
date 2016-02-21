from content_provider import ContentProvider
from random_file_provider import RandomFileProvider
from datetime import datetime
import os


class NewsFileProvider(ContentProvider):
    def __init__(self, source):
        self.source = source

    def _get_filename(self, path):
        if os.path.isfile(path + ".mp3"):
            return path + ".mp3"
        if os.path.isfile(path + ".wav"):
            return path + ".wav"
        return None

    def _is_folder_empty(self, path):
        return os.listdir(path) == []

    def next(self):
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        weekday = datetime.now().weekday()

        folder = self.source + "/" + str(year)+ "-" + str(month) + "-" + str(day) + "/"

        if self._is_folder_empty(folder):
            folder = self.source + "/" + str(year) + "-" + str(month) + "/"

        if self._is_folder_empty(folder):
            folder = self.source + "/" + weekday

        if self._is_folder_empty(folder):
            folder = self.source + "/yolo/"

        provider = RandomFileProvider(True, folder)
        return provider.next()

