from bge import logic,events, types
from mathutils import Vector
import bge



import json
from scripts.scripts_game.JSON import JsonClass 


from scripts.Components.characterComponent import CharacterComponent


jsn_class  = JsonClass()
#jpositions = jsn_class.json_read( name_file="jsons/Colors")



tc    = logic.keyboard.events
m     = logic.mouse.events
scene = logic.getCurrentScene()



def start(cont):
    own = cont.owner
    so  = scene.objects
    #------ SENSORS ---------
    #----- ACTUATORS -------- 
    #------ OBJECTS ---------
    #------------------------

    armt = [obj for obj in own.children if "armature" in obj][0]


    obj  = CharacterComponent(own , char_armature=True , getArmature=armt)
    obj.setVisible(False)
    

    obj.addProps(name_prop  = "vida", 
                 value_prop = 100
                 )


def update(cont):
    own   = cont.owner
    own   = cont.owner
    scene = logic.getCurrentScene()
    tc    = logic.keyboard.events
    m     = logic.mouse.events
    sen   = cont.sensors
    act   = cont.actuators
    so    = scene.objects
    #------ SENSORS ---------

    #----- ACTUATORS --------

    #------ OBJECTS ---------
    

    #------------------------
    prop    = own.getProps()
  

    own.charMove(speed     = own["spedd"],
                keyboard   = tc )
    own.charDirection()
    own.charJump(keyboard = tc)


    