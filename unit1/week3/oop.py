'''
classes
'''
from pydoc import classname


class className:
    '''
    attributes
    '''
    attr1 = 0
    __attr2 = 0
    _attr3 = 0

    '''
    contructor
    '''
    def __init__(self, num2):
        #define attributes of class
        '''
        public (nothing)
        can be accessed inside and outside of the class
        '''
        self.attr1 = 1
        '''
        private (__)
        can be accessed 
        '''
        self.__attr2 = num2
        '''
        protected (_)
        can be accessed inside the class only
        '''
        self._attr3 = 3
    
    '''
    overwriting a function (casting to str) with double underscore
    '''
    def __str__(self):
        return "this is a string yay"
    
    '''
    method
    
    must ALWAYS have self (equivalent to "this" in java)
    '''
    def add2(self, num):
        return num + 2

'''
create an object from a class
'''
obj = className(4)
print(obj.add2(7))


'''
UML class diagram: organize the data types of inputs and outputs, attrs, etc.
(since python does not indicate data type but is data type sensitive)

-   attribute
+   methods

example:

rectangle
-length:float
-width:float

+rectangle(l:float, w:float)
+setsize(l:float, w:float):float
+getarea():float
'''

'''
function object

you can pass the name of a function to another function where it can be called (if it has access)
'''

def do_twice(f, s):
    f(s)
    f(s)

do_twice(print, "HI")
