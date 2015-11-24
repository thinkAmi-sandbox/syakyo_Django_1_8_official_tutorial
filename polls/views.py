from django.shortcuts import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    # Response:
    # - full
    # return HttpResponse(template.render(context))
    # - shortcut
    return render(request, 'polls/index.html', context)

    # return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = HttpResponse("You're looking at the results of question %s.")
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
