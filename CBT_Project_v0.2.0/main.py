import os 
import sys
import shutil

#import json
#from JSON import JsonClass 

from creator_folders import CreatorFolders
from dataSaveLoad import DataSaveLoad
#import notify as nt
import utilis as utlis


class GameTemplatCreator():
	def __init__(self):
		#self.jsn_class        = JsonClass()
		self.maker_folders    = CreatorFolders()
		self.datasSL          = DataSaveLoad(path ="dtsl/")

		#-------------------------------------------------------------------------------------------
		#self.struturs_folders   = self.jsn_class.json_read( name_file="folders_struturs")
		
		self.link_files_origins = [ "files/blend_template" , 
									"files/blend_template/scripts/Components/" , 
									"files/blend_template/scripts/scripts_game/" ]

		self.loop_soft          = True
		pass
	
#----------------------------------------------------------------------------------------------------------
	def inputsWrite(self):
		name_dir_base = input("--> Digite o nome da pasta principal     : ")
		name_blend    = input("--> Digite o nome do .blend do seu jogo  : ")

		return [name_dir_base , name_blend ]

#----------------------------------------------------------------------------------------------------------
	def gameTemplat(self):
		name_dir , name_blend  = self.inputsWrite()
		dir_base 			   = utlis.dict_folders["dir_folder_base"] + name_dir

		try:
			self.maker_folders.cratorFolders(list_folders       = utlis.dict_folders["GAME_TEMP"] , 
											 base_folder        = dir_base 
											 )

			self.maker_folders.copyFiles(	 path_file_origin   =  self.link_files_origins[0] ,
											 type_file 		 	= ".blend", 
											 path_file_new 	    = dir_base + "/" + utlis.dict_folders["GAME_TEMP"][3],
											 blend_name 		= name_blend 
											)

			self.maker_folders.copyScripts(  path_origin 	    = self.link_files_origins[1] , 
											 new_path   		= dir_base + "/" + utlis.dict_folders["GAME_TEMP"][4] 
											)

			self.maker_folders.copyScripts(  path_origin 	    = self.link_files_origins[2] , 
											 new_path   		= dir_base + "/" + utlis.dict_folders["GAME_TEMP"][5] 
											)

			#nt.Noti(titulo = "Finalizado" , mensagen = "Seu template foi criado com sucesso!" )


		except Exception as e:
			print(e)
		pass

#----------------------------------------------------------------------------------------------------------
	def inputActions(self):
		comands_out	  = input(f"--> Digite ({utlis.c_list[1][0]}) para mostrar a lista de comandos internos :")

		if comands_out == utlis.c_list[0][0]:
			self.gameTemplat()
		

		if comands_out == utlis.c_list[1][0]:
			print(utlis.titles[1])
			for index , value in enumerate(utlis.c_list):
				print(f"# comando --> {value[0]} ------- {value[1]} " )


		if comands_out == utlis.c_list[2][0]:
			self.loop_soft = False

#----------------------------------------------------------------------------------------------------------
	def main(self):
		while self.loop_soft:
			print(utlis.titles[0] )
			
			input_comands = self.inputActions()

		pass



#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	app = GameTemplatCreator()
	app.main()
