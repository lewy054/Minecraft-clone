from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()
dirt =  load_texture('assets/thumbnails/dirt_block.png')
brick = load_texture('assets/thumbnails/brick_block.png')
grass = load_texture('assets/thumbnails/grass_block.png')
stone = load_texture('assets/thumbnails/stone_block.png')
thumbnails = [dirt, brick, grass, stone, dirt]
from sky import Sky
from hand import Hand
from voxel import Voxel
from quick_bar import Slot
from update import Update

def update():
    upd.update_function()


def create_quick_bar():
    x = -0.14
    global slots
    for i, texture in enumerate(thumbnails):
        slots[i] = (Slot(x, texture))
        x += 0.07


slots = {}
voxels = []
# window.fps_counter.enabled = False
# scene.fog_density = .05
player = FirstPersonController()
hand = Hand()
sky = Sky()
create_quick_bar()
upd = Update(hand, slots, player, voxels, Voxel)
for z in range(-16, 16):
    for x in range(-16, 16):
        voxels.append(Voxel(upd, position=(x, 0, z)))

app.run()
