import json


class JsonClass():
	def __init__(self):
		pass

	def json_read(self , name_file ):
		with open( name_file + '.json', "r" , encoding="utf8") as js_file:
			return json.load(js_file)

		pass
