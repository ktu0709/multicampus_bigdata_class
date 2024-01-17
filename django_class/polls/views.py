from django.shortcuts import render,redirect,get_object_or_404 #response의 응답페이지 함수
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect #응답페이지의 형식
from .models import Question ,Choice

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index02(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def my_render_view(request): #render/
    #계산용 비즈니스 로직 추가
    context = {"a":1,"b":2}
    return render(request,"my_template.html",context)

def my_redirect_view(request): #redirect/
    return redirect("my_render_view")

def my_json(request):
    data = {"a":1,"b":2}
    return JsonResponse(data)


def myexam(request):
    return render(request, "my_exam.html")

def myfor(request):
    my_list =[1,2,3,4,5,6,7,8]
    context = {'list_item':my_list}
    return render(request, "my_for.html", context)

#tutorial
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
