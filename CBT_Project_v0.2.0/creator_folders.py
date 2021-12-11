import os 
import sys
import shutil
import json
from JSON import JsonClass 


class CreatorFolders():
	def __init__(self):
		#self.jsn_class    = JsonClass()
		#self.cjv          = self.jsn_class.json_read( name_file="files/jsons/folders_struturs")

		#self.trava        = True
		#self.COMANDS      = self.jsn_class.json_read( name_file="files/jsons/comands" )

		pass
	def copyFilesTypes(self , path_origin , new_path ):
		
		for root , dirs , files in os.walk( path_origin ):
			for file in files:
				path_file     = os.path.join( root , file )
				new_path_file = os.path.join( new_path , file)

				if ".blend" in file:
					#shutil.copy( files[1] , new_path_file )

					print( files[1] )


				#new_path_file = os.path.join( new_path , file_name + type_extesion_file )

				#if type_extesion_file in file:
					#shutil.copy( path_file , new_path_file )
				



	#------------------------------------------------------------------------------------
	def copyScripts(self , path_origin , new_path ):
		typ = '.py'

		for root , dirs , files in os.walk( path_origin ):
			for file in files:
				path_file     = os.path.join( root , file )
				new_path_file = os.path.join( new_path , file)

				if typ in file:
					shutil.copy( path_file , new_path_file )

	#------------------------------------------------------------------------------------
	def copyFiles(self, path_file_origin ,type_file , path_file_new , blend_name):
		for root , dirs , files in os.walk( path_file_origin ):
			for file in files:
				path_file     = os.path.join(root , file )
				new_path_file = os.path.join( path_file_new , blend_name + type_file)

				if type_file in file:
					shutil.copy( path_file ,new_path_file )

	#------------------------------------------------------------------------------------
	def cratorFolders(self, list_folders , base_folder):
		path = os.getcwd()

		for folder in list_folders:
			folder_name = os.path.join(base_folder , folder)
			os.makedirs(folder_name , True)
