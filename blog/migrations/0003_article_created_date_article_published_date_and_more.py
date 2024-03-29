# Generated by Django 4.0.3 on 2022-04-06 08:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='article',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.TextField(default='sample text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='headshot',
            field=models.ImageField(blank=True, null=True, upload_to='author_headshots'),
        ),
        migrations.AlterField(
            model_name='author',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
