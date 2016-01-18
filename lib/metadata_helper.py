import mutagen

class MetadataHelper(object):
    def get_length(file):
        element = mutagen.File(f)
        if element:
            return element.length
        else:
            return -1
