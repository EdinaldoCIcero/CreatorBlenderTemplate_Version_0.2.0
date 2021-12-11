from bge import logic,events, types
import bge

import json
from scripts.scripts_game.JSON import JsonClass
#from scripts.topdown.mecanics import MecanicsGame
from scripts.scripts_game.SaveLoad import GameSaveDatas


jsn_class  = JsonClass()
link_datas = "C:/Users/Edinaldo Cicero/Documents/GitHub/GitHub-Game-2021/blend/scripts/scripts_game/json/bugs_data"

jpositions = jsn_class.json_read( name_file=link_datas)
#mecs = MecanicsGame()


save_load = GameSaveDatas()



def start(cont):
    own   = cont.owner
    scene = logic.getCurrentScene()
    GDict = bge.logic.globalDict
    so    = scene.objects
    sen   = cont.sensors
    act   = cont.actuators
    #------ SENSORS ---------

    #----- ACTUATORS -------- 

    #------ OBJECTS ---------
    Dialogs_Text = so["Dialogs_Text"]

    #------------------------
    GDict["DIALOGS"] = ""

    #GDict["TYPPE_EVENT_GAME"]


    dialg  = save_load.LoadDataDict(
                                    name_data_file = "dialogs", 
                                    extension_file = ".dtsl")


    Dialogs_Text["Text"] = str( dialg[ str(GDict["DIALOGS"]) ] )
    




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
    

    #------ OBJECTS ---------
    Dialogs_Text = so["Dialogs_Text"]

    #------------------------

    #GDict["TYPPE_EVENT_GAME"]


    dialg  = save_load.LoadDataDict(
                                    name_data_file = "dialogs", 
                                    extension_file = ".dtsl")


    Dialogs_Text["Text"] = str( dialg[ str(GDict["DIALOGS"] ) ]["ingles"]   )
    #Dialogs_Text["Text"] = str( dialg["dialogo_1"]["ingles"]   )
    
