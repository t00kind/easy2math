from django.db import models
from books.models import Level

class Lessons(models.Model):
    url = models.CharField(max_length=50, verbose_name="URl-адрес", null=True)
    tag = models.ForeignKey("Tag", null=True, on_delete=models.PROTECT, verbose_name="Тег")
    level = models.ForeignKey(Level, on_delete=models.PROTECT, null=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="дата публикации", null=True)


    class Meta:
        verbose_name = "Уроки"
        verbose_name_plural = "Урок"
        ordering = ['-published']

class Tag(models.Model):
    tag = models.CharField(max_length=250, db_index=True, verbose_name="Тег") # in future rename this to "tag"

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = "Теги"
        verbose_name_plural = "Тег"