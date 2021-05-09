from ursina import *

stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
grass_texture = load_texture('assets/grass_block.png')


class Update():
    def __init__(self, hand, slots, player, voxels, Voxel):
        self.hand = hand
        self.slots = slots
        self.player = player
        self._voxels = voxels
        self.Voxel = Voxel
        self._block_pick = 1

    def update_function(self):
        # start_chunk must be greater than render_distance
        start_chunk = 32
        render_distance = 16
        for voxel in self._voxels:
            if self.player.x > voxel.x + render_distance:
                self._voxels.append(self.Voxel(self, position=(
                    voxel.x + start_chunk, 0, voxel.z), texture=stone_texture))
                voxel.delete()
                # self._voxels.remove(voxel)
            elif self.player.x < voxel.x - render_distance:
                self._voxels.append(self.Voxel(self, position=(
                    voxel.x - start_chunk, 0, voxel.z), texture=brick_texture))
                voxel.delete()
                # self._voxels.remove(voxel)
            elif self.player.z > voxel.z + render_distance:
                self._voxels.append(self.Voxel(self, position=(
                    voxel.x, 0, voxel.z + start_chunk), texture=dirt_texture))
                voxel.delete()
                # self._voxels.remove(voxel)
            elif self.player.z < voxel.z - render_distance:
                self._voxels.append(self.Voxel(self, position=(
                    voxel.x, 0, voxel.z - start_chunk), texture=grass_texture))
                voxel.delete()
                # self._voxels.remove(voxel)

        self.hand_position()
        self.select_block()

    def hand_position(self):
        if held_keys['left mouse'] or held_keys['right mouse']:
            self.hand.active()
        else:
            self.hand.passive()

    def select_block(self):
        if held_keys['1']:
            self._block_pick = 1
        elif held_keys['2']:
            self._block_pick = 2
        elif held_keys['3']:
            self._block_pick = 3
        elif held_keys['4']:
            self._block_pick = 4
        elif held_keys['5']:
            self._block_pick = 5
        else:
            return False
        self.activate_slot()

    def activate_slot(self):
        for slot in self.slots:
            self.slots[slot].passive()
        self.slots[self._block_pick - 1].active()

    @property
    def block_pick(self):
        return self._block_pick

    @block_pick.setter
    def block_pick(self, value):
        self._block_pick = value

    @property
    def voxels(self):
        return self._voxels

    @voxels.setter
    def voxels(self, value):
        self._voxels = value
