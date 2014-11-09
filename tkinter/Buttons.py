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
        # Set the style of the window
        self.style()
        
        # Creating another
        
    # Styling the window    
    def style(self):
        self.style = Style()
        self.style.theme_use("default")
        
        # New Frame widget that expands the entire window
        # Relief = border decoration
        frame = Frame(self, relief = RAISED, borderwidth = 1)
        
        # Pack organizes widgets in horizontal and vertical boxes
        frame.pack(fill = BOTH, expand = 1)
        
        self.pack(fill = BOTH, expand = 1)
        
        # Button takes parent widget and options
        close_button = Button(self, text = "Close")
        
        # Put in horizontal box to the right, add space between widget and borders of frame
        close_button.pack(side = RIGHT, padx = 5, pady = 5)
        
        # Ok Button
        ok_button = Button(self, text = "OK")
        ok_button.pack(side = RIGHT)
        
    
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
            