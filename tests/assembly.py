from warpseq.model.arp import Arp
from warpseq.model.clip import Clip
from warpseq.model.device import Device
from warpseq.model.instrument import Instrument
from warpseq.model.pattern import Pattern
from warpseq.model.song import Song
from warpseq.model.scale import Scale
from warpseq.model.track import Track
from warpseq.model.scene import Scene
import json

def test_assembly():

    # this tests the construction of the datastructures that the UI uses.
    # humans won't be using this directly.

    song = Song(
        name='A Song',
        devices = dict(),
        instruments = dict(),
        scales = dict(),
        tracks = [],
        scenes = [],
        arps = dict(),
        clips = dict(),
        patterns = dict()
    )

    d1 = Device(name='IAC Bus')
    d2 = Device(name='MIDI Interface')
    d3 = Device(name='Internal')
    d4 = Device(name='Junk')
    song.add_devices([ d1, d2, d3, d4 ])
    song.remove_device(d4)

    euro1 = Instrument(device=d1, name='eurorack1', channel=1, min_octave=0, base_octave=3, max_octave=8)
    euro2 = Instrument(device=d1, name='eurorack2', channel=2, min_octave=0, base_octave=3, max_octave=8)
    euro3 = Instrument(device=d1, name='eurorack3', channel=3, min_octave=0, base_octave=3, max_octave=8)
    euro4 = Instrument(device=d1, name='eurorack4', channel=4, min_octave=0, base_octave=3, max_octave=8)
    euro5 = Instrument(device=d1, name='eurorack5', channel=5, min_octave=0, base_octave=3, max_octave=8)
    euro6 = Instrument(device=d1, name='eurorack6', channel=6, min_octave=0, base_octave=3, max_octave=8)
    euro7 = Instrument(device=d1, name='eurorack7', channel=7, min_octave=0, base_octave=3, max_octave=8)
    euro8 = Instrument(device=d1, name='eurorack8', channel=8, min_octave=0, base_octave=3, max_octave=8)
    moog  = Instrument(device=d2, name='moog', channel=9, min_octave=2, base_octave=4, max_octave=8)
    kick  = Instrument(device=d3, name='kick', channel=1, min_octave=0, base_octave=3, max_octave=8)

    song.add_instruments([ euro1, euro2, euro3, euro4, euro5, euro6, euro7, euro8, moog, kick])

    foo_scale = Scale(name='foo', root='C', octave=0, slots = [ 1, 2, 3, 4, 5, 6, 7, ])
    bar_scale = Scale(name='bar', root='C', octave=0, slots = [ 1, 2, 3, 4, 5, 6, 7, ])
    baz_scale = Scale(name='baz', root='C', octave=0, slots = [ 1, 2, 3, 4, 5, 6, 7, ])

    song.add_scales([ foo_scale, bar_scale, baz_scale ])

    song.scale = foo_scale
    song.tempo = 140
    song.auto_advance = True
    song.measure_length = 16
    song.repeat = 4

    t1  = Track(name='euro1', instrument=euro1, clip_ids=[])
    t2  = Track(name='euro2', instrument=euro2, clip_ids=[])
    t3  = Track(name='euro3', instrument=euro3, clip_ids=[])
    t4  = Track(name='euro4', instrument=euro4, clip_ids=[])
    t5  = Track(name='euro5', instrument=euro5, clip_ids=[])
    t6  = Track(name='euro6', instrument=euro6, clip_ids=[])
    t7  = Track(name='euro7', instrument=euro7, clip_ids=[])
    t8  = Track(name='euro8', instrument=euro8, clip_ids=[])
    t9  = Track(name='moog',  instrument=moog, clip_ids=[])
    t10 = Track(name='kick',  instrument=kick, clip_ids=[])
    song.add_tracks([t1,t2,t3,t4,t5,t6,t7,t8,t9,t10])
    song.remove_track(t8)

    s1 = Scene(name='s1', repeat=2, clip_ids=[])
    s2 = Scene(name='s2', scale=bar_scale, clip_ids=[])
    s3 = Scene(name='s3', clip_ids=[])
    s4 = Scene(name='s4', clip_ids=[])
    s5 = Scene(name='s5', clip_ids=[])
    song.add_scenes([ s1, s2, s3, s4, s5 ])
    song.remove_scene(s5)

    # FIXME: is this the right data model here?
    a1 = Arp(name='a1', slots=["1","-1","-","0"])
    a2 = Arp(name='a2', slots=[1,0,1])
    song.add_arps([a1, a2])
    song.remove_arp(a2)

    p1 = Pattern(name='p1', slots=[1,4,5,6,2,3,8,1,4])
    p2 = Pattern(name='p2', slots=["I","IV","V","-"," ",1])
    p3 = Pattern(name='p3', slots=[1,' ',' ',' '])
    p4 = Pattern(name='p4', slots=["GRAB(1) RAND_OFF(0.5) +1", "IV" ])
    p5 = Pattern(name='p5', slots=[])
    song.add_patterns([p1,p2,p3,p4,p5])
    song.remove_pattern(p5)

    c1 = Clip(name='c1', pattern=p1, scene_ids=[], track_ids=[])
    c2 = Clip(name='c2', pattern=p1, arp=a1, repeat=None, scene_ids=[], track_ids=[])
    c3 = Clip(name='c3', pattern=p2, scale=baz_scale, scene_ids=[], track_ids=[])
    c4 = Clip(name='c4', pattern=p3, scene_ids=[], track_ids=[])
    c5 = Clip(name='c5', pattern=p3, length=4, repeat=4, scene_ids=[], track_ids=[])
    c6 = Clip(name='c6', pattern=p2, length=8, repeat=1, scene_ids=[], track_ids=[])

    song.add_clips([c1,c2,c3,c4,c5,c6])
    # FIXME: this should auto-name, possibly
    song.remove_clip(c6)

    song.assign_clip(scene=s1, track=t1, clip=c1)
    song.assign_clip(scene=s1, track=t2, clip=c2)
    song.assign_clip(scene=s2, track=t2, clip=c3)
    song.assign_clip(scene=s3, track=t3, clip=c4)
    song.assign_clip(scene=s4, track=t1, clip=c5)
    song.unassign_clip(scene=s2, track=t2, clip=c3)


    data = song.to_json()
    s2 = Song.from_json(data)
    data2 = s2.to_json()

    print(data2)

    assert data == data2

if __name__=="__main__":
    test_assembly()

