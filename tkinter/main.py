from Tkinter import *
from Window import *

def main():
	root = Tk()
	root.geometry("250x150+300+300")
	app = Window(root)
	root.mainloop()

if __name__ == '__main__':
	main()
