from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view

from rest_framework import status
from rest_framework.response import Response

from category.models import Category
from category.serializers import CategorySerializer
from category.tracking_service import get_all_children



def index(request):
    return render(request, 'index.html')


@api_view(['GET'])
def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.get_top_level_categories()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_create_subcategories(request, pk):
    parent = get_object_or_404(Category, id=pk)
    
    category_child_1, category_child_2,status = Category.objects.get_or_create_subcategories(parent)
    
    category_child_1_serializer = CategorySerializer(category_child_1)
    category_child_2_serializer = CategorySerializer(category_child_2)
    
    children = [category_child_1_serializer.data, category_child_2_serializer.data]
    return Response({'data': children}, status=status)

@api_view(['GET'])
def get_children_by_id(request, pk):
    children = get_all_children(pk)
    
    return Response({'data': children}, status=status.HTTP_200_OK)