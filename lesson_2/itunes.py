import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())

# Better print using json.dumps.
# print(json.dumps(response.json(), indent=2))

# Print only the track name.
# response_json = response.json()
# for result in response_json['results']:
#     print(result['trackName'])
