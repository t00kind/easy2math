from django.db import models

class Ll(models.Model):
    url = models.CharField(max_length=50, verbose_name="URl-адрес", null=True)
    level = models.ForeignKey('Level', null=True, on_delete=models.PROTECT, verbose_name="уровень подготовки")


    class Meta:
        verbose_name = "Уроки"
        verbose_name_plural = "Урок"
        ordering = ['level']


class Level(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="уровень подготовки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Классы"
        verbose_name_plural = "Класс"
        ordering = ['name']