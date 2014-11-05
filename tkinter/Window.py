from Tkinter import *

# Inherits the Frame class. "Self" is an instance of Frame
class Window(Frame):

	# Constructor
	def __init__(self, parent):
		'''
		Calling the constructor method of the inherited class. background specifies
		the color of the Frame widget
		'''
		Frame.__init__(self, parent, background = "white")

		# Instance variables of the class
		self.parent = parent

		# Call the method to create the window 
		self.initUI()

	def initUI(self):
		# Set the tiltle of the window
		self.parent.title("Simple")

		'''
		Geometry manager. Organizes widgets into horizontal and vertical boxes. The 
		Frame widget is place on the root window expanding on both sides
		'''
		self.pack(fill = BOTH, expand = 1)
		
		# Call method tho center window
		self.centerWindow()

	def centerWindow(self):
		width = 290
		height = 150

		screen_width = self.parent.winfo_screenwidth()
		screen_height = self.parent.winfo_screenheight()

		x = (screen_width - width)/2
		y = (screen_height - height)/2

		self.parent.geometry('%dx%d+%d+%d' % (width, height, x, y))
