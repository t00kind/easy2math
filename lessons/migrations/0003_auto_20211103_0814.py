# Generated by Django 3.2.7 on 2021-11-03 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_auto_20211102_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(db_index=True, max_length=250, verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Теги',
                'verbose_name_plural': 'Тег',
            },
        ),
        migrations.AlterModelOptions(
            name='lessons',
            options={'ordering': ['tag'], 'verbose_name': 'Уроки', 'verbose_name_plural': 'Урок'},
        ),
        migrations.RemoveField(
            model_name='lessons',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='lessons',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lessons.tag', verbose_name='Тег'),
        ),
    ]