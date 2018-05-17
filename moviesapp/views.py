from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from moviesapp.models import Movielist
from moviesapp.serializers import MovieSerializer


@csrf_exempt
def movie_list(request):
    """
    List all code moviesapp, or create a new moviesapp.
    """
    if request.method == 'GET':
        snippets = Movielist.objects.all()
        serializer = MovieSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def movie_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Movielist.objects.get(pk=pk)
    except Movielist.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MovieSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)