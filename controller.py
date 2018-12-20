from xmas import Xmas
from acceso import Acceso
import threading
import sqlite3


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
            self._db_manager = DbManager()
            self._xmas = Xmas()
            self._acceso = Acceso(True)

    def __init_thread(self, encoding, music, is_vixen):
        if is_vixen:
            self._t1 = threading.Thread(target=self._xmas.play_from_vixen, args=(encoding, music))
        else:
            self._t1 = threading.Thread(target=self._xmas.play, args=(encoding, music))

    def play(self, music, is_vixen):
        if self._t1.isAlive():
            raise ValueError("A song is already playing")
        else:
            file_audio = self._db_manager.get_music_file(music)
            file_encoding = self._db_manager.get_encoding_file(music)
            self.__init_thread(file_encoding, file_audio, is_vixen)
            self._t1.start()

    def stop(self):
        self._xmas.stop_music()

    def turn_on(self):
        if self._t1.isAlive():
            raise ValueError("Thread already started")
        else:
            self._t1 = threading.Thread(target=self._acceso.on)
            self._t1.start()

    def turn_off(self):
        self._acceso.off()

    def get_song_list(self):
        return self._db_manager.get_song_list()


class DbManager:

    def __init__(self):
        self.encoding_query = "SELECT ENCODING_FILE FROM songs WHERE NAME=?"
        self.audio_query = "SELECT FILE_AUDIO FROM songs WHERE NAME=?"
        self.song_list_query = "SELECT NAME FROM songs"

    def get_song_list(self):
        conn = sqlite3.connect('config/songs.db')
        c = conn.cursor()
        c.execute(self.song_list_query)
        query_result = c.fetchall()
        song_names = list()
        for name in query_result:
            song_names.append(name)
        return song_names

    def get_music_file(self, song_name):
        conn = sqlite3.connect('config/songs.db')
        c = conn.cursor()
        c.execute(self.audio_query, song_name)
        file_audio = c.fetchall()
        # TODO add check on the number of file_audio elements
        return file_audio.pop(0)[0]

    def get_encoding_file(self, song_name):
        conn = sqlite3.connect('config/songs.db')
        c = conn.cursor()
        c.execute(self.encoding_query, song_name)
        encoding_file = c.fetchall()
        # TODO add check on the number of file_audio elements
        return encoding_file.pop(0)[0]
