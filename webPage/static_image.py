from mapbox import Static
import pandas as pd
import os

df=pd.read_csv("data/new_fire_weather_data.csv")
service =Static(access_token=os.getenv('MAPBOX'))
fires=[]
for i in range(30):
    print(f'{round(float(df.iloc[i].incident_latitude),2)}--{round(float(df.iloc[i].incident_longitude),2)}')
    fires.append({
        'type': 'Feature',
        'properties':{'name':'fire'},
        'geometry': {
            'type': 'Point',
            'coordinates': [round(float(df.iloc[i].incident_longitude),2),round(float(df.iloc[i].incident_latitude),2)]}
        })
# >>> bend = {
# ...    'type': 'Feature',
# ...    'properties': {'name': 'Bend, OR'},
# ...    'geometry': {
# ...        'type': 'Point',
# ...        'coordinates': [-121.3153, 44.0582]}}
response = service.image('mapbox.satellite',z=5 ,lon=-119.2667,lat=37.1137,width=324,height=394,features=fires)
print(response.status_code)
with open('/tmp/map.png', 'wb') as output:
    _ = output.write(response.content)