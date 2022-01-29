from ursina import *
from ursina.prefabs.first_person_controller import *
game=Ursina()
player=FirstPersonController()
player.position=(10,0,10)
Audio("Racecar.wav",loop=True)
player.speed=20
player.gravity=0
def Winner():
    Text('You win!',background=True)
    player.speed=0
ground=Entity(model='plane',texture='Road1sP',collider='box',scale=(100,1,100),position=(5, 1, 2))
Block1=Entity(model='cube',color=color.red,collider='box',scale=(20,7,20),position=(27.3, 0, -3))
Block2=Entity(model='cube',color=color.red,collider='box',scale=(10,7,20),position=(25, 0, -20.3357))
Block3=Entity(model='cube',color=color.red,collider='box',scale=(22.5,7,3),position=(16.0388, 0, 14.8465))
Block3.rotation_y=90
Block4=Entity(model='cube',color=color.red,collider='box',scale=(8,7,1),position=(15, 0, 28))
Block4.rotation_y=90
Block5=Entity(model='cube',color=color.red,collider='box',scale=(38,7,1),position=(-3, 0, 32))
Block6=Entity(model='cube',color=color.red,collider='box',scale=(8,7,40),position=(-26, 0, 14))
Block7=Entity(model='cube',color=color.blue,collider='box',scale=(20,7,60),position=(-5,0,-20))
wall1=Entity(model='cube',collider='box',scale=(100,10,5),position=(0,5,50),color=color.gray)
wall2=duplicate(wall1,z=-50)
wall3=duplicate(wall1,rotation_y=90,x=-50,z=0)
wall4=duplicate(wall3,x=50)
goal=Entity(model='cube',collider='box',scale=(11,5,1),color=color.white,position=(10,0,11))
z=Entity(model='cube',collider='box',scale=(1,5,1),color=color.white,position=(4,0,10))
k=Entity(model='cube',collider='box',scale=(11,5,1),color=color.white,position=(10,0,12), on_click=Winner)
game.run()
