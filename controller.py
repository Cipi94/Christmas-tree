from xmas import Xmas
from acceso import Acceso
import threading


class Controller:
    _instance = None

    @staticmethod
    def getInstance():
        if Controller._instance is None:
            Controller()
        return Controller._instance

    def __init__(self):
        if Controller._instance is not None:
            raise Exception("This is a singleton class! Use get getInstance")
        else:
            Controller._instance = self
            self._t1 = threading.Thread()
            self._xmas = Xmas()
            self._acceso = Acceso(True)

    def __init_thread(self, music, is_vixen):
        if is_vixen:
            self._t1 = threading.Thread(target=self._xmas.play_from_vixen, args=music)
        else:
            self._t1 = threading.Thread(target=self._xmas.play, args=music)

    def play(self, music, is_vixen):
        if self._t1.isAlive():
            raise ValueError("A song is already playing")
        else:
            self.__init_thread(music, is_vixen)
            self._t1.start()

    def stop(self):
        self._xmas.stop_music()

    def turn_on(self):
        if self._t1.isAlive():
            raise ValueError("Thread already started")
        else:
            self._t1 = threading.Thread(target=self._acceso.on)

    def turn_off(self):
        self._acceso.off()
