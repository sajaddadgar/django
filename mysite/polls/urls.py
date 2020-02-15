from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # /polls/
    path('', views.IndexView.as_view(), name='index'),
    # /polls/5/
    path('<int:pk>/',views.DetailView.as_view(), name='detail'),
    # /polls/5/result
    path('<int:pk>/result/',views.ResultView.as_view(), name='result'),
    # /polls/5/vote/
    path('<int:question_id>/vote/',views.vote, name='vote'),

]