import xmas
import threading


class Controller:

    def __init__(self):
        self._t1 = threading.Thread()

    def __init_thread(self, music, is_vixen):
        if is_vixen:
            self._t1 = threading.Thread(target=xmas.play_from_vixen, args=music)
        else:
            self._t1 = threading.Thread(target=xmas.play, args=music)

    def play(self, music, is_vixen):
        if self._t1.isAlive():
            raise ValueError("A song is already playing")
        else:
            self.__init_thread(music, is_vixen)
            self._t1.start()
