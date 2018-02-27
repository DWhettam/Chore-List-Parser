import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import pprint
pp = pprint.PrettyPrinter()

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Chores').sheet1

date = datetime.datetime.today()
weekday = date.weekday()
startdate = sheet.cell(11,2)

chores = sheet.get_all_records()
