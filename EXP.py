import io
import time

import pyglet
from gtts import gTTS

pyglet.options["audio"] = ("pulse",)

def speak(words: str, lang: str="en"):
    with io.BytesIO() as f:
        gTTS(text = words, lang=lang).write_to_fp(f)
        f.seek(0)
        
        player = pyglet.media.load('_.mp3', file=f).play()
        while player.playing:
            pyglet.app.platform_event_loop.dispatch_posted_events()
            pyglet.clock.tick()