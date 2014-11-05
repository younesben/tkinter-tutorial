from Tkinter import *
from window import *

def main():
	root = Tk()
	root.geometry("250x150+300+300")
	app = window(root)
	root.mainloop()

if __name__ == '__main__':
	main()
