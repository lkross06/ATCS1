from tkinter import *
#call libraries to open and save file names


class FileEditor:
    def __init__(self):
        window = Tk()
        window.title("Simple Text Editor")
        
        # Create a menu bar
        menubar = Menu(window)
        window.config(menu = menubar) # Display the menu bar
        
        # create a pulldown menu, and add it to the menu bar
        operationMenu = Menu("write code here")
        menubar.add_cascade("write code here" )
        operationMenu.add_command("write code here")
        operationMenu.add_command("write code here")
           
        
        # Add a tool bar frame 
        frame0 = Frame(window) # Create and add a frame to window
        frame0.grid(row = 1, column = 1, sticky = W)
        
        # Create images
        #image 1 (Hint: use Photoimage)
        #image 2 (Hint : use Photoimage)
        
        Button(frame0, image = opneImage, command = 
            self.openFile).grid(row = 1, column = 1, sticky = W)
        Button(frame0, image = saveImage,
            command = self.saveFile).grid(row = 1, column = 2)
        
        frame1 = Frame(window) # Hold editor pane
        frame1.grid(row = 2, column = 1)
        
        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side = RIGHT, fill = Y)
        self.text = Text(frame1, width = 40, height = 20, 
            wrap = WORD, yscrollcommand = scrollbar.set)
        self.text.pack()
        scrollbar.config(command = self.text.yview)
        
        window.mainloop() # Create an event loop

    def openFile(self):
        pass
        #Replace pass with the code here
        
    
    def saveFile(self):
        pass
        #Replace pass with the code here
        
    
FileEditor() # Create GUI