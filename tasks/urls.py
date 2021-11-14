from django.urls import path
from .views import get, by_tag

urlpatterns = [
    path('', get, name="tasks"),
    path('<int:tag_id>/', by_tag)
]