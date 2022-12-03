from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Kimlik
from .serializers import KimlikSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
# Create your views here.



@api_view(['POST'])
def gonder(request):
    serializer = KimlikSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
@api_view(['GET'])
def veriler(request):
        snippets = Kimlik.objects.all()
        serializer = KimlikSerializer(snippets, many=True)
        return Response(serializer.data)
    
    
# @csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def detay(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Kimlik.objects.get(pk=pk)
    except Kimlik.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = KimlikSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = KimlikSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)