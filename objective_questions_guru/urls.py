"""objective_questions_guru URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from static_pages.views import about, contact
from questions import urls as qurls
from answers import urls as aurls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", aurls.answer, name="home"),
    path("answer/", include(aurls)),
    path("add/", include(qurls)),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
]
