from django.contrib import admin
from blog.models import Post, Author, Article, ArticleComment

admin.site.register(Post)

admin.site.register(Author)

admin.site.register(Article)

admin.site.register(ArticleComment)