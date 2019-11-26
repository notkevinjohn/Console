import kivy
import time
from datetime import datetime
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from Console import Console
import threading


class Application(App):
		def build(self):
			boxlayout = BoxLayout(orientation='vertical')			
			logDir = "/home/sensys/work/sensys/tests/Console"
			logFile = "test.log"
			self.console = Console(logDir,logFile)
			boxlayout.add_widget(self.console)			
			return boxlayout

def write():
	for i in range(0,1):
		time.sleep(0.5)
		application.console.message("Here is a message in white")	
		time.sleep(0.5)
		application.console.message("Here is a message in red","Red")	
		time.sleep(0.5)
		application.console.message("Here is a message in yellow","Yellow")	
		time.sleep(0.5)
		application.console.message("Here is a message in green","green")	
		time.sleep(0.5)
		application.console.message("Here is a message in blue","blue")
		time.sleep(0.5)
		application.console.message("Here is a message in purple","purple")
		time.sleep(0.5)
		application.console.message("Here is a message in orange","orange")
		time.sleep(1)
		application.console.message_temp("Here is a temp message 1/3","gray")
		time.sleep(1)
		application.console.message_temp("Here is a temp message 2/3","gray")
		time.sleep(1)
		application.console.message_temp("Here is a temp message 3/3","gray")
		time.sleep(1)
		application.console.note("This will not show in the log")
		time.sleep(1)
		application.console.note_temp("This will not show in the log, and it won't last here", "red")
		time.sleep(1)
		application.console.log("This will only show in the log")
		time.sleep(1)
		application.console.message("Complete","green")	
		time.sleep(5)
		application.console.clear()	
	
if __name__ == '__main__':
        Window.size = (1280,800)
        Window.fullscreen = False
        application = Application()
        t1 = threading.Thread(target=write, args=()) 
        t1.start()
        application.run()