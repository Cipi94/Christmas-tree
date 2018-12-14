import time

from flask import Flask, redirect, render_template, request

# from singleton import Singleton
import threading
from controller import Controller
# from vixenexport import VixenExport

app = Flask(__name__)
# sing = Singleton().hello()
# x = Prova('music')
# t2 = threading.Thread(target=x.start_music)
#
t1 = None


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/on')
def turn_on():
    controller.getInstance()
    controller.turn_on()
    return "Tree turned on <a href='/'>home</a>"


@app.route('/off')
def turn_off():
    controller.getInstance()
    controller.turn_off()
    return "Tree turned off <a href='/'>home</a>"


@app.route('/<username>')
def test(username):
    return "Ciao %s" % username


# @app.route('/aaa')
# def aaa():
#     # global x
#     if t2.isAlive():
#         print(t2.isAlive())
#         return '<h1>music has already started</h1><br><a href="/bbb">stop</a>'
#     else:
#         thread_init(None)
#         t1.start()
#         return '<h1>starting music</h1><br><a href="/bbb">stop</a>'


# @app.route('/bbb')
# def m_stop():
#     global x
#     x.stop_music()
#     time.sleep(2)
#     print(t1.isAlive())
#     return '<a href="/aaa">start</a>'

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


@app.route('/start_music/<music>')
def start_music(music=None):
    # if music is not None:
    #     if t1 is None or t1.isAlive():
    #         return
    #     thread_init(music)
    #
    #     return redirect("/")
    #
    # return "Error"
    try:
        controller.play(music, True)
    except ValueError:
        return "music already playing or thread error"
    return redirect("/")


@app.route('/stop_music')
def stop_music():
    controller.stop()


@app.route('/action', methods=['GET', 'POST'])
def do_action():
    controller.getInstance()
    if request.method == 'GET':
        if request.args.get('cmd') == 'on':
            controller.turn_on()
            return "Tree turned on <a href='/'>home</a>"
        else:
            return "wrong get parameter"
    return "Not a GET method"


# def thread_init(music):
#     global t1
#     t1 = threading.Thread(target=x.start_music)
#    global vixenThread
#    vixenThread = threading.Thread(target=VixenExport, args=music)


# controller = Controller()

if __name__ == '__main__':
    controller = Controller()
    app.run(debug=True, host='0.0.0.0')
