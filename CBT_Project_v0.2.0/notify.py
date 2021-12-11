import PySimpleGUI as sg


def Noti(titulo , mensagen ):
	layout=[
			[sg.SystemTray.notify(titulo , mensagen , icon="NotifyIcon.png")]
	]

	try:
		win = sg.Window(title="").layout(layout)
		win.read()
		win.close()

	except Exception as e:
		pass

	
	#win = sg.Window('Not',layout).read()

	

#Noti( titulo="Lld" , mensagen="SGANOG85859295" )