""""""
import pygame

pygame.init()

mixmu = pygame.mixer.music()

outVar = 0
class Setup:
    def __init__(self):
        self.go_back = self.change_back
        self.go_next = self.change_next
        self.go_stop = mixmu.stop()
        self.go_play = mixmu.unpause()
        self.go_pause = mixmu.pause()

    def change_next(self):
        global outVar
        outVar = outVar + 1
        mixmu.load(songs[outVar])
        mixmu.play()

    def change_back(self):
        global outVar
        outVar = outVar - 1
        mixmu.load(songs[outVar])
        mixmu.play()

songs = ['songs/1812-overture-finale.mp3',
         'songs/Ave-maria-instrumental.mp3',
         'songs/Beethoven-5th.mp3',
         'songs/Chopin-etude-op-10-no-4.mp3',
         'songs/Twinkle-twinkle-little-star-mozart.mp3']

mixmu.set_volume(0.7)
mixmu.load(songs[outVar])
mixmu.play()
