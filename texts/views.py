import os
import sys

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from PIL import Image
import matplotlib.pyplot as plt
import numpy
from .models import Post

from .forms import inputForm

import MeCab
from .visualizewordcloud import create_wordcloud
from word_cloud.wordcloud import WordCloud

# Create your views here.
def index(request):
    
    #ファイルの削除を実施
    if os.path.exists("media/Picture/tmpPic.jpg")==True:
        os.remove("media/Picture/tmpPic.jpg")

    #return HttpResponse("Hello World! このページはインデックスです")
    #posts = Post.objects.order_by('-published')
    #form = inputForm()
    #return render(request,'texts/index.html',{'posts':posts})
    #return render(request,'texts/index.html',{'form':form,})
    txt_ = ""
    if request.method == "POST":
        form = inputForm(request.POST,request.FILES) #dataとfilesの両方を渡してフォーム作成      

        # POSTされた文字列
        txt_input = request.POST["text"]
        # アップロードされたテキストファイルの文字列
        #txt_ap = request.POST['file'].read()#.read()で読み込める
        #txt_ap = request.FILES["file"].read()

        txt_in =txt_input

        mecab = MeCab.Tagger("-Owakati")
        txt_ = mecab.parse(txt_in)
        img = create_wordcloud(txt_)#" ".join(g))#.decode('utf-8'))
        img.save('media/Picture/tmpPic.jpg',quality=95)

        contents = {
            'text': txt_,
            'form1': form,}

        return render(request,'texts/index.html',contents)
    else:
        form = inputForm()
        contents = {
            'form1':form,}
        return render(request,'texts/index.html',contents)

