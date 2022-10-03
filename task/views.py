from telnetlib import STATUS

from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import TaskSerializer
# Create your views here.

""
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/task-list/',
        'Detail View' : '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET','POST'])
def taskList(request):
    if request.method == 'GET':
        tasks = Task.objects.all().order_by('-create')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK )

    elif request.mehtod == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else :
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET','PUT','DELETE'])
def taskDetail(request, pk):
    try:
        task = Task.objects.get(id=  int(pk))
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        
    elif request.mehtod == 'DELETE':
        task.delete()
        return Response('Item succsesfully deleted!', status=status.HTTP_200_OK)    
    else :
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


