from django.contrib import admin
from django.urls import path
from video_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.create_meeting, name='create_meeting'),
    path('join/<str:meeting_id>/', views.join_meeting, name='join_meeting'),
]
