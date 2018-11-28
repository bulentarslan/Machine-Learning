'''This script fetches historical commodity data from investing.com and returns commodity name, mean and variance. Written by Bulent Arslan'''

import argparse
import requests
from datetime import datetime
import pandas as pd

parser = argparse.ArgumentParser(description='Fetches historical commodity data\
from investing.com')
parser.add_argument('start',help='historical commodity data starting date. format: MM/DD/YYYY')
parser.add_argument('end',help='historical commodity data ending date. format: MM/DD/YYYY')
parser.add_argument('curr_id',help='commodity id. 8830 for gold, 8836 for silver')

def format_time(time):
    parsed_time = datetime.strptime(time,'%Y-%m-%d')
    formatted_time = parsed_time.strftime('%m/%d/%Y')
    return formatted_time

def select_commodity(commodity):
    if commodity == 'gold':
        curr_id = '8830'
    elif commodity == 'silver':
        curr_id = '8836'
    else:
        raise AssertionError('invalid commodity name')
    return curr_id

args = parser.parse_args()
date_start = format_time(args.start)
date_end = format_time(args.end)
curr_id = select_commodity(args.curr_id)

# date_start = '01/01/2012' # Query start time, MM/DD/YYYY
# date_end = '09/30/2018'   # Query end time, MM/DD/YYYY
# curr_id = '8830'          # Commodity ID, 8830 for gold, 8836 for silver, 18 for USD/TRY

s = requests.session()
url = 'https://www.investing.com/instruments/HistoricalDataAjax'
headers={'Origin': 'http://www.investing.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Date':'Tue, 21 Oct 2018 03:09:55 GMT',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest'}
data = {'curr_id': curr_id,
'st_date': date_start,
'end_date': date_end,
'interval_sec': 'Daily',
'sort_ord': 'DESC',
'action': 'historical_data'}
r = s.post(url,headers=headers,data=data)

data = pd.read_html(r.content)
df =data[0]
df.Date = pd.to_datetime(df.Date)
df = df.set_index(df.Date)
ret = [args.curr_id,df.Price.mean(),df.Price.var()]
print(ret)