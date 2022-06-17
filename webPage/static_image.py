from mapbox import Static
from sklearn.cluster import KMeans
import pandas as pd
import os

df=pd.read_csv("data/new_fire_weather_data.csv")
service =Static(access_token=os.getenv('MAPBOX'))
points =[[round(float(df.iloc[i].incident_longitude),5),round(float(df.iloc[i].incident_latitude),5)] for i in range(df.shape[0])]
km=KMeans(n_clusters=20)
km.fit(points)
fires=km.cluster_centers_
points=[]
for i in range(len(fires)):
    points.append({
        'type': 'Feature',
        'properties':{'marker-size':'small'},
        'geometry': {
            'type': 'Point',
            'coordinates': [round(float(fires[i][0]),2),round(float(fires[i][-1]),2)]}
        })
# >>> bend = {
# ...    'type': 'Feature',
# ...    'properties': {'name': 'Bend, OR'},
# ...    'geometry': {
# ...        'type': 'Point',
# ...        'coordinates': [-121.3153, 44.0582]}}
response = service.image('mapbox.satellite',z=5 ,lon=-119,lat=37,width=320,height=394,features=points)
print(response.status_code)
with open('/tmp/map.png', 'wb') as output:
    _ = output.write(response.content)