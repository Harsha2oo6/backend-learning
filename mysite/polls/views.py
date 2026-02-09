import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Question

def hello_api(request):
    return JsonResponse({"message": "Hello API working"})


def get_questions(request):
    questions = Question.objects.all()

    data = []
    for q in questions:
        data.append({
            "id": q.id,
            "text": q.text,
            "created_at": q.created_at
        })

    return JsonResponse({"questions": data})


@csrf_exempt
def create_question(request):
    if request.method == "POST":
        body = json.loads(request.body)
        text = body.get("text")

        q = Question.objects.create(text=text)

        return JsonResponse({"id": q.id, "text": q.text})
