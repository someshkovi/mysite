# Generated by Django 4.0.3 on 2022-04-06 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_article_created_date_article_published_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='background_picture',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images'),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author'),
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('article_connected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
