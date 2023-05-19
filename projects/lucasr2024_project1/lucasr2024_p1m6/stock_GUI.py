#Lucas Ross 21 Oct. 2022
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
from tkinter import filedialog as fd
from stock_class import Stock, DailyData
import matplotlib.pyplot as plt
import matplotlib.pylab as plb
from datetime import datetime

class StockApp:
    def __init__(self):
        self.stock_list = [] #this will hold our stocks
        self.curr = None #keep track of the index of our current stock
        self.title = "Stock Application" #name of application

        self.root = Tk() # Create a window
        self.root.title(self.title) # Set title
        self.root.geometry("820x700+500+100")

        #set up grid
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=3)

        #string for no stock selected (default)
        self.header_default = "No Stock Selected"

        self.header = Label(self.root, text=self.header_default, font=("TkDefaultFont", 40)) #TkDefaultFont is default font of Tkinter
        self.header.grid(column=0,row=0,columnspan=3, sticky="NS")

        self.stock_listbox()

        self.notebook = Notebook(self.root)
        self.notebook.grid(row=1, column=1, sticky="NESW")

        #make the frames for the tab container
        self.manage_tab()
        self.history_tab()
        self.report_tab()

        self.menu()

        self.root.mainloop()

    def menu(self):
        #make a menu bar widget (container for the cascade menus at the top of the window)
        menubar = Menu(self.root) #container is the root window

        #configure the root with the menu bar
        self.root.config(menu=menubar)

        web_menu = Menu(menubar, tearoff=0) #tearoff does not let you move the menu out of the window
        web_menu.add_command(label="Import CSV from Yahoo! Finance...", command=self.import_csv)

        chart_menu = Menu(menubar, tearoff=0) #tearoff does not let you move the menu out of the window
        chart_menu.add_command(label="Display Chart", command=self.display_chart)

        menubar.add_cascade(label="Web", menu=web_menu)
        menubar.add_cascade(label="Chart", menu=chart_menu)

    def stock_listbox(self):
        stocklist_group = Frame(self.root, width=30) #container
        stocklist_group.grid(row=1, column=0, sticky="NS", padx=5, pady=5)

        #set up grid
        stocklist_group.rowconfigure(0, weight=1)
        stocklist_group.rowconfigure(1, weight=9)

        stocklist_label = Label(stocklist_group, text="Stock List")
        stocklist_label.grid(row=0, sticky="NS")

        #make the listbox
        self.stocklist_list = Listbox(stocklist_group, selectmode=SINGLE)
        self.stocklist_list.grid(row=1, sticky="NS")

        #add event listener
        self.stocklist_list.bind("<<ListboxSelect>>", self.listbox_select)

    def manage_tab(self):
        #initialize and add the frame to the notebook
        manage = Frame(self.notebook)
        manage.grid()
        self.notebook.add(manage, text='Manage')

        #set up grid
        manage.columnconfigure(0, weight=1)
        manage.rowconfigure(0, weight=1)
        manage.rowconfigure(1, weight=1)

        #ADD STOCK

        #add internal elements
        addstock_group = LabelFrame(manage, text="Add Stock") #container
        addstock_group.grid(sticky="NW")

        #set up grids
        manage.columnconfigure(0, weight=1)
        manage.columnconfigure(1, weight=1)
        manage.rowconfigure(0, weight=1)
        manage.rowconfigure(1, weight=1)
        manage.rowconfigure(2, weight=1)
        manage.rowconfigure(3, weight=1)

        #symbol
        addstock_symbollabel = Label(addstock_group, text = "Symbol")
        addstock_symbollabel.grid(column=0, row=0, padx=5, pady=5)
        #DONT MIX PACK AND GRID (ONLY USE GRID)
        self.addstock_symbol = StringVar()
        self.addstock_symbolentry = Entry(addstock_group, textvariable = self.addstock_symbol)
        self.addstock_symbolentry.grid(column=1, row=0, columnspan=2, padx=5, pady=5)

        #company name
        addstock_namelabel = Label(addstock_group, text = "Name")
        addstock_namelabel.grid(column=0, row=1, padx=5, pady=5)
        self.addstock_name = StringVar()
        self.addstock_nameentry = Entry(addstock_group, textvariable = self.addstock_name)
        self.addstock_nameentry.grid(column=1, row=1, columnspan=2, padx=5, pady=5)

        #shares
        addstock_shareslabel = Label(addstock_group, text = "Shares")
        addstock_shareslabel.grid(column=0, row=2, padx=5, pady=5)
        self.addstock_shares = StringVar()
        self.addstock_sharesentry = Entry(addstock_group, textvariable = self.addstock_shares)
        self.addstock_sharesentry.grid(column=1, row=2, columnspan=2, padx=5, pady=5)

        addstock_button = Button(addstock_group,text = "New Stock",command = self.add_stock)
        addstock_button.grid(column=1, row=3, padx=5, pady=5)

        #DELETE STOCK

        deletestock_group = LabelFrame(manage, text="Delete Stock") #container
        deletestock_group.grid(row=1, sticky="NW")

        deletestock_button = Button(deletestock_group, text="Delete Selected Stock", command=self.delete_stock)
        deletestock_button.grid(column=1, row=0, padx=5, pady=5)
        

    def history_tab(self):
        #initialize and add the frame to the notebook
        history = Frame(self.notebook)
        history.grid()
        self.notebook.add(history, text='History')

        #set up grid
        history.rowconfigure(0, weight=1)

        #text box
        self.history_text = Text(history)
        self.history_text.grid(row=0, sticky="NS")

    def report_tab(self):
        #initialize and add the frame to the notebook
        report = Frame(self.notebook)
        report.grid()
        self.notebook.add(report, text='Report')

        #set up grid
        report.rowconfigure(0, weight=1)

        #text box
        self.report_text = Text(report)
        self.report_text.grid(row=0, sticky="NS")
    
    def listbox_select(self, event): #handles a new stock being selected in listbox
        curr = self.stocklist_list.curselection() #returns a tuple
        if curr == (): #when something is deselected, its an empty tuple
            index = self.curr #just reselect whatever was previously selected
        else:
            index = curr[0] #since the listbox only allows single selection, the tuple only has 1 item
        self.update_stock(index)

    def update_stock(self, i): #updates the GUI when a new stock is selected
        self.curr = i

        if i != None:
            curr_stock = self.stock_list[self.curr]
            self.header.config(text=str(curr_stock.name) + " (" + str(curr_stock.shares) + " shares)")
        else:
            self.header.config(text=self.header_default)

        self.display_history()
        self.display_report()

    def add_stock(self):
        valid = True

        #symbol must be between 1-5 characters and unique
        symbol = self.addstock_symbol.get().upper()

        if len(symbol) < 1 or len(symbol) > 5:
            valid = False
            tkinter.messagebox.showerror(title="Invalid Input", message="Symbol must be between 1-5 characters.")

        for st in self.stock_list:  
            if st.symbol == symbol:
                valid = False
                tkinter.messagebox.showerror(title="Invalid Input", message="Symbol already in use.")

        name = self.addstock_name.get()

        #shares must be a positive int
        shares = self.addstock_shares.get()
        if shares.isdigit():
            shares = int(shares)
        else:
            valid = False
            tkinter.messagebox.showerror(title="Invalid Input", message="Shares must be positive integer.")

        if valid:
            stock = Stock(symbol, name, shares)
            self.stocklist_list.insert(len(self.stock_list), symbol)
            self.stock_list.append(stock)

            #finally delete everything from the text boxes
            self.addstock_symbolentry.delete(0, END)
            self.addstock_nameentry.delete(0, END)
            self.addstock_sharesentry.delete(0, END)

    def display_history(self):
        history_default = "Date\t\tPrice\t\tVolume\n---------------------------------------\n"
        s = ""

        if self.curr != None:
            s = history_default
            stock = self.stock_list[self.curr]
            for dd in stock.DataList:
                s += dd.date.strftime("%m/%d/%y") + "\t\t" + str(dd.close) + "\t\t" + str(dd.volume) + "\n"

        #replace the text
        self.history_text.delete(1.0, END)
        self.history_text.insert(1.0, s)

    def get_summary(self, st): #gets the summary for a given stock
        def format_decimal(p): #formats any decimal to 2 decimal places
            return "{:,.2f}".format(p)

        rtn = ""

        if len(st.DataList) > 0:

            #get metrics
            start_date = ""
            end_date = ""
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
                date = dd.date.strftime("%m/%d/%Y")
                price = dd.close
                volume = dd.volume

                if count == 0:
                    start_price = price
                    start_date = date
                if count == len(st.DataList) - 1:
                    end_price = price
                    end_date = date

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
                rtn += "Summary from " + start_date + " to " + end_date + "\n\n"

                #price
                rtn += "Lowest price: $" + format_decimal(low_price) + "\n"
                rtn += "Highest price: $" + format_decimal(high_price) + "\n"

                avg_price = price_total / count
                rtn += "Average price: $" + format_decimal(avg_price) + "\n\n"

                #volume
                rtn += "Lowest volume: " + format_decimal(low_vol) + "\n"
                rtn += "Highest volume: " + format_decimal(high_vol) + "\n"

                avg_vol = volume_total / count
                rtn += "Average volume: " + format_decimal(avg_vol) + "\n\n"

                #more price
                rtn += "Starting price: $" + format_decimal(start_price) + "\n"
                rtn += "Ending price: $" + format_decimal(end_price) + "\n"

                #these two might be negative
                temp = "$" + format_decimal(price_change)
                temp2 = "$" + format_decimal(price_change * st.shares)
                if "-" in temp:
                    #must be index 1
                    temp = "-$" + temp[2:len(temp)] #removes "$-" then adds "-$"
                if "-" in temp2:
                    #must be index 1
                    temp2 = "-$" + temp2[2:len(temp2)] #removes "$-" then adds "-$"

                rtn += "Price change: " + temp + "\n"
                rtn += "Profit/Loss: " + temp2
    
        return rtn
        
    def display_report(self):
        s = ""
        
        if self.curr != None:
            stock = self.stock_list[self.curr]
            if len(stock.DataList) > 0:
                s = self.get_summary(stock)

        #replace the text
        self.report_text.delete(1.0, END)
        self.report_text.insert(1.0, s)

    def delete_stock(self):
        if self.curr != None:
            temp = self.stock_list.pop(self.curr)
            self.stocklist_list.delete(self.curr, self.curr)

            tkinter.messagebox.showinfo(title="Stock Deleted", message="[" + temp.symbol + "] successfully deleted.")

            self.update_stock(None) #once the stock is deleted, nothing is selected in the listbox

    def display_chart(self):
        if self.curr != None:
            #create three empty lists to store series
            date = []
            price = []
            volume = []
            
            st = self.stock_list[self.curr]

            for dd in st.DataList:
                date.append(dd.date)
                price.append(dd.close)
                volume.append(dd.volume)

            fig = plb.gcf()
            fig.canvas.manager.set_window_title(self.title)

            #make line graph (x - date, y - price)
            plt.plot(date, price)

            plt.grid(True)
            plt.title(st.name)
            plt.xlabel("Date (mm/dd/yy)")
            plt.ylabel("Price (USD)")

            plt.show() #show the line plot
        else:
            tkinter.messagebox.showerror(title="No Stock Selected", message="Select a stock to show chart.")
    
    def import_csv(self):
        if self.curr != None:
            stock = self.stock_list[self.curr]
            file = fd.askopenfilename()

            try:
                with open(file, "r+") as stockdata:
                    datareader = stockdata.readlines() #get everything in the CSV
                
                datareader.pop(0) #remove column titles

                for row in datareader:
                    row = row.strip("\n").split(",") #make it into an array (each item is a column)
                    dates = row[0].split("-")
                    date = datetime(int(dates[0]), int(dates[1]), int(dates[2]))
                    closing_price = float(row[4])
                    volume = int(row[6])
                    dd = DailyData(date, closing_price, volume)
                    stock.add_data(dd)
                
                self.update_stock(self.curr)
                tkinter.messagebox.showinfo(title="File Import", message="CSV data successfully imported.")
                

            except FileNotFoundError:
                tkinter.messagebox.showerror(title="File Not Found", message="File Not Found.")
        else:
            tkinter.messagebox.showerror(title="No Stock Selected", message="Select a stock to import CSV data.")

    

StockApp() #make a new object to start the GUI