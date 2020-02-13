from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # /polls/5/
    path('<int:question_id>/',views.detail, name='detail'),
    # /polls/5/result
    path('<int:question_id>/result/',views.result, name='result'),
    # /polls/5/vote/
    path('<int:question_id>/vote/',views.vote, name='vote'),
    # /polls/show/
    path('show/', views.showDetail, name='index'),

]