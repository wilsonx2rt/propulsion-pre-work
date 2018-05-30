from player import Player
from track import Track

def run():
    # create instance of player
    player = Player()

    # create instances for the following three tracks
    track1 = Track("Incubus", "Drive", "Make Yourself")
    track2 = Track("Ritchie Valens", "La Bamba", "La Bamba")
    track3 = Track("Red Hot Chilli Peppers", "Californication", "Californication")
    track4 = Track("Carlos Santana", "Smooth", "Supernatural")

    # add tracks to player
    player.add(track1)
    player.add(track2)
    player.add(track3)
    player.add(track4)

    # # play tracks
    player.play()

    player.next()

    player.next()

    player.next()

    player.back()

    # directly select a track
    player.playSelection(2)


    # print out all tracks
    player.showPlayList()

    # play on 3 sec timer
    player.playSkip(3)


if __name__ == "__main__":
    run()
