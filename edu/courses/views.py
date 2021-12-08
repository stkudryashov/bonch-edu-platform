from django.views.generic import ListView, CreateView
from django.http.response import HttpResponse

from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import Lesson
from users.models import User

from .forms import LessonForm


class IndexHtml(ListView):
    model = Lesson
    template_name = 'courses/views/index.html'


class ShowLessons(ListView):
    model = Lesson
    template_name = 'courses/views/lessons.html'
    context_object_name = 'lessons'


class ShowBackend(ShowLessons):
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        if self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)
            context['title'] = 'Backend'
            return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Lesson.objects.filter(is_approved=True)


class CreateLesson(CreateView):
    form_class = LessonForm
    template_name = 'courses/forms/add_lesson.html'
    success_url = reverse_lazy('backend')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Урок успешно отправлен на модерацию')
        return super(CreateLesson, self).form_valid(form)


class ShowOnApproval(ShowLessons):
    template_name = 'courses/admin/on_approval.html'
    context_object_name = 'lesson'

    def get_context_data(self, *, object_list=None, **kwargs):
        if self.request.user.is_staff:
            context = super().get_context_data(**kwargs)
            context['title'] = 'на одобрении'
            return context

    def get_queryset(self):
        if self.request.user.is_staff:
            approval_lessons = Lesson.objects.filter(is_approved=False, id_rejected=False)
            approval_lessons = approval_lessons.order_by('datetime')
            return approval_lessons.first()


def change_bookmarks(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(pk=request.user.pk)
        lesson_id = request.POST.get('lesson_id')
        lesson = Lesson.objects.get(pk=lesson_id)

        status = request.POST.get('status')
        if status == 'true':
            current_user.bookmarks.add(lesson_id)
        elif status == 'false':
            current_user.bookmarks.remove(lesson_id)

        lesson.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=401)


def approval_decide(request, lesson_pk, decide):
    if request.user.is_staff:
        lesson = Lesson.objects.get(pk=lesson_pk)
        if decide == 0:
            lesson.is_approved = True
            lesson.save()
        else:
            lesson.id_rejected = True
            lesson.save()
        return redirect('approval')
    else:
        return HttpResponse(status=401)
