# Generated by Django 2.1.2 on 2018-11-11 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='similar_books',
            field=models.ManyToManyField(to='core.Book', blank=True),
        ),
    ]