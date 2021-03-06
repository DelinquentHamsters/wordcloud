"""wordcloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#from django.conf.urls import include, url
from django.conf.urls.static import static #必ずstaticの読み込みが先
from django.conf import settings #後に読み込む
from texts import views

urlpatterns = [
    path('texts/',include('texts.urls')), #texts階層のurlsを関連付け
    #path('texts/',views.index,name="index"),
    path('admin/', admin.site.urls),
    #path('texts/<int:post_id>/',views.post_detail,name="post_detail")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
