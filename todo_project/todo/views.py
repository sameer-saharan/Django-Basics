from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['POST'])
def create_task(request): 
    serializer = TaskSerializer(data=request.data)

    if not serializer.is_valid(): 
        return Response({'status': 403, 'message': 'Something went wrong'})

    serializer.save()
    return Response({'status': 200, 'data': serializer.data})

@api_view(['GET'])
def view_task(request): 
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response({'status': 200, 'tasks': serializer.data})

@api_view(['PUT'])
def edit_task(request, id): 
    try: 
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist: 
        return Response({'status': 403, 'message': "Task doesn't exist"})
    
    serializer = TaskSerializer(task, data=request.data)
    if not serializer.is_valid(): 
        return Response({'status': 403, 'message': "Serializer is not valid"})
    
    serializer.save()
    return Response({'status': 200, 'task': serializer.data})

@api_view(['DELETE'])
def delete_task(request, id): 
    try: 
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist(): 
        return Response({'status': 403, 'message': "Task doesn't exist"})
    
    task.delete()
    return Response({'status': 204, 'message': "Task Deleted Successfully"})