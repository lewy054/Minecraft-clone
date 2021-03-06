from ursina import *
import update


grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
punch_sound = Audio('assets/punch_sound', loop=False, autoplay=False)


class Voxel(Button):
    def __init__(self, upd, position=(0, 0, 0), texture=grass_texture):
        self.upd = upd
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color=color.light_gray,
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                block_pick = self.upd.block_pick
                if block_pick == 1:
                    block_texture = dirt_texture
                elif block_pick == 2:
                    block_texture = brick_texture
                elif block_pick == 3:
                    block_texture = grass_texture
                elif block_pick == 4:
                    block_texture = stone_texture
                elif block_pick == 5:
                    block_texture = dirt_texture
                Voxel(self.upd, position=self.position +
                      mouse.normal, texture=block_texture)
            elif key == 'right mouse down':
                punch_sound.play()
                self.delete()

    def delete(self):
        self.upd.voxels.remove(self)
        destroy(self)
