from Tkinter import Tk, BOTH
from ttk import Style, Frame, Button

# Inherits the Frame class from ttk. "Self" is an instance of Frame
class Window(Frame):

	# Constructor
	def __init__(self, parent):
		'''
		Calling the constructor method of the inherited class. background specifies
		the color of the Frame widget
		'''
		Frame.__init__(self, parent)

		# Instance variables of the class
		self.parent = parent

		# Call the method to create the window 
		self.initUI()

	# Initialize the UI
	def initUI(self):
		# Set the style
		self.style()

		# Set the tiltle of the window
		self.parent.title("First example")

		'''
		Geometry manager. Organizes widgets into horizontal and vertical boxes. The 
		Frame widget is place on the root window expanding on both sides
		'''
		self.pack(fill = BOTH, expand = 1)

		# Add QUIT button
		quit_button = Button(self, text = "Quit", command = self.quit)
		quit_button.place(x = 50, y = 50)
		
		# Call method tho center window
		self.centerWindow()

	# Center the window
	def centerWindow(self):
		width = 290
		height = 150

		screen_width = self.parent.winfo_screenwidth()
		screen_height = self.parent.winfo_screenheight()

		x = (screen_width - width)/2
		y = (screen_height - height)/2

		self.parent.geometry('%dx%d+%d+%d' % (width, height, x, y))

		# Adding a them to all widgets
	def style(self):
		self.style = Style()
		self.style.theme_use("default")
