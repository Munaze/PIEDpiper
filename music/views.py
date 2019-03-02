
from django.http import HttpResponse, Http404
#from django.template import loader
from django.shortcuts import render , get_object_or_404
from .models import Album



def index(request):
    all_albums = list(Album.objects.all())
    return render(request, 'music/index.html',{ 'all_albums': all_albums,})
    #template = loader.get_template('music/index.html')
    #return HttpResponse(template.render(context, request))
   

def detail(request, album_id ):
    #return HttpResponse("<h1>Details for album id " + str(album_id) +  "</h1>")
    #try:
    #    album = Album.objects.get(pk=album_id)
    #except Album.DoesNotExist:
    #    raise Http404("album Does not exits")
    album = get_object_or_404(Album,pk =album_id ) 
    return render(request, 'music/detail.html',{ 'album': album,})
    #album = get_object_or_404(Album,pk =album_id )


def favorite(request ,album_id):
    album = get_object_or_404(Album,pk =album_id ) 
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError,Song.DoesNotExist):
        return render(request, 'music/detail.html',{'album':album , 'error_message': "you did not select any Valid Song" })
    else:
         if selected_song.is_favorite:
            selected_song.is_favorite = False
         else:
            selected_song.is_favorite = True
         selected_song.save()
         return render(request, 'music/detail.html', {'album': album})

    


#html =""
 #   for album in all_albums:
  #      url = '/music/' + str(album.id) + '/'
   #     html = '<a href = "' + url + '">' + album.album_title + '</a> <br>'