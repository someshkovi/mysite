import imp
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    highlighted = models.TextField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    headshot = models.ImageField(upload_to='author_headshots', blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(Author, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    website = models.URLField(blank=True, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    background_picture = models.ImageField(upload_to='blog_images', height_field=None, width_field=None, blank=True, null=True)


    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={
            'pk' : self.pk})

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    @property
    def number_of_comments(self):
        return ArticleComment.objects.filter(article_connected=self).count()

class ArticleComment(models.Model):
    article_connected = models.ForeignKey(
        Article, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.author) + ', ' + self.article_connected.title[:40]