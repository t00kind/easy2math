from django.db import models

class Mm(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    content = models.TextField(null=True, blank=True, verbose_name="суть")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="дата публикации")

    class Meta:
        verbose_name_plural = "Публикации"
        verbose_name = "Публикация"
        ordering = ['-published']