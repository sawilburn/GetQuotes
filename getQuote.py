import requests
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('sampleoauthexample-8d2caab9b693.json', scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the spreadsheet (replace 'Your Spreadsheet Name' with your actual spreadsheet name)
spreadsheet = client.open('Quotes on SPX PUT')

# Access a specific worksheet within the spreadsheet
worksheet = spreadsheet.worksheet('Sheet1')

# Specify the column you want to retrieve
column_index = 3  # Column C

# Get all values in the specified column
column_values = worksheet.col_values(column_index)

# Get the last value written

if column_values:
    last_value = column_values[-1]

# Get the next row index
next_row_index = len(column_values) + 1

# URL to get the SPX Quote
url = "https://api.marketdata.app/v1/options/quotes/SPX240621P04980000/?token=WFhqOU9WSG5vVll5X2FFcUdwVzRISXhCcmVTX1FmaFRqQkszQjlzbzZhaz0"

# Now loop thru and get values and write to spreadsheet
i = 0

while i < 100: 

   # Invoke the API to get the value
   response = requests.request("GET", url)

   data = response.json()

   ask_value = data.get('ask', None)
   underlying_price = data.get('underlyingPrice', None)
   open_interest = data.get('openInterest', None)

   value_ask_value = [float(item) for item in ask_value]
   value_underlying_price = [float(item)for item in underlying_price]

   # Generate Date Time
   current_datetime = datetime.now()

   # Format the date-time stamp
   datetime_stamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

   print("Datetime:" + str(datetime_stamp) + " Price:" + str(underlying_price) + " Value:" + str(ask_value) + " Open Interest:" + str(open_interest))

   # Strip brackets from the variable
   value_stripped = str(ask_value).replace("[", "").replace("]","") 

   # Write the date / time
   worksheet.update_cell(next_row_index, 1, datetime_stamp)

   # Write the value
   worksheet.update_cell(next_row_index, column_index, value_stripped)

   # Sleep for 5 minutes

   time.sleep(300)
   i+=1
   next_row_index+=1

	


