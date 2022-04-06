from django.urls import path
from blog import views
from django.contrib.auth.views import LogoutView

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('ov/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('article/<int:pk>/', views.DetailView.as_view(), name='article_detail'),
    path('list', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path("logout/", LogoutView.as_view(), name="logout"),
]
