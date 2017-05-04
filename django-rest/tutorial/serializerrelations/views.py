from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from serializerrelations.models import Album, Track
from serializerrelations.serializers import AlbumSerializer

@csrf_exempt
def album_list(request):
    """
    List all code albums, or create a new album.
    """
    if request.method == 'GET':
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AlbumSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def album_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        album = Album.objects.get(pk=pk)
    except Album.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AlbumSerializer(album)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AlbumSerializer(album, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        album.delete()
        return HttpResponse(status=204)