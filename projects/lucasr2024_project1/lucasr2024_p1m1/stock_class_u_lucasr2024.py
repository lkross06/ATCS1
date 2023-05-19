#Lucas Ross, Sep. 8 2022
'''
LINK TO UML CLASS DIAGRAM
https://cloud.smartdraw.com/share.aspx/?pubDocShare=6CB7354D670C028E40F223E25F407FA68DC
'''

#import for date attr of DailyData
from datetime import date as d

'''
handles a company's stock
'''
class Stock:
    symbol = ""
    name = ""
    shares = 0
    DataList = []

    '''
    constructor
    initializes the stock with unique variables (symbol and company name)
    '''
    def __init__(self, symbol, name, shares):
        '''
        symbol and company name are unique variables that MUST be defined to distinguish
        this object from others. shares is a value that is not unique and if an invalid
        input is entered (i.e. less than zero or not an integer), we can set it to default
        value of 0. if symbol or company name are not valid, throw an Error.
        '''
        s1 = self.setsymbol(symbol)
        n = self.setname(name)
        s2 = self.setshares(shares)

        if not(s1 and n and s2):
            raise ValueError("Invalid inputs to Stock constructor.")
       
    
    '''
    adds a daily data object to the stock's data history
    '''
    def add_data(self, stock_data):
        self.DataList.append(stock_data)
    
    '''
    sets symbol attr (unique) if it is a string
    returns true if it can be set successfully, false otherwise
    '''
    def setsymbol(self, s):
        if isinstance(s, str):
            self.symbol = s
            return True
        return False
    
    '''
    sets name attr (unique) if it is a string
    returns true if it can be set successfully, false otherwise
    '''
    def setname(self, n):
        if isinstance(n, str):
            self.name = n
            return True
        return False

    '''
    sets shares attr if it is a positive int
    otherwise, set to default value (0)
    returns true if it can be set successfully, false otherwise
    '''
    def setshares(self, s):
        if str(s).isdigit():
            if int(s) > 0:
                self.shares = int(s)
        return True

'''
data from each day of trading per stock
'''
class DailyData:
    date = d #params (year:int, month:int, day:int)
    close = 0.0
    volume = 0
    '''
    constructor
    initializes the data per day per stock with unique variable date
    '''
    def __init__(self, date, close, volume):
        self.date = date
        self.close = close
        self.volume = volume

# Unit Test - Do Not Change Code Below This Line *** *** *** *** *** *** *** *** ***
# main() is used for unit testing only. It will run when stock_class.py is run.
# Run this to test your class code. Once you have eliminated all errors, you are
# ready to continue with the next part of the project.

def main():
    error_count = 0
    error_list = []
    print("Unit Testing Starting---")
    # Test Add Stock
    print("Testing Add Stock...",end="")
    try:
        testStock = Stock("TEST","Test Company",100)
        print("Successful!")
    except:
        print("***Adding Stock Failed!")
        error_count = error_count+1
        error_list.append("Stock Constructor Error")
    # Test Change Symbol
    print("Test Change Symbol...",end="")
    try:
        testStock.symbol = "NEWTEST"
        if testStock.symbol == "NEWTEST":
            print("Successful!")
        else:
            print("***ERROR! Symbol change unsuccessful.")
            error_count = error_count+1
            error_list.append("Symbol Change Error")
    except:
        print("***ERROR! Symbol change failed.")
        error_count = error_count+1
        error_list.append("Symbol Change Failure")
    print("Test Change Name...",end="")
    try:
        testStock.name = "New Test Company"
        if testStock.name == "New Test Company":
            print("Successful!")
        else:
            print("***ERROR! Name change unsuccessful.")
            error_count = error_count+1
            error_list.append("Name Change Error")
    except:
        print("***ERROR! Name change failed.")
        error_count = error_count+1
        error_list.append("Name Change Failure")
        print("Test Change Name...",end="")
    try:
        testStock.shares = 2000
        if testStock.shares == 2000:
            print("Successful!")
        else:
            print("***ERROR! Shares change unsuccessful.")
            error_count = error_count+1
            error_list.append("Shares Change Error")
    except:
        print("***ERROR! Shares change failed.")
        error_count = error_count+1
        error_list.append("Shares Change Failure")
        

    # Test add daily data
    print("Creating daily stock data...",end="")
    daily_data_error = False
    try:
        dayData = DailyData("1/1/20",float(14.50),float(100000))
        testStock.add_data(dayData)
        if testStock.DataList[0].date != "1/1/20":
            error_count = error_count + 1
            daily_data_error = True
            error_list.append("Add Daily Data - Problem with Date")
        if testStock.DataList[0].close != 14.50:
            error_count = error_count + 1
            daily_data_error = True
            error_list.append("Add Daily Data - Problem with Closing Price")
        if testStock.DataList[0].volume != 100000:
            error_count = error_count + 1
            daily_data_error = True
            error_list.append("Add Daily Data - Problem with Volume")  
    except:
        print("***ERROR! Add daily data failed.")
        error_count = error_count + 1
        error_list.append("Add daily data Failure!")
        daily_data_error = True
    if daily_data_error == True:
        print("***ERROR! Creating daily data failed.")
    else:
        print("Successful!")
    
    if (error_count) == 0:
        print("Congratulations - All Tests Passed")
    else:
        print("-=== Problem List - Please Fix ===-")
        for em in error_list:
            print(em)
    print("Goodbye")

# Program Starts Here
if __name__ == "__main__":
    # run unit testing only if run as a stand-alone script
    main()


