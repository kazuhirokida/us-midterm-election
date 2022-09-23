import requests
import pandas as pd
from datetime import datetime

data = requests.get('https://www.realclearpolitics.com/epolls/json/48_map.js').json()

row = pd.Series(data['election']['module_info']).to_frame().T

row.to_csv('data/'+datetime.today().strftime('%Y-%m-%d')+'us_midterm_house_forecast_details.csv',index=False)

row['date'] = pd.to_datetime(row.lastBuildDate,format='%a, %d %b %Y %H:%M:%S %z',utc=True).dt.date

df = pd.read_csv('https://github.com/kazuhirokida/us-midterm-election/raw/main/us_midterm_house_details.csv')

df = pd.concat([df,row]).drop_duplicates()

df.to_csv('us_midterm_house_forecast_details.csv',index=False)
