from ursina import *

class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            color = color.white,
            texture = 'white_cube',
            rotation = Vec3 (45,45,45)
        )

class Test_btn(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'cube',
            texture = 'brick',
            color = color.blue,
            highlight_color = color.red,
            pressed_color = color.lime
        )

app = Ursina()

testSquare = Entity(model = 'quad', color = color.red, scale = (1, 4), position = (5, 4)) 

sans_texture = 'assets\Sans.png'

sans =  Entity(model = 'quad', texture = sans_texture)

def update():
    if held_keys['a']:
        testSquare.x -= 4 * time.dt

test_btn = Test_btn()

app.run()