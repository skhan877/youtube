from googleapiclient.discovery import build 
creds = "creds.txt"

with open(creds, "r") as f:
    for line in f:
        api_key = line

youtube = build("youtube", "v3", developerKey=api_key)

content_req = youtube.channels().list(
    part="contentDetails",
    forUsername="BenParkes"
)

content_resp = content_req.execute() 
playlistId = content_resp['items'][0]['contentDetails']['relatedPlaylists']['uploads']
# print(playlistId)


playlist_req = youtube.playlistItems().list(
    part="snippet",
    playlistId="UUxvOq2gCCMnnQq-XlO68STA",
    maxResults=10
)

playlist_resp = playlist_req.execute() 

keys = ['publishedAt', 'title']

for i in range(len(playlist_resp['items'])):
    videos = playlist_resp['items'][i]['snippet']
    print([videos.get(key) for key in keys])
