from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from voxel import Voxel

app = Ursina()
player = FirstPersonController()

for z in range(16):
    for x in range(16):
        voxel = Voxel(position=(x, 0, z))

app.run()
