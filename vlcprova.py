import pyglet

music = pyglet.resource.media('test.wav')
music.play()

pyglet.app.run()