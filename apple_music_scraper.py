import requests
from bs4 import BeautifulSoup
import json
url = "https://music.apple.com/ca/playlist/todays-hits/pl.f4d106fed2bd41149aaacabb233eb5eb"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
script_tag = soup.find('script', id='serialized-server-data')
if script_tag:
    json_data = script_tag.string
    data = json.loads(json_data)
    data_dict = json.loads(json_data)[0]

    songs =  (data_dict['data']['seoData']['ogSongs'])
    print((songs))
    song_list = []

for item in songs:
    song_dict = {
        "Artist": item['attributes']["artistName"],
        "Song": item['attributes']["name"]
    }
    song_list.append(song_dict)
json_data = json.dumps(song_list, indent=4)
print(json_data)

file_name = "apple_music_playlist_data.json"
with open(file_name, 'w', encoding='utf-8') as json_file:
    json.dump(song_list, json_file, ensure_ascii=False, indent=4)

