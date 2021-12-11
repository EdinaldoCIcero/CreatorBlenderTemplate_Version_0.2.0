from bge import logic,events , types
from mathutils import Vector
import bge


tc    = logic.keyboard.events
scene = logic.getCurrentScene()
GDict = bge.logic.globalDict


class CharacterComponent(types.KX_GameObject):

    def __init__(self, object, char_armature=False , getArmature=None ):

        self.props = {
                    "char_constraints" : bge.constraints.getCharacter(self),
                    "armature"         : getArmature,
                    "char_armature_tr" : char_armature,
                    "char_name"        : "nome_nada"
                    }

    #-----------------------------------------------------------------------------------------
    def setGlobalId(self , name_id , value_id):
        GDict[name_id] = value_id
        pass

    #-----------------------------------------------------------------------------------------
    def getGlobalId(self , name_id):
        return GDict[name_id]
        pass

    #----------------------------------------------------------------------------------------
    def addProps(self, name_prop , value_prop):
        self.props[name_prop] = value_prop
        pass

    #-----------------------------------------------------------------------------------------
    def getProps(self):
        return self.props

    #-----------------------------------------------------------------------------------------
    def setVisible(self , vis):
        self.visible = vis
        pass

    #-----------------------------------------------------------------------------------------
    def charMove(self , speed , keyboard):
        w , s = keyboard[events.WKEY], keyboard[events.SKEY]
        a , d = keyboard[events.AKEY], keyboard[events.DKEY]
        #-----------------------------#
        x,y,z = 0,0,0

        y = w - s 
        x = d - a
        
        vec = Vector([x,y,z]).normalized() * speed
        self.props["char_constraints"].walkDirection = self.worldOrientation * vec
        
    #-----------------------------------------------------------------------------------------
    def charDirection(self):
        direction = self.props["char_constraints"].walkDirection
        #-----------------------------#
        if self.props["char_armature_tr"] == True:
            if direction.length != 0:
                self.props["armature"].alignAxisToVect(direction, 1,0.5)
                self.props["armature"].alignAxisToVect([0,0,1], 2, 1)
        else:
            print("Not armature")

    #-----------------------------------------------------------------------------------------
    def charJump(self , keyboard):
        space = keyboard[events.SPACEKEY]
        #-----------------------------#
        if space in [1,1]:
            self.props["char_constraints"].jump()
            
