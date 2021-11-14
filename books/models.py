from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    pdf = models.CharField(null=True, blank=True, verbose_name="pdf", max_length=50)
    fb2 = models.CharField(null=True, blank=True, verbose_name="fb2", max_length=50)
    epub = models.CharField(null=True, blank=True, verbose_name="epub", max_length=50)
    mobi = models.CharField(null=True, blank=True, verbose_name="mobi", max_length=50)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="дата публикации")
    level = models.ForeignKey('Level', null=True, on_delete=models.PROTECT, verbose_name="уровень подготовки")
    author = models.CharField(max_length=100, verbose_name="Автор", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Книги"
        verbose_name = "Книгy"
        ordering = ['-published']


class Level(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="уровень подготовки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Классы"
        verbose_name = "Класс"
        ordering = ['name']
