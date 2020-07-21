"""testst"""
import tkinter as tk
import music_setup

commands_set = music_setup.MusicSetup()

class Mp3Player:
    """Overall gui with tkinter all buttons
    """
    def __init__(self, master):
        self.master = master
        self.titles = self.title_set
        self.back_button = tk.Button(master, text="Back", command=commands_set.change_back)
        self.back_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(master, text="Pause", command=commands_set.change_pause)
        self.pause_button.pack(side=tk.LEFT)

        self.play_button = tk.Button(master, text="Play", command=commands_set.change_play)
        self.play_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(master, text="Stop", command=commands_set.change_stop)
        self.stop_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(master, text="Next", command=commands_set.change_next)
        self.next_button.pack(side=tk.LEFT)

        self.sound_scale = tk.Scale(master, from_=0, to=100)
        self.sound_scale.set(50)
        self.sound_scale.pack(side=tk.TOP)

    def title_set(self, whatiwant):
        self.master.title(whatiwant)

root = tk.Tk()
my_gui = Mp3Player(root)
root.mainloop()
