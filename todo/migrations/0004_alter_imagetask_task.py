# Generated by Django 4.1.7 on 2023-03-16 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_imagetask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_task', to='todo.task'),
        ),
    ]
