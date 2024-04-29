import openai

openai.api_key = 'sk-proj-8tpxDprsPvkfV3JGBl0iT3BlbkFJ2Oxg45xOkd0Xl7Byxorx'

def get_summary(transcript):
    response = openai.Completion.create(
      engine="gpt-3.5-turbo-instruct",
      prompt=transcript,
      temperature=0.3,
      max_tokens=100
    )

    summary = response.choices[0].text.strip()
    return summary
