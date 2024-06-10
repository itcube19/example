from django.urls import path
from Calcualtions.views import *

urlpatterns = [
    path('user/', UserList.as_view()),
    path('user_view/<int:pk>/', UserDetail.as_view()),
    path('problem/', ProblemList.as_view()),
    path('problem_view/<int:pk>/', ProblemDetail.as_view()),
    path('training/', TrainingList.as_view()),
    path('training_view/<int:pk>/', TrainingDetail.as_view()),
    path('', index, name='index'),
    path('testlevel/', testLevel, name='testLevel'),
    path('diffsettings/', diffSettings, name='diffSettings'),
    path('generate/', generate_example, name='generate_example'),
    path('check_answer/', check_answer, name='check_answer'),
    path('registr/', show_registr, name='show_registr'),
]