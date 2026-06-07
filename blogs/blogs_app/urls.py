"""Defines URL patterns for blogs_aps."""

from django.urls import path

from .import views

app_name = 'blogs_app'
urlpatterns = [
    # Home page
    path('',views.index, name='index'),
    # Page that shows all topics.
    path('topics/',views.topics, name='topics'),
    # Detail page for the single topic.
    path('topic/<int:topic_id>/', views.topic, name='topic'),
]