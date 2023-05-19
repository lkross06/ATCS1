# -*- coding: utf-8 -*-
"""
@author: praga
"""
# -*- coding: utf-8 -*-
"""
@author: Pragati 
"""

#Lucas Ross Sep. 21 2022
from datetime import datetime
from stock_class import Stock, DailyData
from account_class import Traditional, Robo

def add_stock(stock_list):
    while True:
        print("\n---- Add Stock ----")

        #must be between 1-5 characters
        symbol = ""
        while True:
            temp1 = input("Enter Stock Symbol: ") 
            temp1 = temp1.upper()
            if len(temp1) > 5 or len(temp1) < 1:
                temp = input("Incorrect input, Symbol must be between 1-5 characters. Press Enter to Continue. ")
            else:
                symbol = temp1
                break
        
        #no rules for this one    
        name = input("Enter Stock Name: ")

        #must be a pos number
        shares = 0.0
        while True:
            temp2 = input("Enter the amount of Shares: ")
            try:
                temp2 = float(temp2)
                if temp2 < 0.0:
                    temp = input("Incorrect input, Shares must be positive number. Press Enter to Continue. ")
                else:
                    shares = temp2
                    break
            except ValueError:
                temp = input("Incorrect input, Shares must be a number. Press Enter to Continue. ")

        new = Stock(symbol, name, shares)
        stock_list.append(new)

        temp = input("\nStock added, press Enter to Continue, or 0 to add another Stock: ")
        if temp != "0":
            break

# Remove stock and all daily data
def delete_stock(stock_list):
    print("\n---- Delete Stock ----")

    #print all symbols
    sl_str = "Stock List: ["
    i = 1
    for st in stock_list:
        sl_str += str(st.symbol)
        if i < len(stock_list):
            sl_str += ", "
            i += 1
    sl_str += "]\n"
    print(sl_str)

    sy = input("Enter Stock Symbol to delete: ").upper()

    rem = "a" #symbols cant be lowercase so it will NEVER be "a"
    found = False
    i = 0
    for st in stock_list:
        if st.symbol == sy:
            found = True
            rem = stock_list.pop(i)
            break
        i += 1
    if found:
        print("Deleted " + str(rem.symbol) + ".")
    else:
        print("Error: Symbol not found.")
    
    temp = input("\nPress Enter to Continue. ")
    
# List stocks being tracked
def list_stocks(stock_list):
    print("\n---- Stock List ----")
    print("SYMBOL\t\tNAME\t\tSHARES")
    print("---------------------------------------")
    for i in stock_list:
        print(str(i.symbol) + "\t\t" + str(i.name) + "\t\t" + str(i.shares))

    temp = input("\nPress Enter to Continue.")
    
# Add Daily Stock Data
def add_stock_data(stock_list):
    print("\n---- Add Daily Stock Data ----")

    #print all symbols
    sl_str = "Stock List: ["
    i = 1
    for st in stock_list:
        sl_str += str(st.symbol)
        if i < len(stock_list):
            sl_str += ", "
            i += 1
    sl_str += "]\n"
    print(sl_str)

    sy = input("Enter Stock Symbol to add Daily Stock Data to: ").upper()

    add = "a" #symbols cant be lowercase so it will NEVER be "a"
    found = False
    i = 0
    for stock in stock_list:
        if stock.symbol == sy:
            found = True
            add = stock
            break
        i += 1
    if found:
        print("Addding Daily Stock Data to " + str(add.symbol) + ".")
        print("Enter Blank Line to Cancel.")
        
        data = input("\nEnter Date, Price, Volume (mm/dd/yy, xx.xx, n): ")
        while data != "":
            date, price, volume = data.split(",") #makes three variables from the output of an array
            daily_data = DailyData(datetime.strptime(date,"%m/%d/%y"),float(price),float(volume))
            add.add_data(daily_data)

            temp = input("Daily Stock Data added to " + str(add.symbol) +". Press Enter to Continue. ")
            data = input("\nEnter Date, Price, Volume (mm/dd/yy, xx.xx, n): ").strip(" ") #remove the spaces if needed
        print("Successfully cancelled adding to Daily Stock Data.")
    else:
        print("Error: Symbol not found. Daily Stock Data was not able to be added.")
    temp = input("\nPress Enter to Continue. ")


#creates a retirement account for the user based on two different types of accounts
def investment_type(stock_list):
    print("\n---- Investment Account ----\n")

    bal = 0
    while True:
        tbal = input("Enter initial balance: ")
        try:
            bal = float(tbal)
            break
        except ValueError:
            _ = input("Incorrect input, balance must be a positive integer. Press Enter to Continue.")

    num = 0
    while True:
        tnum = input("Enter account number: ")
        if tnum.isdigit():
            num = int(tnum)
            break
        else:
            _ = input("Incorrect input, balance must be a positive integer. Press Enter to Continue.")
        
    while True:
        acc = input("Choose investment account type, (T) traditional or (R) Robo: ")

        if acc.lower() == "r":
            print()
            yr = 0
            while True:
                tyr = input("Enter number of years until requirement: ")
                if tyr.isdigit():
                    yr = int(tyr)
                    break
                else:
                    _ = input("Incorrect input, balance must be a positive integer. Press Enter to Continue.")

            robo = Robo(float(bal), int(num), int(yr))
            print("Your investment return is $" + str(robo.investment_return()) + " USD.")
            break

        elif acc.lower() == "t":
            trad = Traditional(float(bal), int(num))
            temp_list = []

            #print all symbols
            sl_str = "Stock List: ["
            i = 1
            for st in stock_list:
                sl_str += str(st.symbol)
                if i < len(stock_list):
                    sl_str += ", "
                    i += 1
            sl_str += "]\n"
            print(sl_str)

            while True:
                sym = input("Enter stock symbol to purchase (or 0 to quit): ").upper()
                if sym == "0":
                    break

                found = False
                for st in stock_list:
                    if st.symbol == sym:
                        found = True
                        curr = st
                        break
                if found:
                    shares = int(input("Enter number of shares to buy from [" + sym + "]: "))

                    print("Bought " + str(shares) + " shares of [" + sym + "].\n")

                    curr.shares += shares
                    temp_list.append(curr)
                else:
                    print("Error: Symbol not found.")
            trad.add_stock(temp_list)
            break

        else:
            _ = input("Incorrect input, enter \"T\" for traditional account or \"R\" for robo account. Press Enter to continue. ")

# Function to create stock chart
def display_stock_chart(stock_list,symbol):
    print("This method is under construction")

# Display Chart
def display_chart(stock_list):
    print("This method is under construction")
                
 # Get price and volume history from Yahoo! Finance using CSV import.
def import_stock_csv(stock_list):
    print("This method is under construction")
    
   # Display Report 
def display_report(stock_list):
    print("This method is under construction")
    
def main_menu(stock_list):
    option = ""
    while True:
        print("\n---- Stock Analyzer ----")
        print("1 - Add Stock")
        print("2 - Delete Stock")
        print("3 - List stocks")
        print("4 - Add Daily Stock Data (Date, Price, Volume)")
        print("5 - Show Chart")
        print("6 - Investor Type")
        print("7 - Load Data")
        print("0 - Exit Program")
        option = input("Enter Menu Option: ")
        if option =="0":
            print("Goodbye")
            break
        
        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            delete_stock(stock_list)
        elif option == "3":
            list_stocks(stock_list)
        elif option == "4":
           add_stock_data(stock_list) 
        elif option == "5":
            display_chart(stock_list)
        elif option == "6":
            investment_type(stock_list)
        elif option == "7":
            import_stock_csv(stock_list)
        else:
            #TODO: check if this is invalid input or whatnot?
            print("Goodbye")

# Begin program
def main():
    stock_list = []
    main_menu(stock_list)

# Program Starts Here
if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()