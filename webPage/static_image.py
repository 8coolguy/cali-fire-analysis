from mapbox import Static
import os


service =Static(access_token=os.getenv('MAPBOX'))

portland = {
    'type': 'Feature',
    'properties': {'name': 'Portland, OR'},
    'geometry': {
    'type': 'Point',
    'coordinates': [-122.7282, 45.5801]}
    }
# >>> bend = {
# ...    'type': 'Feature',
# ...    'properties': {'name': 'Bend, OR'},
# ...    'geometry': {
# ...        'type': 'Point',
# ...        'coordinates': [-121.3153, 44.0582]}}
response = service.image('mapbox.satellite', features=[portland])
print(response.status_code)
with open('/tmp/map.png', 'wb') as output:
    _ = output.write(response.content)