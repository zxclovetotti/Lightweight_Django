# import os
import sys

from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES={
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    },
)

from django.conf.urls import url
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application

# view.py 
def index(request):
    return HttpResponse('Hello World')

# urls.py
urlpatterns = (
    url(r'^$', index),
)

# settings.py
# wsgi.py
# pip3 install gunicorn

application = get_wsgi_application()

# Django 1.11.2 using "__main__" instead of __main__''
if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
