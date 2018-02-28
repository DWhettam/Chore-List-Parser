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
startdate = datetime.datetime.strptime(sheet.cell(11,2).value, '%d/%m/%Y')

weeks = int(round((date-startdate).days /7, -1)) + 1
week_column = 0
chores = sheet.get_all_records()
pp.pprint(chores)
for idx, week in enumerate(chores[1]):
    if str(weeks) in week:
        week_column = week
