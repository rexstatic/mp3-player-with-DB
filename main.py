import tkinter as tk
import music_setup

commands_set = music_setup.MusicSetup()

class Mp3Player:
    """Overall gui with tkinter all buttons
    """
    def __init__(self, root, w, h):
        self.root = root
        self.w = w
        self.h = h
        self.width_v = 5
        self.height_v = 5

        #self.root = tk.Tk() # Main window
        self.root.title("Mp3 player")
        # self.root.iconbitmap(r'C:\Users\17_es\PycharmProjects\square_puzzle\images\icon.ico')
        
        # buttons
        self.back_button = tk.Button(root, text="Back", width=self.width_v,
                                     height=self.height_v, command=commands_set.change_back)
        self.back_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(root, text="Pause", width=self.width_v,
                                      height=self.height_v, command=commands_set.change_pause)
        self.pause_button.pack(side=tk.LEFT)

        self.play_button = tk.Button(root, text="Play", width=self.width_v,
                                     height=self.height_v, command=commands_set.change_play)
        self.play_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(root, text="Stop", width=self.width_v,
                                     height=self.height_v, command=commands_set.change_stop)
        self.stop_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(root, text="Next", width=self.width_v,
                                     height=self.height_v, command=commands_set.change_next)
        self.next_button.pack(side=tk.LEFT)

        # Scale
        self.sound_scale = tk.Scale(root, from_=0, to=100)
        self.sound_scale.set(50)
        self.sound_scale.pack(side=tk.TOP)

    commands_set.start_player()

root = tk.Tk()
main_frame = Mp3Player(root, 200, 200)
root.mainloop()

#root = tk.Tk()
#my_gui = Mp3Player(root)
#root.mainloop()\

#tk.mainloop()
