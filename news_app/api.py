from ninja import NinjaAPI , Router
from django.http import JsonResponse
import openai 

api = NinjaAPI()
openai.api_key = 'sk-proj-8tpxDprsPvkfV3JGBl0iT3BlbkFJ2Oxg45xOkd0Xl7Byxorx'

from .tasks import check_for_new_summaries  # import the Celery task

@api.post("/summarize")
def summarize(request):
    # Trigger the Celery task
    check_for_new_summaries.delay()
    return {"message": "Summarization started"}


router = Router()

@router.get("/chat")
def chat_endpoint(request, query: str):
    # Use the OpenAI API to answer the natural language query
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=query,
        max_tokens=150
    )

    # Extract the generated text from the response
    generated_text = response.choices[0].text.strip()

    # Return the generated text as a JSON response
    return JsonResponse({"response": generated_text})

api.add_router("/chat", router)