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

	yellow = '[color=FFFF00]'
	blue = '[color=0000FF]'
	green = '[color=00FF00]'
	red = '[color=FF0000]'
	end = '[/color]'
	recurision = 0

	def __init__(self, logDir, logFile, **kwargs):
		super(Console, self).__init__(**kwargs)
		self.consoleGrid = ConsoleGrid()
		self.add_widget(self.consoleGrid)
		self.file = logFile
		self.dir = logDir

	def clear(self):
		self.consoleGrid.clear_widgets();

	def addText(self, text, color=None, Temp=False):
		for item in self.consoleGrid.children:
			if item.Temp == True:
				self.consoleGrid.remove_widget(item)
		try:
			now = datetime.datetime.now()
			if not os.path.isdir(self.dir):
				print "log directory "+self.dir+" does not exist!"
				return

			if Temp == False:
				path = self.dir+"/"+self.file
				f = open(path, "a")
				f.write(now.strftime("%Y-%m-%d %H:%M")+": "+str(text)+"\n")
				f.close()

			label = ConsoleLabel(Temp)
			label.size = (10,10)

			if color == 'yellow':
				label.text = self.blue+str(text)+self.end
			if color == 'green':
				label.text = self.green+str(text)+self.end
			elif color == 'red':
				label.text = self.red+str(text)+self.end
			elif color == 'blue':
				label.text = self.blue+str(text)+self.end
			else:
				label.text = str(text)

			self.consoleGrid.add_widget(label)
			self.scroll_to(label)
		except:
			if self.recurision < 10:
				self.addText(text, color)
				self.recursion += 1
			else:
				self.recursion = 0 


class ConsoleLabel(Label):
	def __init__(self, Temp, *args, **kwargs):
		super(ConsoleLabel, self).__init__(*args, **kwargs)
		self.Temp = Temp

class ConsoleGrid(GridLayout):
	pass
