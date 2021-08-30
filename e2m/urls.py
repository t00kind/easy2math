from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('lessons/', include('lessons.urls')),
    path('', include('main.urls')),
    path('tasks/', include('tasks.urls')),
    path('books/', include('books.urls')),
    path('admin/', admin.site.urls)

]
