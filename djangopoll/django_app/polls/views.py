from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    # return HttpResponse(template.render(request,context=context))
    return render(request, 'polls/index.html',context=context)


def detail(request, question_id):
    return HttpResponse('너는 질문을 보고 있다 $s.' % question_id)

def results(request, question_id):
    response = '너는 질문의 결과를 보고 있다. %s.'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('너는 질문에 대한 투표를 하고 있다 $s.'% question_id)