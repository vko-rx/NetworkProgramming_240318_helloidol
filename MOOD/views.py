from django.shortcuts import render

# Create your views here.
def show_ksw(request):
    context = {
        'group_name': 'MOOD',
        'name': '강신우',
        'img_src': 'https://pbs.twimg.com/media/GDP5hQNbQAARNaW.jpg',
    }
    # return render(request, 'MOOD/ksw.html')
    return render(request, 'MOOD/member.html', context = context)

def show_ajy(request):
    context = {
        'group_name': 'MOOD',
        'name': '안진영',
        'img_src': 'https://pbs.twimg.com/media/F4XTxkIaEAANwdy.jpg',
    }
    # return render(request, 'MOOD/ajy.html')
    return render(request, 'MOOD/member.html', context = context)