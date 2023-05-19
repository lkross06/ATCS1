# Lucas Ross 15 Oct. 2022

from pynput.keyboard import Controller
import time as t

'''
controls the snake by simulating key presses

snake moves at a rate of 6 spaces every 0.5 secs
'''
class Snake:
    def __init__(self):
        #wait for my set up
        t.sleep(5)

        '''
        positon variable
        up      0
        right   1
        down    2
        left    3
        '''
        self.position = 1 #snake always starts right
        self.toggle = -1
        self.controller = Controller()
        self.turn_interval = 0.05 # amount of seconds to delay movement after a turn

        self.width = 10 # width of board
        self.height = 9 # height of board

        self.boring()

    #this is really stupid
    def boring(self):
        #snake starts 1/3 across the board, facing right
        self.controller.press("d") #start
        self.skip(int((self.width * 2) / 3))
        self.left()
        while True:
            self.skip(self.height / 3)
            self.left(2)
            for i in range(0, (self.width // 2) - 1):
                self.skip(self.height - 3)
                self.right(2)
                self.skip(self.height - 3)
                self.left(2)
            self.skip(self.height - 2)
            self.left()
            self.skip((self.width * 3) / 4)
            self.left()
            self.skip((self.height // 3) + 0.5)
    
    def boring_og(self):
        #snake starts 1/3 across the board, facing right
        self.controller.press("d") #start
        self.skip(6)
        self.left()
        while True:
            self.skip(3)
            self.left(2)
            for i in range(0, 4):
                self.skip(6)
                self.right(2)
                self.skip(6)
                self.left(2)
            self.skip(7)
            self.left()
            self.skip(7.5)
            self.left()
            self.skip(3.5)
            

    def left(self, n = 1): #turns left n times
        for i in range(0, n):
            if self.position == 0:
                self.controller.press("a")
                self.position = 3
            elif self.position == 1:
                self.controller.press("w")
                self.position = 0
            elif self.position == 2:
                self.controller.press("d")
                self.position = 1
            else:
                self.controller.press("s")
                self.position = 2
            t.sleep(self.turn_interval)

    def right(self, n = 1): #turns right n times
        for i in range(0, n):
            if self.position == 0:
                self.controller.press("d")
                self.position = 1
            elif self.position == 1:
                self.controller.press("s")
                self.position = 2
            elif self.position == 2:
                self.controller.press("a")
                self.position = 3
            else:
                self.controller.press("w")
                self.position = 0
            t.sleep(self.turn_interval)
    
    def skip(self, n): # goes straight for n tiles
        t.sleep(0.1 * n)

snake = Snake()
