from googleapiclient.discovery import build 
creds = "creds.txt"

with open(creds, "r") as f:
    for line in f:
        api_key = line

youtube = build("youtube", "v3", developerKey=api_key)
request = youtube.channels().list(
    part="statistics",
    forUsername="BBC"
)

response = request.execute() 
print(response)