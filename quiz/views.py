from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

# Create your views here.
from .models import *


class QuizHome(ListView):
    model = Quiz
    template_name = 'index.html'
    context_object_name = 'quiz'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# class ShowQuiz(DetailView, FormView):
#     model = Quiz
#     template_name = 'quiz.html'
#     slug_url_kwarg = 'test_slug'
#     context_object_name = 'test'
#     success_url = reverse_lazy('home')

def show_quiz(request, test_slug):
    test = get_object_or_404(Quiz, slug=test_slug)
    questions = test.questions_set.all()
    if request.method == 'POST':
        right_answers = [q.answers_set.filter(is_right=1) for q in questions]
        right_answers = list(map(lambda x: str(list(x)[0]), right_answers))
        data = list(map(lambda x: str(x[0]), list(dict(request.POST).values())[1:]))
        count = {'result': sum(i[0] == i[1] for i in zip(right_answers, data)),
                 'quiz_length': len(questions),
                 }
        print(data, count)
        return render(request, 'result.html', context=count)

    answers = [q.answers_set.all() for q in questions]
    first_answers = list(map(lambda x: x[0], answers))
    q_and_a = list(zip(questions, answers, first_answers))

    context = {
        'q_and_a': q_and_a
    }
    return render(request, 'quiz.html', context=context)


def about(request):
    return render(request, 'about.html')






