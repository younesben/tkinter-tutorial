from Tkinter import Tk, RIGHT, BOTH, RAISED
from ttk import Frame, Button, Style

#################### Buttons class ####################
class Buttons(Frame):
    
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
        self.style()
        
    # Styling the window    
    def style(self):
        self.style = Style()
        
        
    
#################### Main function ####################
def Main():
    # Main window
    root = Tk()
    
    # Size and positioning
    root.geometry("300x200+300+300")
    
    # Instance of the window
    main_window = Buttons(root)
    
    # Entering mainloop
    main_window.mainloop()
    
    
#################### Run script ####################    
if __name__ == '__main__':
    Main()
            