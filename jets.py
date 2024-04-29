from nats.aio.client import Client as NATS

async def main():
    # Connect to NATS
    nc = NATS()
    await nc.connect("localhost")
    print("Connected to NATS.")

    # Connect to JetStream
    js = nc.jetstream()
    print("Connected to JetStream.")
    
    stream_name = "youtube-news"
    await js.add_stream(name="youtube-news", subjects=["youtube-news"])
    print(f"Stream '{stream_name}' has been created.")

# Run the main function
import asyncio
asyncio.run(main())
