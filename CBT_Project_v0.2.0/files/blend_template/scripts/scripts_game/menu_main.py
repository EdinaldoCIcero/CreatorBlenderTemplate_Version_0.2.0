from bge import logic,events, types
import bge
from scripts.scripts_game.SaveLoad import GameSaveDatas

tc    = logic.keyboard.events
m     = logic.mouse.events
scene = logic.getCurrentScene()
GDict = bge.logic.globalDict


class MenuMain(types.KX_GameObject):
    def __init__(self, own ):
        self.GDict = bge.logic.globalDict

        try:
            self.selecion_buttons =  [selc for selc in scene.objects if "selecion_button" in selc ][0]
            self.list_points_menu =  [points for points in scene.objects if "points_menus" in points ]
        except:
            pass

        # 0 = Point_CredtsGame
        # 1 = Point_Pos_Menus
        # 2 = Point_Controle
        # 3 = Point_MenuMain
        
        self.save_load = GameSaveDatas()
        self.point_pos = [-24.0512, 22.9488 , -17.0477]

  
#-----------------------------------------------------------------------------------------
    def buttons_main(self,cont, sen ,act, hit_button, scene_load_game  ):
        SceneRemoveMenu = act["SceneRemoveMenu"]

        if hit_button["button_type"] == "iniciar_jogo":
            cont.activate(scene_load_game)
            cont.activate(SceneRemoveMenu)
            

        elif hit_button["button_type"] == "controlls":
            self.list_points_menu[2].worldPosition = self.list_points_menu[1].worldPosition
            self.list_points_menu[3].worldPosition.x = -100

        elif hit_button["button_type"] == "credits":
            self.list_points_menu[0].worldPosition = self.list_points_menu[1].worldPosition
            self.list_points_menu[3].worldPosition.x = -100

        elif hit_button["button_type"] == "quit":
            logic.endGame()


        #------- Buttons for Back ---------------------------- quit

        if hit_button["button_type"] == "voltar_1":
            self.list_points_menu[2].worldPosition.y = self.point_pos[1]
            self.list_points_menu[3].worldPosition.x = self.point_pos[2]
           

        if hit_button["button_type"] == "voltar_2":
            self.list_points_menu[0].worldPosition.y = self.point_pos[0]
            self.list_points_menu[3].worldPosition.x = self.point_pos[2]
            
        pass

#-----------------------------------------------------------------------------------------
    def buttons_pausa(self, cont, sen ,act, hit_button ,game_resum, V_Menu):
        scene = logic.getCurrentScene()
        Point_MenuPause = scene.objects["Point_MenuPause"]
        #---------------------------------------------------------


        if hit_button["button_type"] == "restona_jogo":
            cont.activate(game_resum)
            game_resum.scene = str(self.GDict["GAME_SCENE_ACTUAL"])
            Point_MenuPause.worldPosition.x = -24.0477

        #---------------------------------------------------------
        elif hit_button["button_type"] == "voltar_menu":
            cont.activate(V_Menu)
            pass
            
        #---------------------------------------------------------
        elif hit_button["button_type"] == "sair_jogo":
            logic.endGame()

#-----------------------------------------------------------------------------------------
    def buttons_gameover(self, cont, sen ,act, hit_button ,game_reicinar_level, V_Menu):
        scene = logic.getCurrentScene()
        Point_MenuGameOver = scene.objects["Point_MenuGameOver"]
        #---------------------------------------------------------


        if hit_button["button_type"] == "reinicar_level":
            cont.activate(game_reicinar_level)
            #game_resum.scene = str(self.GDict["GAME_SCENE_ACTUAL"])
            Point_MenuGameOver.worldPosition.x = -25.0477

        #---------------------------------------------------------
        elif hit_button["button_type"] == "voltar_menu":
            cont.activate(V_Menu)
            pass

        #---------------------------------------------------------
        elif hit_button["button_type"] == "sair_jogo":
            logic.endGame()

#-----------------------------------------------------------------------------------------
    def buttons_menu_main(self ,cont, sen ,act , mouse_over_buttons, scene_load_game ):
        m     = logic.mouse.events
        #-------------------------------------------

        if mouse_over_buttons.positive:
            self.selecion_buttons.worldPosition.x , self.selecion_buttons.worldPosition.y = mouse_over_buttons.hitObject.worldPosition.x, mouse_over_buttons.hitObject.worldPosition.y
            if m[events.LEFTMOUSE] in [1,1]:
                self.buttons_main(cont, sen ,act,
                                  hit_button      = mouse_over_buttons.hitObject , 
                                  scene_load_game = scene_load_game )
        else:
            self.selecion_buttons.worldPosition.x = -100
        pass

#-----------------------------------------------------------------------------------------
    def buttons_menu_pause(self ,cont, sen ,act , mouse_over_buttons , game_resum  , V_Menu):
        m     = logic.mouse.events
        tc    = logic.keyboard.events
        scene = logic.getCurrentScene()
        #-------------------------------------------
        Menu_Plane_Selecion_Buttons = scene.objects["Menu_Plane_Selecion_Buttons.001"]
        Point_MenuPause = scene.objects["Point_MenuPause"]
        #-------------------------------------------

        if tc[events.ESCKEY] in [1,1]:
            Point_MenuPause.worldPosition.x = -17.0477

        if mouse_over_buttons.positive:
            Menu_Plane_Selecion_Buttons.worldPosition.x , Menu_Plane_Selecion_Buttons.worldPosition.y  = mouse_over_buttons.hitObject.worldPosition.x, mouse_over_buttons.hitObject.worldPosition.y

            if m[events.LEFTMOUSE] in [1,1]:
                self.buttons_pausa(cont, sen ,act ,
                                   hit_button  = mouse_over_buttons.hitObject ,
                                   game_resum  = game_resum , 
                                   V_Menu      = V_Menu
                                   )

        else:
            Menu_Plane_Selecion_Buttons.worldPosition.x = -100

#-----------------------------------------------------------------------------------------
    def buttons_menu_gameover(self, cont, sen, act, mouse_over_buttons, game_reicinar_level, V_Menu):
        m     = logic.mouse.events
        tc    = logic.keyboard.events
        scene = logic.getCurrentScene()
        #-------------------------------------------
        Menu_Plane_Selecion_Buttons = scene.objects["Menu_Plane_Selecion_Buttons.002"]
        Point_MenuGameOver          = scene.objects["Point_MenuGameOver"]
        #-------------------------------------------

        if tc[events.ESCKEY] in [1,1]:
            Point_MenuGameOver.worldPosition.x = -0.047701

        if mouse_over_buttons.positive:
            Menu_Plane_Selecion_Buttons.worldPosition.x , Menu_Plane_Selecion_Buttons.worldPosition.y  = mouse_over_buttons.hitObject.worldPosition.x, mouse_over_buttons.hitObject.worldPosition.y

            if m[events.LEFTMOUSE] in [1,1]:
                self.buttons_gameover(cont, sen ,act ,
                                   hit_button           = mouse_over_buttons.hitObject ,
                                   game_reicinar_level  = game_reicinar_level , 
                                   V_Menu               = V_Menu
                                   )

        else:
            Menu_Plane_Selecion_Buttons.worldPosition.x = -100

#-----------------------------------------------------------------------------------------

def start(cont):
    own   = cont.owner
    scene = logic.getCurrentScene()
    so    = scene.objects
    #------ SENSORS ---------
    
    #----- ACTUATORS -------- 
    
    #------ OBJECTS ---------
    
    #------------------------

    main_menu = MenuMain(own)


    pass


def update_pause(cont):
    own   = cont.owner
    GDict = bge.logic.globalDict
    scene = logic.getCurrentScene()
    tc    = logic.keyboard.events
    m     = logic.mouse.events
    sen   = cont.sensors
    act   = cont.actuators
    so    = scene.objects
    #------ SENSORS ---------
    MouseOverButtons = sen["MouseOverButtons"]

    #----- ACTUATORS --------
    Game_resume      = act["Game_resume"]
    V_Menu           = act["V_Menu"]

    #------ OBJECTS ---------
    #Point_MenuPause  = so["Point_MenuPause"]
    
    #------------------------
    #------------------------

    own.buttons_menu_pause( cont,sen ,act,
        mouse_over_buttons = MouseOverButtons,
        game_resum         = Game_resume,
        V_Menu             = V_Menu
        )


def update_gameover(cont):
    own   = cont.owner
    GDict = bge.logic.globalDict
    scene = logic.getCurrentScene()
    tc    = logic.keyboard.events
    m     = logic.mouse.events
    sen   = cont.sensors
    act   = cont.actuators
    so    = scene.objects
    #------ SENSORS ---------
    MouseOverButtons = sen["MouseOverButtons"]

    #----- ACTUATORS --------
    Game_restart      = act["Game_restart"]
    V_Menu            = act["V_Menu"]

    #------ OBJECTS ---------
    #Point_MenuPause  = so["Point_MenuPause"]
    
    #------------------------
    #------------------------

    own.buttons_menu_gameover( cont,sen ,act,
        mouse_over_buttons  = MouseOverButtons,
        game_reicinar_level = Game_restart,
        V_Menu              = V_Menu
        )


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
    MouseOverButtons = sen["MouseOverButtons"]

    #----- ACTUATORS --------
    SceneLoadingGame = act["SceneLoadingGame"]

    #------ OBJECTS ---------

    #------------------------
    
    #------------------------
    own.buttons_menu_main(cont, sen ,act ,
        mouse_over_buttons = MouseOverButtons,
        scene_load_game    = SceneLoadingGame
        )

    pass