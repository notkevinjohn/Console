from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
import datetime
import os
import sys

class Console(ScrollView):

	Builder.load_file("Console.kv")
	rowHeight = 22

	pallet = {
		'yellow':'FFFF00',
		'white':'FFFFFF',
		'blue':'0099FF',
		'green':'00FF00',
		'red':'FF0000',
		'purple':'FF00FF',
		'orange':'FFBB00',
		'gray':'999999'
	}

	def __init__(self, logDir, logFile, **kwargs):
		super(Console, self).__init__(**kwargs)
		self.consoleGrid = ConsoleGrid()
		self.consoleGrid.height = 0
		self.add_widget(self.consoleGrid)
		self.file = logFile
		self.dir = logDir

	def clear(self):
		self.consoleGrid.clear_widgets();
		self.consoleGrid.height = 0

	def message(self, text, color='default'):
		self.addText(text, color, True, True, False)

	def message_temp(self, text, color='default'):
		self.addText(text, color, True, True, True)

	def note(self, text, color='default'):
		self.addText(text, color, True, False, True)

	def note_temp(self, text, color):
		self.addText(text, color, True, False, True)

	def log(self, text):
		self.addText(text, 'default', False, True, False)	
	

	def addText(self, text, color, Console, Log, Temp):
		if Log:
			now = datetime.datetime.now()
			if not os.path.isdir(self.dir):
				print "Error: log directory "+self.dir+" does not exist!"
				return

			path = self.dir+"/"+self.file
			f = open(path, "a")
			f.write(now.strftime("%Y-%m-%d %H:%M")+": "+str(text)+"\n")
			f.close()

		if Console:
			for label in self.consoleGrid.children:
				if label.Temp == True:
					self.removeLabel(label)
	
			label = ConsoleLabel(Temp, font_size=self.rowHeight - 4)
			label.height = self.rowHeight

			color = color.lower().strip()
			if color in self.pallet:
				color = self.pallet[color]
			else:
				color = self.pallet['white']
			label.text = '[color='+color+']'+str(text)+'[/color]'		
			self.addLabel(label)		
	
	def addLabel(self, label):
		self.consoleGrid.height += self.rowHeight
		self.consoleGrid.add_widget(label)
		self.scroll_to(label)

	def removeLabel(self, label):
		self.consoleGrid.height -= self.rowHeight
		self.consoleGrid.remove_widget(label)

class ConsoleLabel(Label):
	def __init__(self, Temp, *args, **kwargs):
		super(ConsoleLabel, self).__init__(*args, **kwargs)
		self.Temp = Temp

class ConsoleGrid(GridLayout):
	pass
