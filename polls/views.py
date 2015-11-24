from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import Http404
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Question, Choice

# generic view class
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
# non-generic view class
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = RequestContext(request, {
#         'latest_question_list': latest_question_list,
#     })
#     # Response:
#     # - full
#     # return HttpResponse(template.render(context))
#     # - shortcut
#     return render(request, 'polls/index.html', context)
#
#     # return HttpResponse("Hello, world. You're at the polls index.")

# generic view
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
# non-generic view
# def detail(request, question_id):
#
#     # Response:
#     # - full
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question': question})
#     #
#     # - shortcut
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#     # return HttpResponse("You're looking at question %s." % question_id)


# generic view
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
# non-generic view
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
#     # response = HttpResponse("You're looking at the results of question %s.")
#     # return HttpResponse(response % question_id)

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
    # return HttpResponse("You're voting on question %s." % question_id)
