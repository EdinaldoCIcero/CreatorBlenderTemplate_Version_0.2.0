from bge import logic,events, types
import bge

import json
from scripts.scripts_game.JSON import JsonClass
from scripts.scripts_game.SaveLoad import GameSaveDatas


jsn_class  = JsonClass()
#jpositions = jsn_class.json_read( name_file="jsons/Colors")


save_load = GameSaveDatas()


def start(cont):
    own = cont.owner
    scene = logic.getCurrentScene()
    GDict = bge.logic.globalDict
    so  = scene.objects
    sen   = cont.sensors
    act   = cont.actuators
    #------ SENSORS ---------

    #----- ACTUATORS -------- 

    #------ OBJECTS ---------
    #------------------------
    GDict["GAME_SCENE_ACTUAL"] = scene.name

    logic.addScene("->_3_Hud")

    pass

def update(cont):
    own   = cont.owner
    scene = logic.getCurrentScene()
    GDict = bge.logic.globalDict
    tc    = logic.keyboard.events
    m     = logic.mouse.events
    sen   = cont.sensors
    act   = cont.actuators
    so    = scene.objects
    #------ SENSORS ---------

    #----- ACTUATORS -------- 
    SupendGame   = act["SupendGame"]
    

    #------ OBJECTS ---------

    #------------------------
    GDict["GAME_SCENE_ACTUAL"] = scene.name


    if tc[events.ESCKEY] in [1,1]:
        cont.activate(SupendGame)
        SupendGame.scene = GDict["GAME_SCENE_ACTUAL"]
        
        



    pass
        
