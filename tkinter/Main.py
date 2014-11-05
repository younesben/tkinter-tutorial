from Tkinter import *
from Window import *

def Main():
	# Main window is created. Must be created before any widgets
	root = Tk()

	# Setting a size and position for the window on the screen
	root.geometry("250x150+300+300")

	# Creating an instance of the class window
	main_window = Window(root)

	'''
	Entering the mainloop to handle events from the window system.
	These are dispatched to application widgets
	'''
	main_window.mainloop()

if __name__ == '__main__':
	Main()
