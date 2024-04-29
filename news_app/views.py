from django.shortcuts import render
from .models import NewsVideo
from .utils import get_summary  # or from .openai_utils import get_summary


# Create your views here.


def latest_videos(request):
    # Retrieve the latest videos from the database
    videos = NewsVideo.objects.order_by('-title')[:10]

    # Render the 'latest.html' template with the videos as context
    return render(request, '/home/mkatti/CS_482/ninja_news/news_app/templates/news_app/latest.html', {'videos': videos})


def summarize_view(request, video_id):
    # Retrieve the video by its ID
    video = NewsVideo.objects.get(id=video_id)

    # Retrieve the original transcript (description) and its summary
    transcript = video.description  # use 'description' instead of 'transcript'
    summary = get_summary(video.description)  # assuming 'summary' is a field in your model

    # Render the view
    return render(request, '/home/mkatti/CS_482/ninja_news/news_app/templates/news_app/summarize.html', {'transcript': transcript, 'summary': summary})
