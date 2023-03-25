from ursina import *
import time

app = Ursina()

from ursina.prefabs.platformer_controller_2d import PlatformerController2d
player = PlatformerController2d(y=1, z=.01, scale_y=1, max_jumps=2)

ground = Entity(model='quad', scale_x=50, collider='box', color=color.black, y = -8)

camera.add_script(SmoothFollow(target=player, offset=[0,1,-30], speed=4))



camera.orthographic = True
camera.fov = 16

app.run()
