from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.shortcuts import render

from .api import ProductSerializer
from .models import Product


from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )


###########
# APIView #
###########

class ProductListView(ListAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [AllowAny]



#################
# DetailAPIView #
#################

class ProductDetailAPIView(RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [AllowAny]
  lookup_field = 'id'



