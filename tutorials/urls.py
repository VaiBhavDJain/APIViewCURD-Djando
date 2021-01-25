from django.conf.urls import url
from tutorials import views
from django.urls import path
urlpatterns = [
    path('tutorial-detail/<pk>', views.tutorial_detail),
    path('tutorials-list/', views.tutorial_list),
    path('api/tutorials/published', views.tutorial_list_published)
]

