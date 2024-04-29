from django.test import TestCase
from django.utils import timezone
from .models import NewsVideo
from datetime import datetime , timedelta
#upload_date = datetime.strptime('Apr 23, 2024', '%b %d, %Y')

class NewsTests(TestCase):
    def setUp(self):
        #upload_date = datetime.strptime('Apr 23, 2024', '%b %d, %Y')
        self.news = NewsVideo.objects.create(
            title="Testimony to continue in hush money trial of Former President Trump",
            description="Phil Taitt reports the details from Lower Manhattan.",
            #upload_date="upload_date",
            duration=timedelta(minutes=3),
            youtube_link="https://youtu.be/sm757r-pI-4?si=3PZs1HICs_6vaKY9",
        )

    def test_episode_content(self):
        self.assertEqual(self.news.title, "Testimony to continue in hush money trial of Former President Trump")
        #self.assertEqual(self.episode.link, "https://myawesomeshow.com")
        self.assertEqual(
            self.news.youtube_link, "https://youtu.be/sm757r-pI-4?si=3PZs1HICs_6vaKY9"
        )

    def test_news_str_representation(self):
        self.assertEqual(
            str(self.news), "Testimony to continue in hush money trial of Former President Trump"
        )