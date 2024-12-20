from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('home/', login_required(Home), name='home'),

    path('list_academy/', login_required(AcademyList.as_view()), name='list-academy'),
    path('create_academy/', login_required(AcademyCreate.as_view()), name='create-academy'),
    path('edit_academy/<int:pk>', login_required(AcademyUpdate.as_view()), name='edit-academy'),
    path('delete_academy/<int:pk>', login_required(AcademyDelete.as_view()), name='delete-academy'),

    path('list_lesson/', login_required(LessonList.as_view()), name='list-lesson'),
    path('create_lesson/', login_required(LessonCreate.as_view()), name='create-lesson'),
    path('edit_lesson/<int:pk>', login_required(LessonUpdate.as_view()), name='edit-lesson'),
    path('delete_lesson/<int:pk>', login_required(LessonDelete.as_view()), name='delete-lesson'),

    # path('admin_teacher/', login_required(), name='teacher'),
    # path('admin_offer/', login_required(), name='offer'),
]

urlpatterns += [
    path('academy/', login_required(TemplateView.as_view(template_name='administration/about_us.html')), name='academy'),
    path('admin_lesson/', login_required(TemplateView.as_view(template_name='administration/lesson.html')), name='admin-lesson'),


]
