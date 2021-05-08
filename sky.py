from ursina import *

sky_texture = load_texture('assets/skybox.png')


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture
        )
