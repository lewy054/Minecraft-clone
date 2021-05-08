from voxel import Voxel
from ursina import *



class Slot(Entity):
    def __init__(self, x, txt, clr=color.white):
        super().__init__(
            parent=camera.ui,
            model='cube',
            texture=txt,
            color=clr,
            position=Vec2(x, -0.47),
            scale=0.07
        )

    def active(self):
        self.color = color.red

    def passive(self):
        self.color = color.white
