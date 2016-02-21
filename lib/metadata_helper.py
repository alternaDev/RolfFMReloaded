import mutagen


class MetadataHelper(object):
    @staticmethod
    def get_length(f):
        element = mutagen.File(f)
        if element:
            return element.length
        else:
            return -1
