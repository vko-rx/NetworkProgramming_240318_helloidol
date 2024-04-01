from django.shortcuts import render

group = {
    'members': [
        {
            'group_name': 'MOOD',
            'name': '강신우',
            'img_src': 'https://pbs.twimg.com/media/GDP5hQNbQAARNaW.jpg',
        },
        {
            'group_name': 'MOOD',
            'name': '안진영',
            'img_src': 'https://pbs.twimg.com/media/F4XTxkIaEAANwdy.jpg',
        },
        {
            'group_name': 'MOOD',
            'name': '김유섭',
            'img_src': 'https://i.ytimg.com/vi/ovAhPsk_iNk/maxresdefault.jpg',
        },
        {
            'group_name': 'MOOD',
            'name': '김주한',
            'img_src': 'https://i.ytimg.com/vi/ovAhPsk_iNk/maxresdefault.jpg',
        },
    ]
}


# Create your views here.
def show_ksw(request):
    context = list(filter(lambda member: '강신우' in member['name'], group['members']))[0]
    # context = group['members'][0]
    return render(request, 'MOOD/member.html', context=context)
    # return render(request, 'MOOD/ksw.html')


def show_ajy(request):
    context = list(filter(lambda member: '안진영' in member['name'], group['members']))[0]
    # context = group['members'][1]
    return render(request, 'MOOD/member.html', context=context)
    # return render(request, 'MOOD/ajy.html')


def show_member(request, member_):
    context = list(filter(lambda member: member_ in member['name'], group['members']))[0]
    return render(request, 'MOOD/member.html', context=context)
