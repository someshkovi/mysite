* pipenv shell
* django-admin startproject mysite .
* django-admin startapp polls
* python3 manage.py migrate
* python3 manage.py makemigrations polls
* python3 manage.py migrate polls
* python3 manage.py createsuperuser
* python3 manage.py test polls
* python3 -c "import django; print(django.__path__)"
* python3 manage.py collectstatic

* django-admin startapp blog

## for django-anywhere
* $ pa_autoconfigure_django.py --python=3.8 https://github.com/someshkovi/mysite.git--nuke                                         