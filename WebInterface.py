import time

from flask import Flask
from aaa import Prova
import threading

app = Flask(__name__)

stri = 's'
x = Prova('music')
t1 = threading.Thread(target=x.start_music)


@app.route('/')
def hello_world():
    return '<a href="/aaa">start</a>'


@app.route('/<username>')
def test(username):
    return "Ciao %s" % username


@app.route('/aaa')
def aaa():
    global x
    global t1
    if t1.isAlive():
        print(t1.isAlive())
        return '<h1>music has already started</h1><br><a href="/bbb">stop</a>'
    else:
        thread_init()
        t1.start()
        return '<h1>starting music</h1><br><a href="/bbb">stop</a>'


@app.route('/bbb')
def m_stop():
    global x
    x.stop_music()
    time.sleep(2)
    print(t1.isAlive())
    return '<a href="/aaa">start</a>'

# @app.route('/bbb')
# def bbb():
#     x = Prova('Luca')
#     t1 = threading.Thread(target=x.moo)
#     t1.start()
#     time.sleep(2)
#     print('---------------' + x.val)
#     x.set_stringa('NINNI')
#     print('---------------' + x.val)
#     return 'moo'


def thread_init():
    global t1
    t1 = threading.Thread(target=x.start_music)


if __name__ == '__main__':
    app.run(debug=True)
