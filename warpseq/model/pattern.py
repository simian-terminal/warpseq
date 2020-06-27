from .base import BaseObject
from classforge import Class, Field
from .scale import Scale
from .arp import Arp

FORWARD='forward'
REVERSE='reverse'

DIRECTIONS = [
    FORWARD,
    REVERSE
]

class Pattern(BaseObject):

    name = Field(required=True, nullable=False)
    slots = Field(type=list)
    length = Field(type=int, default=16)

    arp = Field(type=Arp, default=None, nullable=True)
    tempo = Field(type=int, default=None, nullable=True)
    scale = Field(type=Scale, default=None, nullable=True)

    def to_dict(self):
        result = dict(
            name = self.name,
            slots = self.slots,
            length = self.length,
            tempo = self.tempo
        )
        if self.arp:
            result['arp'] = arp.name
        else:
            result['arp'] = None
        if self.scale:
            result['scale'] = scale.name
        else:
            result['scale'] = None
        return result

    @classmethod
    def from_dict(cls, song, data):
        return Pattern(
            name = data['name'],
            slots = data['slots'],
            length = data['length'],
            arp = song.find_arp(data['arp']),
            tempo = data['tempo'],
            scale = song.find_scale(data['scale'])
        )