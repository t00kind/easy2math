from django.urls import path
from .views import index, by_tag, LesCreateView

urlpatterns = [
    path('', index, name="lessons"),
    path('<int:tag_id>/', by_tag),
    path('add/', LesCreateView.as_view(), name="add")
]