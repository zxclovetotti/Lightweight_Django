import os
import sys

# view.py 
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World')

# urls.py
from django.conf.urls import url

urlpatterns = (
    url(r'^$', index),
)

# settings.py
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

# Django 1.11.2 using "__main__" instead of __main__''
if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
