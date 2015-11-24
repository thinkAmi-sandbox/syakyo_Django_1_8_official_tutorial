from django.shortcuts import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404

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

    # Response:
    # - full
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
    #
    # - shortcut
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

    # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = HttpResponse("You're looking at the results of question %s.")
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
