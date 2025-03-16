from django.shortcuts import render

def post_list(requset):
    return render(requset, 'blog/post_list.html', {})
