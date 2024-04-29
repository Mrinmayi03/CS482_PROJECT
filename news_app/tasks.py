from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import NewsVideo  # assuming you have a model named Transcript
import openai  # make sure to install the openai python package

openai.api_key = 'sk-proj-8tpxDprsPvkfV3JGBl0iT3BlbkFJ2Oxg45xOkd0Xl7Byxorx'

@shared_task
def check_for_new_summaries():
    # Get all transcripts that have not yet been summarized
    transcripts_to_summarize = NewsVideo.objects.filter(is_summarized=False)

    for transcript in transcripts_to_summarize:
        # Call the OpenAI API to generate a summary
        response = openai.Completion.create(
          engine="text-davinci-002",
          prompt=transcript.title,
          temperature=0.3,
          max_tokens=60
        )

        # Store the summary in your database and mark the transcript as summarized
        transcript.summary = response.choices[0].text.strip()
        transcript.is_summarized = True
        transcript.save()
