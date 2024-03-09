"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from apps.resume import views as resume_view
from apps.company01 import views as company01_view
from apps.company02 import views as company02_view
from apps.datashow import views as data_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', resume_view.index, name="resume"),
                  path('datashow/', data_view.index, name="datashow"),
                  path('shanghaiqiluan/', company01_view.index, name="shanghaiqiluan"),
                  path('anhuirunchuang/', company02_view.index, name="anhuirunchuang"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
