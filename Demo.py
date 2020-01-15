import kivy
import time
from datetime import datetime
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from Console import Console
import threading
from random import randint


class Application(App):
		def build(self):
			boxlayout = BoxLayout(orientation='vertical')
			logDir = "/home/sensys/work/sensys/tests/Console"
			logFile = "test.log"
			self.console = Console(logDir,logFile)
			boxlayout.add_widget(self.console)
			return boxlayout

def demo():
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

def example():
	time.sleep(0.5)
	application.console.message("Starting","green")
	application.console.note("Initializing Application...","blue")
	time.sleep(1)
	application.console.note("Application Initialized","blue")
	time.sleep(1)
	application.console.note("Loading Data...","blue")
	for i in range(0,21):
		application.console.note_temp(str(i*5)+"% loaded","yellow")
		time.sleep(0.25)
	time.sleep(0.5)
	application.console.note("Data Loaded","blue")
	application.console.note("Connecting To Device", "blue")
	time.sleep(1)
	application.console.message("Failed To Connect to Device, Retrying...", "red")
	time.sleep(1)
	application.console.message("Connected to Device", "green")
	application.console.note("Downloading Data...", "blue")
	for i in range(0,5):
		data = []
		for i in range(0,20):
			data.append(str(randint(0,256)))
		application.console.message("["+",".join(data)+"]", "grey")
		time.sleep(0.5)
	application.console.note("Data Downloaded", "blue")
	application.console.note("Proccessing Data...", "blue")
	for i in range(0,21):
                application.console.note_temp(str(i*5)+"% Processed","yellow")
                time.sleep(0.25)
        time.sleep(0.5)
	application.console.message("Final Result: 42","purple")
	time.sleep(0.5)
	application.console.message("Complete","green")


if __name__ == '__main__':
        Window.size = (800,600)
        Window.fullscreen = False
        application = Application()
        t1 = threading.Thread(target=example, args=()) 
        t1.start()
        application.run()
