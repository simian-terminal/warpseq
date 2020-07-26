from .base import ReferenceObject
from classforge import Class, Field
from .scale import Scale
from .transform import Transform

FORWARD='forward'
REVERSE='reverse'

DIRECTIONS = [
    FORWARD,
    REVERSE
]

class Pattern(ReferenceObject):

    name = Field(required=True, nullable=False)
    slots = Field(type=list, required=True, nullable=False)
    length = Field(type=int, default=None, nullable=True)
    octave_shift = Field(type=int, default=0, nullable=False)

    tempo = Field(type=int, default=None, nullable=True)
    scale = Field(type=Scale, default=None, nullable=True)

    def on_init(self):
        super().on_init()

    def to_dict(self):
        result = dict(
            obj_id = self.obj_id,
            name = self.name,
            slots = self.slots,
            length = self.length,
            tempo = self.tempo,
            octave_shift = self.octave_shift,
        )
        if self.scale:
            result['scale'] = self.obj_id
        else:
            result['scale'] = None
        return result

    @classmethod
    def from_dict(cls, song, data):
        return Pattern(
            obj_id = data['obj_id'],
            name = data['name'],
            slots = data['slots'],
            length = data['length'],
            tempo = data['tempo'],
            octave_shift = data['octave_shift'],
            scale = song.find_scale(data['scale'])
        )