from django.shortcuts import render
from django.contrib.auth.models import User
from dogmatics.models import Preprint,FormalPaper
from forum.models import Post
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def mypage(request):

    #ログインユーザー取得
    user = request.user

    #プレプリント取得
    preprints = Preprint.objects.filter(author=user)

    #journalの論文取得
    formal_papers = []
    for preprint in preprints:
        if FormalPaper.objects.filter(preprint=preprint):
            formal_papers.extend(FormalPaper.objects.filter(preprint=preprint))

    #forumへの投稿を取得
    posts = Post.objects.filter(owner=user).order_by('-created_at')[:10]

    
    for f in formal_papers:
        print(f.preprint.title)


    params = {
        'user' : user,
        'preprints' : preprints,
        'formal_papers'  : formal_papers,
        'posts' : posts,
    }

    
    return render(request, 'mypage/mypage.html', params)

def preprint_delete(request,preprint_id):
        
    if request.method == "POST":

        preprint = get_object_or_404(Preprint, id=preprint_id)
        preprint.delete()

        return redirect('mypage:mypage')
    
    return redirect('mypage:mypage')