from bge import logic,events, types
import bge


#------------------------------
tc    = logic.keyboard.events
m     = logic.mouse.events
scene = logic.getCurrentScene()
GDict = bge.logic.globalDict
#------------------------------


class Huds(types.KX_GameObject):
    def __init__(self, own ):
        self.GDict = bge.logic.globalDict
        self.GDict["HUD_EVENT"] = "True"

        pass  

#-----------------------------------------------------------------------------------------
    def append_objetct_manipulation(self , object ):
        self.list_object.append( object )
        pass    

#-----------------------------------------------------------------------------------------
    def hud_elements_mouse_over(self, cont, sen, act, mouse_over_hud):
        tc    = logic.keyboard.events
        m     = logic.mouse.events
        #---------------------------------
        pass



#-----------------------------------------------------------------------------------------
def start(cont):
    own = cont.owner
    so  = scene.objects
    #------ SENSORS ---------
    
    #----- ACTUATORS -------- 
    
    #------ OBJECTS ---------
    
    #------------------------
    GDict["VIDA_PLAYER_FOR_BAR"] = 100
   
    hud = Huds(own)

    pass


def update(cont):
    own   = cont.owner
    GDict = bge.logic.globalDict
    scene = logic.getCurrentScene()
    tc    = logic.keyboard.events
    m     = logic.mouse.events
    sen   = cont.sensors
    act   = cont.actuators
    so    = scene.objects
    #------ SENSORS ---------
    MouseOverHud = sen["MouseOverHud"]

    #----- ACTUATORS --------
    
    #------ OBJECTS ---------

    #------------------------
    own["vida_player"] = GDict["VIDA_PLAYER_FOR_BAR"]

    #------------------------

    pass