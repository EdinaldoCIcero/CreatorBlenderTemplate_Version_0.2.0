from bge import logic,events, types
import bge

import json
from scripts.topdown.JSON import JsonClass 


jsn_class  = JsonClass()
#jpositions = jsn_class.json_read( name_file="jsons/Colors")


scene = logic.getCurrentScene()
GDict = bge.logic.globalDict

#menuPause.py

def pauseMenu(cont):
    own            = cont.owner
    scene          = logic.getCurrentScene()
    tc  , m        = logic.keyboard.events , logic.mouse.events
    sen, act, so   = cont.sensors , cont.actuators , scene.objects

    #------ SENSORS ---------
    MouseOverAny   = sen["MouseOverAny"]
    mho            = MouseOverAny.hitObject

    #----- ACTUATORS --------
    SetScene        = act["SetScene"]
    SceneRemovPause = act["SceneRemovPause"]
    Actionreverse   = act["Actionreverse"]

    #------ OBJECTS ---------
    select_pause_buttons = so["select_pause_buttons"]
    #------------------------


    if MouseOverAny.positive:
        select_pause_buttons.worldPosition.x = MouseOverAny.hitObject.worldPosition.x
        select_pause_buttons.worldPosition.y = MouseOverAny.hitObject.worldPosition.y
        

        if m[events.LEFTMOUSE] in [1,1]:

            if mho["type"] == "voltaraojogo":

                cont.activate(Actionreverse)
                print( Actionreverse.frame )
                
                if own["frame_action"] == 0.0:
                    print("despausado")

                    cont.activate(SceneRemovPause)
                    cont.activate(SetScene)
                
        
            elif mho["type"] == "voltarmenu":
                logic.restartGame()

            elif mho['type'] == "quitgame":
                logic.endGame()

                pass

    else:
        select_pause_buttons.worldPosition = [0,-25 , 0]
