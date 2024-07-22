# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import sys

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def search_videos_by_name(request_text: str, max_count:int = 5):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "OAuth2Data.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        part="snippet",
        maxResults=max_count,
        q=request_text,

    )
    response = request.execute()

    searched_videos = []
    base_url = "https://www.youtube.com/watch?v="

    for _ in range(max_count):
        video_id = response['items'][0]['id']['videoId']
        title = response['items'][0]['snippet']['title']
        link = base_url + video_id
        searched_videos.append((title,link))

    return searched_videos

def create_new_playlist(playlist_name: str):
    pass

if __name__ == "__main__":
    (' '.join(sys.argv[1:]))