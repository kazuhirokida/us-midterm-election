import requests
import pandas as pd
from datetime import datetime

data = requests.get('https://www.realclearpolitics.com/epolls/json/48_map.js').json()

row = pd.Series(data['election']['module_info']).to_frame().T

row.to_csv('data/'+datetime.today().strftime('%Y-%m-%d')+'_us_midterm_house_forecast_details.csv',index=False)

row['date'] = pd.to_datetime(row.lastBuildDate,format='%a, %d %b %Y %H:%M:%S %z',utc=True).dt.date

df = pd.read_csv('https://github.com/kazuhirokida/us-midterm-election/raw/main/us_midterm_house_forecast_details.csv',index_col='date').astype(int)

df = pd.concat([df,row.set_index('date').drop(['id','year','type','name','link','sort','description','copyright'],axis=1)].astype(int)).drop_duplicates()

df.to_csv('us_midterm_house_forecast_details.csv',index=False)
