from django.urls import path
from main_app.views import *

urlpatterns = [
    path('user/', UserList.as_view()),
    path('user_view/<int:pk>/', UserDetail.as_view()),
    path('problem/', ProblemList.as_view()),
    path('problem_view/<int:pk>/', ProblemDetail.as_view()),
    path('training/', TrainingList.as_view()),
    path('training_view/<int:pk>/', TrainingDetail.as_view())
]