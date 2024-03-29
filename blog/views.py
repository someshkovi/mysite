from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic

from blog.models import Post, Article, ArticleComment
from blog.forms import PostForm

class IndexView(generic.ListView):
    model = Article
    template_name = 'blog/index.html'

class DetailView(generic.DetailView):
    model = Article
    template_name = 'blog/article.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = ArticleComment.objects.filter(
            article_connected=self.get_object()).order_by('-date_posted')
        data['comments'] = comments_connected
        # if self.request.user.is_authenticated:
        #     data['comment_form'] = NewCommentForm(instance=self.request.user)

        return data

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }
    return render(request, 'blog/index.html', context)


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def about(request):
    context = {
    }
    return render(request, 'blog/about.html', context)