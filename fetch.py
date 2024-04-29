import requests
from nats.aio.client import Client as NATS
from youtube_transcript_api import YouTubeTranscriptApi
import json 
import asyncio
import video_data_pb2  # Import the generated Protobuf code

# Replace with your actual API key
api_key = "AIzaSyC0hlrCFHc6dtHFFrD_B51U0Ao3ZIoU_WA"

async def main():
    
    nc = NATS()
    await nc.connect("localhost")
    js = nc.jetstream()
    
    stream_name = "youtube-news"
    await js.add_stream(name="youtube-news", subjects=["youtube-news"])
    print(f"Stream '{stream_name}' has been created.")
    
    # Define your 9 news categories
    categories = ["Top stories", "Sports", "Entertainment", "Science", "Health", "Business", "Technology", "National", "World"]

    # Define the endpoint URL
    url = "https://www.googleapis.com/youtube/v3/search"

    # Loop over the categories
    for category in categories:
        # Define the parameters
        params = {
            "part": "snippet",
            "maxResults": 10,
            "order": "viewCount",
            "type": "video",
            "q": category,
            "key": api_key
        }

        # Send the request
        response = requests.get(url, params=params)

        # Parse the response
        data = response.json()

        # Loop over the videos
        for item in data["items"]:
            # Get the video ID
            video_id = item["id"]["videoId"]

            # Fetch the transcript
            try:
                transcript = YouTubeTranscriptApi.get_transcript(video_id)
                print(f'Transcript for video {video_id} in category {category}:')
                print(transcript)
                
                # Create a VideoData message
                video_data = video_data_pb2.VideoData()
                video_data.video_url = f'https://www.youtube.com/watch?v={video_id}'
                video_data.transcript = str(transcript)
                video_data.channel = item['snippet']['channelTitle']
                video_data.publication_date = item['snippet']['publishedAt']
                video_data.category = category

                # Serialize the message
                serialized_message = video_data.SerializeToString()
                
                print("Serialized message:", serialized_message)

                # Publish the message
                await nc.publish("youtube-news", serialized_message)
                
                print("PUBLISHED.")
                
                
            except Exception as e:
                print(f'Could not fetch transcript for video {video_id} in category {category}: {str(e)}')
    
    

asyncio.run(main())
