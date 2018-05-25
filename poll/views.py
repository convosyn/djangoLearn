from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *
# Create your views here.

def index(request):
    respoList = Question.objects.order_by('-pub_date')[:5]
    context = {'question_list': respoList}
    return render(request, 'poll/index.html', context)

def  detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #response = "You're looking at question {!s}".format(question_id)
    context = {"question" : question}
    return render(request, 'poll/detail.html', context)

def results(request, question_id):
    return HttpResponse("You are looking at the results of question {!s}".format(question_id))

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "you didn't select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))

