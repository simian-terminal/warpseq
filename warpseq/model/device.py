# ------------------------------------------------------------------
# Warp Sequencer
# (C) 2020 Michael DeHaan <michael@michaeldehaan.net> & contributors
# Apache2 Licensed
# ------------------------------------------------------------------

from .base import ReferenceObject
from classforge import Class, Field

class Device(ReferenceObject):

    name = Field(type=str, required=True)

    def to_dict(self):
        return dict(
            obj_id = self.obj_id,
            name = self.name
        )

    @classmethod
    def from_dict(cls, song, data):
        return Device(
            obj_id = data['obj_id'],
            name = data['name']
        )