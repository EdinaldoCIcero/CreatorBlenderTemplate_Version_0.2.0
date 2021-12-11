from bge import logic, events, types
from mathutils import Vector
import bge


tc    = logic.keyboard.events
m     = logic.mouse.events
scene = logic.getCurrentScene()
GDict = bge.logic.globalDict


class menuComponent(types.KX_GameObject):

    def __init__(self , own ,comp_name ):

        self.props = {
                    "":""
                    }

        #self.select_buttons = scene.objects["select_buttons"]

        self.list_select   = self.get_select()
        self.empty_buttons = self.get_empty_buttons()
   

    def get_select(self):
        selects = [but for but in scene.objects if "select_buttons" in but]
        return selects

    def get_empty_buttons(self):
        empty = [empt for empt in scene.objects if "empty_buttons" in empt]
        return empty
        
    def printi(self):
        if tc[events.EKEY] in [1,1]:
            print("empty-button ->" ,self.empty_buttons )
            print("buttons ->", self.list_select )
        pass

    def mouse_over_buttons(self , mouse_over ):

        if mouse_over.positive:
            #if mouse_over.hitObject['style_type'] == "simples" :
            self.list_select[0].worldPosition.x = mouse_over.hitObject.worldPosition.x
            self.list_select[0].worldPosition.y = mouse_over.hitObject.worldPosition.y
        else:
            self.list_select[0].worldPosition = [0,-30,0]

        self.mouse_buttons(mouse_over) #action_point


    def mouse_buttons(self , mouse_over ):
        if mouse_over.positive and m[events.LEFTMOUSE] in [1,1]:

            if mouse_over.hitObject['type'] == "startgame":
                scene.replace( "game")

            if mouse_over.hitObject["type"] == "quitgame":
                logic.endGame()

                pass



