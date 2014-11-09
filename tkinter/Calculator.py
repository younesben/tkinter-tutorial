from Tkinter import Tk, W, E
from ttk import Frame, Button, Label, Style, Entry

#################### Calculator class ####################
class Calculator(Frame):
    
    def __init__(self, parent):
        # Calling the constructor method of the inherited class.
        Frame.__init__(self, parent)
        
        # Instance variables of the class
        # Root window
        self.parent = parent
        
        # Initialize the window
        self.initUI()
        
    # Initialize the UI
    def initUI(self):
        # Set the style of the window
        self.style()
        
    # Set the style of the window
    def style(self):
        Style().configure("TButton", padding = (0, 5, 0, 5), font = "serif 10")
        
        


#################### Main function ####################
def Main():
    # Main window
    root = Tk()
    
    # Instance of the window
    main_window = Calculator(root)
    
    # Entering mainloop
    main_window.mainloop()
    
    
#################### Run script ####################    
if __name__ == '__main__':
    Main()