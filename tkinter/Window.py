from Tkinter import *

class Window(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent, background = "white")

		self.parent = parent
		self.initUI()

	def initUI(self):
		self.parent.title("Simple")
		self.pack(fill = BOTH, expand = 1)
		self.centerWindow()

	def centerWindow(self):
		width = 290
		height = 150

		screen_width = self.parent.winfo_screenwidth()
		screen_height = self.parent.winfo_screenheight()

		x = (screen_width - width)/2
		y = (screen_height - height)/2

		self.parent.geometry('%dx%d+%d+%d' % (width, height, x, y))
