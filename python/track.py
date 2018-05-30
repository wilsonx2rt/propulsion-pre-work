class Track(object):

    def __init__(self, artist, title, album):
        self.artist = artist
        self.title = title
        self.album = album

    def printName(self):
        print('Playing %s by %s' % (self.title, self.artist))