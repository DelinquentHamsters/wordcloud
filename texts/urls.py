from django.conf.urls import url

from . import views
#URLが無い場合には、index.htmlを読み込む
urlpatterns = [url(r'^$',views.index,name='index')] #viewsのindex関数を関連付け
