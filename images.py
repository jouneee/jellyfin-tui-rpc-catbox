import requests
import sys
import traceback

api_token = "YOUR_API_TOKEN_HERE"
url = 'http://"YOUR_URL_HERE"/Sessions'

headers = {"Authorization": f'MediaBrowser Token={api_token}'}

parameters = dict(DeviceId="YOUR_DEVICE_ID_HERE")

try: 
    resp = requests.get(url=url, params=parameters, headers=headers )
    data = resp.json() 
    album_id = data[0]["NowPlayingItem"]["AlbumId"]
    d = requests.get(f'http://YOUR_URL_HERE/Items/{album_id}/Images/Primary')
    with open ('temp_image.jpeg', 'wb') as f:
        f.write(d.content)

    with open('temp_image.jpeg', 'rb') as f:
        data = {
            'reqtype': (None, 'fileupload'),
            'userhash': (None, ''),
            'fileToUpload': f
        }
        r = requests.post("https://catbox.moe/user/api.php", files=data)

    if not r.ok:
        print(r.text[:1000])
        exit(1)

    print(r.text, end='')

except:
    traceback.print_exc(file=sys.stdout)
    exit(1)
