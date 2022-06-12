from mapbox import Static
import os


service =Static(access_token=os.getenv('MAPBOX'))

cali = {
    'type': 'Feature',
    'properties': {'name': 'Portland, OR'},
    'geometry': {
    'type': 'Point',
    'coordinates': [-119.2667,37.1137]}
    }
# >>> bend = {
# ...    'type': 'Feature',
# ...    'properties': {'name': 'Bend, OR'},
# ...    'geometry': {
# ...        'type': 'Point',
# ...        'coordinates': [-121.3153, 44.0582]}}
response = service.image('mapbox.satellite',z=5 ,lon=-119.2667,lat=37.1137,width=324,height=394)
print(response.status_code)
with open('/tmp/map.png', 'wb') as output:
    _ = output.write(response.content)