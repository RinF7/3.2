# Generated by Django 5.1.3 on 2024-12-09 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Publishers',
            },
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['publication_date'], 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='library.author'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='book_list', to='library.publisher'),
        ),
    ]