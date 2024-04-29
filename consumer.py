import os
import asyncio
from nats.aio.client import Client as NATS
import video_data_pb2  # Import the generated Protobuf code
from asgiref.sync import sync_to_async

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ninja_news.settings')
import django
django.setup()

from news_app.models import NewsVideo


async def main():
    nc = NATS()
    await nc.connect("localhost")
    js = nc.jetstream()
    
    # Define the callback function that will handle the messages
    async def message_handler(msg):
        print("Received a new message from the 'youtube-news' stream.")  # New print statement

        print("Raw data:", msg.data)
        # Deserialize the Protobuf message
        video_data = video_data_pb2.VideoData()
        video_data.ParseFromString(msg.data)

        # Print the video data
        print(f"Video URL: {video_data.video_url}")
        print(f"Transcript: {video_data.transcript}")
        print(f"Channel: {video_data.channel}")
        print(f"Publication Date: {video_data.publication_date}")
        print(f"Category: {video_data.category}")
        print("\n")
        
        await sync_to_async(NewsVideo.objects.create)(
            title=video_data.category,
            description=video_data.transcript,  # Assuming transcript is used as description
            duration=None,  # You might need to fetch this from somewhere else
            youtube_link=video_data.video_url,
        )
        # news_video.save()
        print("ADDED SUCCESSFULLY TO THE DATABASE.")

    # Subscribe to the "youtube-news" stream
    await js.subscribe("youtube-news", cb=message_handler)

    # Keep the event loop running
    while True:
        await asyncio.sleep(1)

asyncio.run(main())
