from django.db.models import F
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse



# Create your views here.
def index(request):
    latestQuestionList = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    stuff_for_frontend = {
        'latest_question_list': latestQuestionList,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', stuff_for_frontend)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist!')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})


def result(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    stuff = {
        'question': question
    }
    return render(request, 'polls/result.html', stuff)


def vote(request, question_id):
    # return HttpResponse('you are in vote page in question: %s' % question_id)
    question = get_object_or_404(Question, pk =     question_id)
    stuff_for_frontend = {
        'question': question,
        'error_message': "You didn't select a choice.",
    }
    try:
        selectedChoice = question.choice_set.get(pk = request.POST['aaa'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', stuff_for_frontend)
    else:
        selectedChoice.votes += 1
        selectedChoice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))

def showDetail(request):
    latestQuestionList = Question.objects.order_by('-pub_date')[:5]
    output = ','.join([q.question_text for q in latestQuestionList])
    return HttpResponse(output)

