from time import sleep
import threading


class Player(object):

    tracks = []
    currentTrack = ''
    currentTrackNumber = 0

    def add(self, track):
        self.tracks.append(track)

    def play(self):
        self.currentTrack = self.tracks[0]
        self.currentTrackNumber = self.tracks.index(self.currentTrack)
        self.currentTrack.printName()

    def stop(self):
        self.currentTrack = ''
        self.currentTrackNumber = None
        print('Playback Stopped')

    def next(self):
        if  self.currentTrackNumber == len(self.tracks) -1:
            self.currentTrack = self.tracks[0]
            self.currentTrackNumber = self.tracks.index(self.currentTrack)
        else:
            self.currentTrack = self.tracks[self.currentTrackNumber + 1]
            self.currentTrackNumber = self.tracks.index(self.currentTrack)
        self.currentTrack.printName()

    def back(self):
        if self.currentTrackNumber == 0:
            self.currentTrack = self.tracks[len(self.tracks) -1]
            self.currentTrackNumber = self.tracks.index(self.currentTrack)
        else:
            self.currentTrack = self.tracks[self.currentTrackNumber - 1]
            self.currentTrackNumber = self.tracks.index(self.currentTrack)
        self.currentTrack.printName()

    def showPlayList(self):
        print('\nPlaylist:')
        for each in self.tracks:
            print('\t\t\tSong: %s - By: %s - Album: %s \n' % (each.title, each.artist, each.album))

    def playSelection(self, selectionNumber):
        for each in self.tracks:
            if self.tracks.index(each) == selectionNumber -1:
                self.currentTrack = each
                self.currentTrackNumber = self.tracks.index(self.currentTrack)
                each.printName()

    # def playSkip(self):
    #     self.play()
    #     sleep(3)
    #     while self.currentTrackNumber != len(self.tracks) -1:
    #         self.next()
    #         sleep(3)


    def playSkip(self, time):
        count = 0
        e = threading.Event()
        while not e.wait(time) and count < len(self.tracks):
            self.next()
            count += 1