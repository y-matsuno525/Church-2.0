from django.shortcuts import render
from django.contrib.auth.models import User
from dogmatics.models import Preprint,FormalPaper
from forum.models import Post

def userpage(request, username):

    user = User.objects.filter(username=username).first()

    preprints = Preprint.objects.filter(author=user)

    formal_papers = []
    for preprint in preprints:
        if FormalPaper.objects.filter(preprint=preprint):
            formal_papers.extend(FormalPaper.objects.filter(preprint=preprint))

    posts = Post.objects.filter(owner=user).order_by('-created_at')[:10]
    


    params = {
        'user' : user,
        'preprints' : preprints,
        'formal_papers'  : formal_papers,
        'posts' : posts,
    }

    return render(request, 'userpage/userpage.html', params)

    