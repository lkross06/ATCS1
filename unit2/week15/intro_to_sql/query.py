#Lucas Ross 10 Jan 2023
#Purpose: Query database using SQL

import sqlite3
import pandas as pd

file = "weather.db"

#format output
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

#connect to and query db
connect = sqlite3.connect(file)

#sql command
select = " SELECT * FROM observations ORDER BY timestamp; "
tselect = " SELECT MIN(temperature), MAX(temperature) FROM observations; "
cselect = "SELECT temperature, windspeed, textDescription FROM observations where textDescription = 'Clear'; "
hselect = "SELECT MIN(relativeHumidity), MAX(relativeHumidity) FROM observations; "

#print out the query
result = pd.read_sql_query(hselect, connect)
print(result)