from rest_framework.response import Response
from rest_framework.decorators import api_view
from baseApp.models import Tools
from . serializer import ToolSerializer
from rest_framework import status


@api_view(['GET'])
def viewTools(request):
    tools = Tools.objects.all()
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addTools(request):
    serializer = ToolSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getTool(request, id):
    try:
        tool =Tools.objects.get(pk=id)
    except Tools.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ToolSerializer(tool)
        return Response(serializer.data)

@api_view(['PUT'])
def updateTool(request, id):
    try:
        tool = Tools.objects.get(pk=id)
    except Tools.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        serializer = ToolSerializer(tool)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteTool(request, id):
    try:
        tool = Tools.objects.get(pk=id)
    except Tools.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    tool.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)