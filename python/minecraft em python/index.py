from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController as FPC

app = Ursina()

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture  = load_texture('assets/dirt_block.png')
sky_texture   = load_texture('assets/skybox.png')
arm_texture   = load_texture('assets/arm_texture.png')
punch_sound   = Audio('assets/punch_sound',loop = False, autoplay = False)
block_pick = 1

def update():
    global  block_pick

    if held_keys['right mouse'] or held_keys['left mouse']:
        hand.active()
    else:
        hand.passive()

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4


class Voxel(Button):# 1°
    def __init__(self, position=(0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene, # 2°
            position =  position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.lime,
            scale = 0.5
        )
    # 3°
    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                if block_pick == 1: voxel = Voxel(position= self.position + mouse.normal, texture= grass_texture)
                if block_pick == 2: voxel = Voxel(position= self.position + mouse.normal, texture= stone_texture)
                if block_pick == 3: voxel = Voxel(position= self.position + mouse.normal, texture= brick_texture)
                if block_pick == 4: voxel = Voxel(position= self.position + mouse.normal, texture= dirt_texture)
        
            if key == 'left mouse down':
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            paret = scene,
            model = 'sphere',
            texture = sky_texture,
            double_sided = True,
            scale = 150
        )
class Hand(Entity):
    def __init__(self):
        super().__init__(
			parent = camera.ui,
			model = 'assets/arm',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.6))
    def active(self):
        self.position = Vec2(0.3,-0.5)    
    def passive(self):
        self.position = Vec2(0.4,-0.6)

for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x,0,z))

player = FPC()
sky = Sky()
hand = Hand()

app.run()

# Glossario
# 1° Voxel é exatamente tudo no Mine, ou seja, quando criamos a classe voxel e colocamos um botão como argumento é por que queremos criar um voxel (bloco) a cada clique de um botão.
# 2° Coloca o bloco no jogo em si, e não o bloco é o jogo. Se esquecer o que é, testa retirar está linha.
# 3° Criamos a Fç imput e chamamos o método FPC - First person controller - e com isso, passamos key == 'right mouse down' como condição para caso eu clique no Btn direito do mouse ele crie um novo voxel na direção da superficie em que meu mouse esta apontando - self.position + mouse.normal.

