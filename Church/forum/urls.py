from django.urls import path
from . import views
from .models import Book,Chapter,Verse

app_name = "bible_forum"

urlpatterns = [
    path('',views.book_list,name='book_list'),
    path("book",views.book,name="book"),
    path("book/forum",views.forum,name="forum"),
]

