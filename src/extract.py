import gspread
import numpy as np
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# Define the path to your service account credentials JSON file
credentials_path = "/path/to/credentials.json"

# Define the ID of the Google Sheet you want to extract data from
sheet_id = "your_sheet_id"

# Define the name of the worksheet you want to extract data from
worksheet_name = "your_worksheet_name"

# Define the range of cells you want to extract data from
range_name = "A1:C10"

# Authenticate with Google Sheets using the service account credentials
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
client = gspread.authorize(credentials)

# Open the Google Sheet
sheet = client.open_by_key(sheet_id)

# Select the worksheet
worksheet = sheet.worksheet(worksheet_name)

# Extract the data from the specified range
data = worksheet.get(range_name)

# Print the extracted data
for row in data:
    print(row)
