import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()
DEVELOPER_KEY = os.getenv('GOOGLE_DEV_KEY')
youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)


def get_latest_video_link(playlist_id):
    req = youtube.playlistItems().list(
        playlistId=playlist_id,
        part='snippet',
        maxResults=1
    )

    res = req.execute()

    video_id = res['items'][0]['snippet']['resourceId']['videoId']

    link = 'https://www.youtube.com/watch?v=' + video_id

    print(link)

    return link


def get_latest_video_title(playlist_id):
    req = youtube.playlistItems().list(
        playlistId=playlist_id,
        part='snippet',
        maxResults=1
    )

    res = req.execute()

    title = res['items'][0]['snippet']['title']

    print(title)

    return title


def get_channel_id():
    req = youtube.search().list(
        part='snippet',
        type='channel',
        q='Aruka Ch. あるか'
    )

    res = req.execute()

    channel_id = res['items'][0]['snippet']['channelId']

    print(channel_id)

    return channel_id


def get_uploads_id():
    channel_id = get_channel_id()

    req = youtube.channels().list(
        part='contentDetails',
        id=channel_id
    )

    res = req.execute()

    uploads_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    print("Uploads ID: ", uploads_id)

    return uploads_id

#get_latest_video()
#get_channel_id()
#get_uploads_id()