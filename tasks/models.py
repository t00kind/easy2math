from django.db import models
from books.models import Level
from lessons.models import Tag

class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название", null=True)
    task = models.CharField(max_length=500, verbose_name="задача", null=True)
    level = models.ForeignKey(Level, on_delete=models.PROTECT, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, null=True)
    answer = models.ForeignKey("Answer", null=True, on_delete=models.PROTECT, verbose_name="ответ")


    class Meta:
        verbose_name = "Задачи"
        verbose_name_plural = "Задача"
        ordering = ['task']




class Tag(models.Model):
    name = models.CharField(max_length=100,verbose_name="tag")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Теги"
        verbose_name_plural = "Тег"
        ordering = ['name']


class Answer(models.Model):
    ans = models.CharField(max_length=150, verbose_name="ответ")

    def __str__(self):
        return self.ans

    class Meta:
        verbose_name = "Ответы"
        verbose_name_plural = "Ответ"
        ordering = ['ans']