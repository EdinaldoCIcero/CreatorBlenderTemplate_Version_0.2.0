from bge import logic,events, types
import bge

import json
from scripts.scripts_game.JSON import JsonClass

jsn_class  = JsonClass()
#jpositions = jsn_class.json_read( name_file="jsons/Colors")


scene = logic.getCurrentScene()
GDict = bge.logic.globalDict

class MecanicsGame():
    def __init__(self):
        self.GDict       = bge.logic.globalDict
        self.GDict["VALEU_POSITION_X"] = 0

        #----------------------------------------
        self.GRID_SIZEx , self.GRID_SIZEy = 2,2
        self.speed = 0.005

#-----------------------------------------------------------------------------------
    def set_navemesh_path(self , cont , sen , act , so , object, steering_path, target_obj ,navmesh_obj , distance_to_object ,armture_player, distance_value , speed ):
        #--------------------------------
        m     = logic.mouse.events
        x,y,z = 0 , object["speed"] ,0
        #-----------------------------------

        if object.getDistanceTo(distance_to_object) >= distance_value:
            cont.activate(steering_path)
            #steering_path.target  = target_obj
            steering_path.navmesh = navmesh_obj

            object["speed"] = speed
            armture_player.playAction("Player_walks", 10 , 25 , blendin=3)
            object.applyMovement([x,y,z],True)

        else:
            armture_player.playAction("Player_idle",  10 , 10 , blendin=4)
            cont.deactivate(steering_path)
            object["speed"] = 0

        pass

#-----------------------------------------------------------------------------------
    def set_position_object_distance(self ,cont , sen , act ,so, 
        object , track_To ,distance_to_object , distance_value , speed , select_area , armture_player):
        #--------------------------------
        m     = logic.mouse.events
        x,y,z = 0 , object["speed"] ,0
        #-----------------------------------

        #if m[events.RIGHTMOUSE]:
           # cont.activate(track_To)
            #track_To.object = select_area 
        #else:
        #if m[events.LEFTMOUSE] in [1,1]: #and not m[events.RIGHTMOUSE]:
           #  distance_to_object.worldPosition.x = 
            #point_mouse.worldPosition.y = SelectArea.worldPosition.y 


        if object.getDistanceTo(distance_to_object) >= distance_value:
            cont.activate(track_To)
            track_To.object = distance_to_object
            object["speed"] = 0.100
            armture_player.playAction("Player_walks",10 , 25 , blendin=3)
            object.applyMovement([x,y,z],True)

        else:
            armture_player.playAction("Player_idle",10 , 10 , blendin=4)
            cont.deactivate(track_To)
            object["speed"] = 0


        pass


    #-----------------------------------------------------------------------------------
    def DrawGrid(self):
        cor = [255,0,0,1]

        line_x  = 0
        line_y  = 0

        start        = 2
        quant        = 10 

        for i in range(start , quant ):
            line_y += 2 
            line_1  = scene.addObject("Linha_1" )
            
            line_1.worldPosition.x = -quant
            line_1.localScale.x    =  quant
            
            line_1.worldPosition.y = line_y -quant + 1


        for i in range(start , quant ):
            line_x += 2
            line_2  = scene.addObject("Linha_2" )
            
            line_2.worldPosition.y = -quant
            line_2.localScale.y    =  quant
            line_2.worldPosition.x = line_x -quant +1

    #---------------------------------------------------------------------------------
    def snapToGridX(self,x):
        return x // self.GRID_SIZEx * self.GRID_SIZEx
        pass

    #---------------------------------------------------------------------------------
    def snapToGridY(self,y):
        return y // self.GRID_SIZEy * self.GRID_SIZEy
        pass

    #---------------------------------------------------------------------------------
    def ObjectMousePositionConstantXY(self , cont ,sen, act,so, mouse_over_near , object):

        if mouse_over_near.positive:
           # object.worldPosition.x = self.snapToGridX( x=mouse_over_near.hitPosition.x +1 )  
            #object.worldPosition.y = self.snapToGridY( y=mouse_over_near.hitPosition.y +1 )
            
            object.worldPosition.x = mouse_over_near.hitPosition.x
            object.worldPosition.y = mouse_over_near.hitPosition.y
            pass

    #-----------------------------------------------------------------------------------
    def paradoxo( self , cont , own , sen , act ,so  , near):
        tc    = logic.keyboard.events
        m     = logic.mouse.events
        scene = logic.getCurrentScene()
        #-------------------------------
        e     = sen["e"]
        #------------------------------
        PoontoAzul  = so["PoontoAzul"]
        addPoint    = so["add_point_person_2"]
        #-------------------------------
        if e.positive:
            own.worldPosition  = PoontoAzul.worldPosition
            person2            = scene.addObject("copia_player_colision"  , addPoint )
            pass

    #-----------------------------------------------------------------------------------
    def sistem_robots_editor(self , cont , own ,sen , act ,so , point_info_bug ,mouse_over ,resume_game ,remove_editor ):
        m     = logic.mouse.events
        tc    = logic.keyboard.events
        scene = logic.getCurrentScene()
        #--------------------------------
        #----------------------------

        if mouse_over.positive:
            point_info_bug.worldPosition = mouse_over.hitObject.worldPosition
            if m[events.LEFTMOUSE] in [1,1]:
                self.GDict["BUG_TYPE"] = mouse_over.hitObject["type_logic"] 
                cont.activate(remove_editor)
                cont.activate(resume_game)
                resume_game.scene = str(self.GDict["GAME_SCENE_ACTUAL"])
        else:
            point_info_bug.worldPosition = [ 0 ,40, 0 ]

        pass
