"""Setup of commands done in pygame to affect tkinter gui"""
from pygame import mixer

mixer.init()

OUT_VAR = 0
class MusicSetup:
    """Commands for tkinter button commands

    Returns:
        methods: pygame commands to change music functions
    """

# issues with making it with init. then realised that the constructor was only if
# i needed a preset build. after removing the init and
# moving commands to other methods it works just fine

    def change_next(self):
        """skip to next song

        Returns:
            func: figure out what song in list is being played and skip to next
        """
        global OUT_VAR
        OUT_VAR = OUT_VAR + 1
        mixer.music.load(songs[OUT_VAR])
        return mixer.music.play()

    def change_back(self):
        """go one song back

        Returns:
            func: go one back in list
        """
        global OUT_VAR
        OUT_VAR = OUT_VAR - 1
        mixer.music.load(songs[OUT_VAR])
        return mixer.music.play()

    def change_pause(self):
        """pauses the song
        """
        return mixer.music.pause()

    def change_play(self):
        """unpauses the song if paused
        """
        return mixer.music.unpause()

    def change_stop(self):
        """stops the song
        """
        return mixer.music.stop()

songs = ['sounds/Beethoven-5th.mp3',
         'sounds/1812-overture-finale.mp3',
         'sounds/Ave-maria-instrumental.mp3',
         'sounds/Chopin-etude-op-10-no-4.mp3',
         'sounds/Twinkle-twinkle-little-star-mozart.mp3']

mixer.music.set_volume(0.5)
mixer.music.load(songs[OUT_VAR])
mixer.music.play()
