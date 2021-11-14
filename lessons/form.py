from django.forms import ModelForm
from .models import Lessons

class LessonsForm(ModelForm):
    class Meta:
        model = Lessons
        fields = ('url', 'tag', 'level')