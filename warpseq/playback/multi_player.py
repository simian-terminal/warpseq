# TODO?

from .. model.base import BaseObject
from classforge import Field
from . player import TIME_INTERVAL
import time

# FIXME: any higher level code that allows renaming of a clip will have to call remove_clip and then add_clip
# or this implementation will get confused when trying to stop that clip.

class MultiPlayer(BaseObject):

    # input
    song = Field()
    engine_class = Field()
    sleep_enabled = Field(type=bool, default=True)

    # state
    clips = Field(type=list)
    players = Field(type=dict)

    def on_init(self):
        self.clips = []
        self.players = {}


    #def start(self, milliseconds=TIME_INTERVAL):
    #    for (n, p) in self.players.items():
    #        p.start()
    #        p.advance(milliseconds=milliseconds)

    def stop(self):
        for (n, p) in self.players.items():
            p.stop()

            assert p.queue_size() == 0

    def advance(self, milliseconds=TIME_INTERVAL):
        for (n, p) in self.players.items():
            p.advance(milliseconds=milliseconds)

        if self.sleep_enabled:
            time.sleep(milliseconds / 1000.0)

    def add_clip(self, clip):

        # starts a clip playing, including stopping any already on the same track

        assert clip.track is not None

        need_to_stop = [ c for c in self.clips if clip.track.obj_id == c.track.obj_id ]
        for c in need_to_stop:
            self.remove_clip(c)

        matched = [ c for c in self.clips if c.name == clip.name ]
        if not len(matched):
            self.clips.append(clip)

            player = clip.get_player(self.song, self.engine_class)
            self.players[clip.name] = player

            player.start()

    def remove_clip(self, clip):

        # stops a playing clip

        player = self.players[clip.name]
        player.stop()
        del self.players[clip.name]

        self.clips = [ c for c in self.clips if c.name != clip.name ]

