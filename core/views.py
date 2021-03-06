from django.shortcuts import render, redirect

from core.models import Dork

google_url = 'https://www.google.com/search?q='

def index(request):
    dorks = Dork.objects.all()
    return render(request, 'index.html', {'dorks':dorks})

def get_query(request, selected_dork):
    dork = Dork.objects.get(id=selected_dork)
    return render(request, 'search.html', {'dork': dork})


def search(request, dork):

    if request.method ==  'GET':
        query = request.GET.get('query')
        new_url = str(str(google_url)+str(dork)+str(query)).replace('&', '%26')
        return redirect(new_url)
    redirect(index)

def search_music(request):
    if request.method ==  'POST':
        singer = request.POST.get('query-singer')
        music = request.POST.get('query-music')
        query = f'index of {str(singer)} type: mp3 intext: {str(music)}'
        new_url = str(google_url)+str(query)
        return redirect(new_url)
    return render(request, 'music.html')
