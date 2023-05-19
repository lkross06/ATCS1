# -*- coding: utf-8 -*-
"""
@author: praga
"""
# -*- coding: utf-8 -*-
"""
@author: Pragati 
"""

#Lucas Ross Sep. 21 2022
from contextlib import closing
from datetime import datetime
from tracemalloc import start
from xml.sax.saxutils import prepare_input_source
from stock_class import Stock, DailyData
from account_class import Traditional, Robo
from matplotlib import pyplot as plt

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
    #create three empty lists to store series
    date = []
    price = []
    volume = []
    #store name of company for title
    name = ""
    
    #iterate through stocks for a certain stock
    for st in stock_list:
        #if we find the right stock
        if st.symbol == symbol:
            #change company name for later
            name = st.name
            #loop through that stock's daily data and add each entry to the lists we made (they will naturally be in order)
            for dd in st.DataList:
                date.append(dd.date)
                price.append(dd.close)
                volume.append(dd.volume)

    #make line graph (x - date, y - price)
    plt.plot(date, price)

    plt.grid(True)
    plt.title(name)
    plt.xlabel("Date (mm/dd/yy)")
    plt.ylabel("Price (USD)")

    plt.show() #show the line plot

# Display Chart
def display_chart(stock_list):
    print("\n---- Show Chart ----\n")
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

    found = False
    sym = input("Enter Stock Symbol to Graph: ").upper()

    for st in stock_list:
        if sym == st.symbol:
            #we dont even need to keep track of which obj it was
            found = True
            break

    if found:
        display_stock_chart(stock_list, sym)
    else:
        _ = input("Invalid input, Stock Symbol not found. Press Enter to continue. ")
        
                
 # Get price and volume history from Yahoo! Finance using CSV import.
def import_stock_csv(stock_list):
    print("\n---- Import Stock CSV ----")

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

    #must be between 1-5 characters
    symbol = input("Enter Stock Symbol: ").upper()
    filepath = input("Enter file path: ")

    found = False
    for st in stock_list:
        if st.symbol == symbol:
            stock = st
            found = True
            break
    if found:
        try:
            with open(filepath, "r+") as stockdata:
                datareader = stockdata.readlines()
                datareader.pop(0) #remove column titles
                for row in datareader:
                    row = row.strip("\n").split(",")
                    dates = row[0].split("-")
                    date = datetime(int(dates[0]), int(dates[1]), int(dates[2]))
                    closing_price = float(row[4])
                    volume = int(row[6])
                    dd = DailyData(date, closing_price, volume)
                    stock.add_data(dd)
            display_report(stock_list)    
        except FileNotFoundError:
            print("Error: File not found.")   
    else:
        print("Error: Symbol not found.")

    
   # Display Report 
def display_report(stock_list):
    def format_decimal(p):
        return "{:,.2f}".format(p)
    for st in stock_list:
        print("\n---- " + st.name + " [" + st.symbol + "] ----")
        print("Shares: " + str(st.shares))

        #get metrics
        count = 0
        start_price = 0
        end_price = 0
        price_change = 0
        price_total = 0
        volume_total = 0
        low_price = float("inf") #infinity
        high_price = 0
        low_vol = float("inf")
        high_vol = 0

        for dd in st.DataList:
            price = dd.close
            volume = dd.volume

            if count == 0:
                start_price = price
            if count == len(st.DataList) - 1:
                end_price = price

            price_total += price
            if price < low_price:
                low_price = price
            if price > high_price:
                high_price = price

            volume_total += volume
            if volume < low_vol:
                low_vol = volume
            if volume > high_vol:
                high_vol = volume
            
            count += 1
        
        price_change = end_price - start_price

        if count > 0:
            #now print everything out
            print("---- Summary ----")

            #price
            print("Lowest price: $" + format_decimal(low_price))
            print("Highest price: $" + format_decimal(high_price))

            avg_price = price_total / count
            print("Average price: $" + format_decimal(avg_price))

            #volume
            print("Lowest volume: " + format_decimal(low_vol))
            print("Highest volume: " + format_decimal(high_vol))

            avg_vol = volume_total / count
            print("Average volume: " + format_decimal(avg_vol))

            #more price
            print("Starting price: $" + format_decimal(start_price))
            print("Ending price: $" + format_decimal(end_price))
            print("Price change: $" + format_decimal(price_change))
            print("Profit/Loss: $" + format_decimal(price_change * st.shares))
    
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