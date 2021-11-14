# Generated by Django 3.2.7 on 2021-11-05 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_rename_mm_books'),
        ('tasks', '0002_auto_20211105_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='books.level'),
        ),
    ]