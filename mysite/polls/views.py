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

def update_question(request):
    body = json.loads(request.body)
    id = body.get("id")
    text = body.get("text")

    q = Question.objects.get(id=id)
    q.text = text
    q.save()
    return JsonResponse({"id": q.id, "text": q.text})

def delete_question(request):
    body = json.loads(request.body)
    id = body.get("id")
    q = Question.objects.get(id=id)
    q.delete()
    return JsonResponse({"message": "Question deleted"})

def create_question(request):
    body = json.loads(request.body)
    text = body.get("text")

    q = Question.objects.create(text=text)

    return JsonResponse({"id": q.id, "text": q.text})

@csrf_exempt
def question_operations(request):
    method = request.method
    match method:
        case "GET":
            return get_questions(request)
        case "POST":
            return create_question(request)
        case "PUT":
            return update_question(request)
        case "DELETE":
            return delete_question(request)
        case _:
            return JsonResponse({"error": "Method not allowed"}, status=405)