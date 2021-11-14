from django.shortcuts import render
from .models import Lessons, Tag
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from .form import LessonsForm


def index(request):
    sudo = Lessons.objects.all()
    tags = Tag.objects.all()
    title = "Уроки"
    context = {"sudo": sudo, "tags": tags, "title": title}
    return render(request, 'lessons/index.html', context)


def by_tag(request, tag_id):
    les = Lessons.objects.filter(tag=tag_id)
    tags = Tag.objects.all()
    current_tag = Tag.objects.get(tg=tag_id)
    context = {"les": les, "tags": tags, "current_tag": current_tag}
    return render(request, "lessons/by_tag.html", context)


class LesCreateView(CreateView):
    template_name = 'lessons/create.html'
    form_class = LessonsForm
    success_url = reverse_lazy('lessons')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
