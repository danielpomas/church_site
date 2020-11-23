from django.urls import path

from .views import (
    ChurchesAdminListView,
    ChurchesAdminCreateView,
    ChurchesAdminUpdateView,
    AdminSpeakerListView,
    AdminSpeakersCreateView
)

app_name = 'churches'

urlpatterns = [
    path('manage/speakers/', AdminSpeakerListView.as_view(), name='admin-speakers-list'),
    path('manage/speakers/add/', AdminSpeakersCreateView.as_view(), name='admin-speakers-create'),
    path('manage/churches/', ChurchesAdminListView.as_view(), name='churches-admin-list'),
    path('manage/churches/add/', ChurchesAdminCreateView.as_view(), name='churches-admin-create'),
    path('manage/churches/<int:pk>/update/', ChurchesAdminUpdateView.as_view(), name='churches-admin-update'),
]
