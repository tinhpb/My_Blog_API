from rest_framework import viewsets

from ..models import Category
from ..Serializers.category_serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()