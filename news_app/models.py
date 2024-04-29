from django.db import models

class NewsVideo(models.Model):
    title = models.CharField(max_length=200)
    #uploader = models.CharField(max_length=100)
    description = models.TextField()
    #upload_date = models.DateTimeField()
    duration = models.DurationField(null=True)
    #source = models.CharField(max_length=100)
    youtube_link = models.URLField(max_length=200)
    is_summarized = models.BooleanField(default=False)
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
