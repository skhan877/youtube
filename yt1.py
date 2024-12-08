from googleapiclient.discovery import build 
creds = "creds.txt"

with open(creds, "r") as f:
    for line in f:
        api_key = line

youtube = build("youtube", "v3", developerKey=api_key)

# request = youtube.channels().list(
#     part="contentDetails",
#     forUsername="NovaraMedia"
# )

# response = request.execute() 
# print(response)


playlist_req = youtube.playlistItems().list(
    part="snippet",
    playlistId="UUOzMAa6IhV6uwYQATYG_2kg",
    maxResults=10
)

playlist_resp = playlist_req.execute() 
print(playlist_resp)
