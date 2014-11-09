from Tkinter import Tk, W, E, FLAT
from ttk import Frame, Button, Label, Style, Entry
import Tkinter

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
        
        self.parent.title("Calculator")
        
        # Add padding to columns
        for i in range(0, 4):
            self.columnconfigure(i, pad = 3)  
        
        # Add padding to rows
        for i in range(0, 5):
            self.rowconfigure(i, pad = 3)
        
        # Entry widget is where digits are displayed
        entry =  Entry(self)
        
        # Place in first row and span 4 columns. Sticky expands widget in a given direction.
        # In this case from left to right
        entry.grid(row = 0, columnspan = 4, sticky = W + E)
        
        # Clear button, Second row, first column
        clear_button = Button(self, text = "Clr")
        clear_button.grid(row = 1, column = 0)
        
        # Back button
        back_button = Button(self, text = "Back")
        back_button.grid(row = 1, column = 1)
        
        # Empty space that uses the Tkinter button in order to make it flat
        empty = Tkinter.Button(self, relief = FLAT)
        empty.grid(row = 1, column = 2)
        
        # Close button
        close_button = Button(self, text = "Close")
        close_button.grid(row = 1, column = 3)
                
        # Show the fram widget and gives it an initial size
        self.pack()
        
        
    # Set the style of the window
    def style(self):
        # Configure Button widget with padding and font
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