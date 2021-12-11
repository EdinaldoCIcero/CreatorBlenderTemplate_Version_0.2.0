from bge import logic,events , types
from mathutils import Vector
import bge
from random import randint
from scripts.topdown.mecanics import MecanicsGame

import json
from scripts.topdown.JSON import JsonClass

jsn_class  = JsonClass()

tc         = logic.keyboard.events
scene      = logic.getCurrentScene()
link_datas = "C:/Users/Edinaldo Cicero/Documents/GitHub/GitHub-Game-2021/blend/scripts/topdown/json/bugs_data"

class RobotsIA(types.KX_GameObject):
    def __init__(self, own ):
        self.GDict = bge.logic.globalDict
        self.GDict["BUG_TYPE"] = ""

        #self.GDict["GAME_SCENE_ACTUAL"] = "Level_1"
        #self.scene_suspend     = self.GDict["GAME_SCENE_ACTUAL"]

        self.list_points_eixos = [point for point in self.children if "point_bot" in point]
        self.list_points_eixos.reverse()
        print( self.list_points_eixos )

        self.esqueleto         = [esq for esq in self.children if "esqueleto" in esq][0]
 
        self.AddLaser          = [laser for laser in self.esqueleto.children if "AddLaser" in laser][0]

        self.nave_meshe        = [ mesh for mesh in scene.objects if "NaveMeshe" in mesh ][0]

        #self.mecs              = MecanicsGame()
        self.list_object       = []
        

        self.bug_datas         = jsn_class.json_read( name_file= link_datas)

#-----------------------------------------------------------------------------------------
    def append_objetct_manipulation(self , object ):
        self.list_object.append( object )
        pass    

    def timer_bugs(self , values_end):
            
        if self["timer"] >= values_end:
            self["timer"] = 0.000
            self["type_efect"] = "" 
            self["trava_2_patrulha"] = True
            print(self["timer"])
           


        pass

    def follow_player( self , cont ,sen, act, so, track,path_steering ):

        cont.activate(track)
        track.object = "player_colision"

        cont.activate(path_steering)
        path_steering.navmesh = self.nave_meshe
        self.esqueleto.playAction("Robo_walk_1" , 10 , 29 , blendin=6)
        self.applyMovement([ 0, self["speed_walk"] , 0 ],True)


        pass
    #-----------------------------------------------------------------------------------------
    def IApatrulha(self ,cont ,sen, act, so, daley_timer , track):
        x,y,z = 0,0,0


        if daley_timer.positive:
            self['ran'] = randint( 0 , 4)
            cont.activate(track)

        if self['ran'] == 4:
            self.esqueleto.playAction("Robo_walk_1" , 1 , 1 )

        elif self['ran'] == 0:
            self.applyMovement([ 0, self["speed_walk"]  , 0 ],True)
            track.object = self.list_points_eixos[ self['ran'] ]
            self.esqueleto.playAction("Robo_walk_1" , 10 , 29 )

        elif self['ran'] == 1:
            self.applyMovement([ 0, -self["speed_walk"] ,0 ],True)
            track.object = self.list_points_eixos[ self['ran'] ]
            self.esqueleto.playAction("Robo_walk_1" , 10 , 29 )

        elif self['ran'] == 3:
            self.applyMovement([-self["speed_walk"] ,0  ,0 ],True)
            track.object = self.list_points_eixos[ self['ran'] ]
            self.esqueleto.playAction("Robo_walk_1" , 10 , 29 )

        elif self['ran'] == 2:
            self.applyMovement([ self["speed_walk"] ,0  ,0 ],True)
            track.object = self.list_points_eixos[ self['ran'] ]
            self.esqueleto.playAction("Robo_walk_1" , 10 , 29 )

        pass

    #-----------------------------------------------------------------------------------
    def bugs_func(self,cont ,sen, act , so , track , path_steering):
        #------------------------------------------------------
        x,y,z = 0,0,0
        comt = 0

        #--
        if self["type_efect"] == self.bug_datas["bug_turn_on"][0]:
            self["trava_2_patrulha"] = False
            self.esqueleto.playAction("Robo_shotdown", 1 ,1 , blendin=6 )
            self.timer_bugs(values_end = 4.000)
            cont.deactivate(track)

        #==
        if self["type_efect"] == self.bug_datas["laser_shooter"][0]:
            #self.esqueleto.playAction("Robo_walk_1" , 10 , 29 , blendin=6)

            self["trava_vision"]     = True
            self["trava_2_patrulha"] = False

            if self["VIDA_ROBOT"] == 0:
                self.state = 2

          

        #==
        #if self["type_efect"] == self.bug_datas["bug_shotdown"][0]  :
         #   self.esqueleto.playAction("Robo_shotdown", 1 ,1 , blendin=6)
         #   self.timer_bugs(values_end = 8.000 )
         #   self["trava_2_patrulha"] = False
         #   cont.deactivate(track)

          #  pass


        #==
        #if self["type_efect"] == self.bug_datas["bug_dance"][0] :
        #    self.esqueleto.playAction("Robo_dance" , 10 ,39 , blendin=6)
        #    self.timer_bugs(values_end = 13.000 )  
        #    self["trava_2_patrulha"] = False
        #   cont.deactivate(track)


        #==
        #if self["type_efect"] == self.bug_datas["bug_short_circuit"][0]:
        #    self.state = 2
 
            pass


    #-----------------------------------------------------------------------------------
    def main(self ,cont ,sen, act , so, daley_timer , track ,trackto_2, vision , 
             game_over, supend_game ,daley_game_over, path_steering):
        #---------------------------------------------------------
        x,y,z  = 0,0,0
        scene  = logic.getCurrentScene()
        player = scene.objects["player_colision"]


        self.bugs_func( cont ,sen, act, so, track , path_steering )


        if self["trava_2_patrulha"] == True and self["trava_vision"] == False:
            self.IApatrulha( cont ,sen, act, so, daley_timer, track )

        else:
            if vision.positive:
                self["trava_vision"] = True 



        if self["trava_vision"] == True:
            if self.getDistanceTo(player) >= 6.00:
                self.esqueleto.playAction("Robo_walk_1" , 10 , 29 )
                self.follow_player(cont ,sen, act, so, track, path_steering )

            else:
                self.esqueleto.playAction("Robo_shooter" , 10 ,10 , blendin=3)
                if daley_game_over.positive and self["trava_2_patrulha"] == False:
                    scene.addObject("LaserRobots" , self.AddLaser , 80 )





                 #   # cont.activate(game_over) 
                  #  # cont.activate(supend_game)
                    # supend_game.scene = self.GDict["GAME_SCENE_ACTUAL"] #self.scene_suspend
            #cont.deactivate(trackto_2)  self["trava_vision"]
         #if vision.positive:
            #self["trava_vision"] = True

            #self.esqueleto.playAction("Robo_shooter" , 9 , 9 )
           #     cont.activate(track)
            #    track.object      = vision.hitObject
             #   cont.activate(trackto_2)
              #  trackto_2.object  = vision.hitObject
               # if daley_game_over.positive:
                #    scene.addObject("LaserRobots" , self.AddLaser , 80 )
                 #   # cont.activate(game_over) 
                  #  # cont.activate(supend_game)
                    # supend_game.scene = self.GDict["GAME_SCENE_ACTUAL"] #self.scene_suspend
            #else:
             #   self.IApatrulha( cont ,sen, act, so, daley_timer, track )
              #  cont.deactivate(trackto_2)
                



   
def start(cont):
    own = cont.owner
    scene = logic.getCurrentScene()
    GDict = bge.logic.globalDict
    so  = scene.objects
    #------ SENSORS ---------
    #----- ACTUATORS -------- 
    #------ OBJECTS ---------
    #------------------------

    rob = RobotsIA(own)

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
    DelayTimeEixo   = sen["DelayTimeEixo"]
    VisaoColis      = sen["VisaoColis"]
    DelayOverGame   = sen["DelayOverGame"]    

    #-------------------
    TrackEsquelet = act["TrackEsquelet"]
    trackto_2     = act["trackto_2"]
    SceneGameOver = act["SceneGameOver"]
    SceneSuspendGAME = act["SceneSuspendGAME"]

    SteeringRobot = act["SteeringRobot"]
    
    #------------------------
    own.main(
        cont ,sen, act , so, 
        daley_timer     = DelayTimeEixo, 
        track           = TrackEsquelet,
        trackto_2       = trackto_2 ,
        vision          = VisaoColis,
        game_over       = SceneGameOver,
        supend_game     = SceneSuspendGAME,
        daley_game_over = DelayOverGame,
        path_steering   = SteeringRobot
        )


    pass

