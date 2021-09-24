from .models import Todo
from django.http import request
from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer

# Create your views here.


@api_view(['GET'])
def index(request):
    data = {
        "list": "/task-list/",
        'detail-view': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'update': '/task-update/<str:pk>/',
        'delete': '/task-delete/<str:pk>/'

    }

    return Response(data)


@api_view(['GET'])
def taskList(request):
    tasks = Todo.objects.all()
    serializer = TodoSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    task = Todo.objects.get(id=pk)
    serializer = TodoSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):

    serializer = TodoSerializer(data=request.data, many=False)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Todo.objects.get(id=pk)

    serializer = TodoSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Todo.objects.get(id=pk)
    task.delete()

    return Response("Todo Deleted")
