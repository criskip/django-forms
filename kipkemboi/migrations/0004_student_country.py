# Generated by Django 4.1.7 on 2023-03-02 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kipkemboi', '0003_student_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='country',
            field=models.IntegerField(blank=True, default=6, max_length=50),
            preserve_default=False,
        ),
    ]
