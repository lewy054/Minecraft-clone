
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from update import update_function

app = Ursina()
from sky import Sky
from hand import Hand
from voxel import Voxel

def update():
    update_function(hand)


window.fps_counter.enabled = False
player = FirstPersonController()
hand = Hand()
sky = Sky()

for z in range(16):
    for x in range(16):
        voxel = Voxel(position=(x, 0, z))

app.run()
