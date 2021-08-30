from django.db import models

class Tt(models.Model):
    task = models.CharField(max_length=500, verbose_name="задача", null=True)
    level = models.ForeignKey('Level', null=True, on_delete=models.PROTECT, verbose_name="уровень подготовки")
    # answer = models.ForeignKey('Answer', null=True, on_delete=models.PROTECT, verbose_name="ответ")


    class Meta:
        verbose_name = "Задачи"
        verbose_name_plural = "Задача"
        ordering = ['level']


class Level(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="уровень подготовки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Классы"
        verbose_name_plural = "Класс"
        ordering = ['name']

# class Answer(models.Model):
#         my = models.CharField(max_length=300, db_index=True, verbose_name="Ответ")
#
#         def __str__(self):
#             return self.my
#
#         class Meta:
#             verbose_name = "Ответы"
#             verbose_name_plural = "Ответ"
#             ordering = ['name']
