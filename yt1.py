from googleapiclient.discovery import build 
api_key = "AIzaSyBfEWLrzQxJ4yAd_uzWqLqt_Srg4vMLWBw"

youtube = build("youtube", "v3", developerKey=api_key)
request = youtube.channels().list(
    part="statistics",
    forUsername="BBCNews"
)

response = request.execute() 
print(response)