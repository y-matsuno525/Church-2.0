from django.shortcuts import render

#メニューを表示するだけ
def index(request):

    return render(request,'menu/index.html')

