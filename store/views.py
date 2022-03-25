
import django
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from numpy import product
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from .models import Collection, OrderItem, Product, Reviews
from .serializer import CollectionSerializer, ProductSerializer, ReviewSerializer
from rest_framework import status
from django.db.models import Count
from rest_framework.views import APIView
from store import serializer
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field="id"

    def get_serializer_context(self):
        return {"request":self.request}


    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['id']).count()>0:
            return Response({"error": "Product cannot be deleted"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)


class CollectionViewSet(ModelViewSet):
    queryset=querset=Collection.objects.annotate(products_count=Count('products')).all()
    serializer_class=CollectionSerializer

    def delete(self,request,pk):
        collection=get_object_or_404(Collection,pk=pk)
        if collection.products.count()>0:
            return Response({"error":"Collection cannot be deleted"},status=status.HTTP_400_BAD_REQUEST)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewViewSet(ModelViewSet):
    queryset=Reviews.objects.all()
    serializer_class=ReviewSerializer

# class ProductList(ListCreateAPIView):

    

#     # def get_queryset(self):
#     #     return Product.objects.select_related('collection').all()

#     # def get_serializer_class(self):
#     #     return ProductSerializer

#     def get_serializer_context(self):
#         return {"request":self.request}


#     # def get(self,request):
#     #     queryset=Product.objects.select_related('collection').all()
#     #     serializer=ProductSerializer(queryset,many=True,context={"request":request})
#     #     return Response(serializer.data)

#     # def post(self,request):
#     #     serializer=ProductSerializer(data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save()
        
#     #     return Response('ok')

# class ProductDetails(RetrieveUpdateDestroyAPIView):
#     queryset= Product.objects.all()
#     serializer_class=ProductSerializer
#     lookup_field="id"

#     def delete(self,request,id):
#         product=get_object_or_404(Product,pk=id)
#         if product.orderitems.count()>0:
#             return Response({"error": "Product cannot be deleted"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

    # def get(self,request,id):
    #    product=get_object_or_404(Product,pk=id)
    #    serializer=ProductSerializer(product)
    #    return Response(serializer.data)


    # def put(self,request,id):
    #     product = get_object_or_404(Product,pk=id)
    #     serializer=ProductSerializer(product,data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response('ok')

    



# @api_view(['GET','POST','DELETE'])
# def products_list(request):
#     product=get_object_or_404(Product,pk=id)
#     if request.method  == 'GET':

#         queryset=Product.objects.select_related('collection').all()
#         serializer=ProductSerializer(queryset,many=True,context={"request":request})

#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer=ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
        
#         return Response('ok')

#     elif request.method  == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET','POST','DELETE'])
# def product_details(request,id):
  
#     product=get_object_or_404(Product,pk=id)
#     if request.method  == 'GET':

#         queryset=Product.objects.select_related('collection').all()
#         serializer=ProductSerializer(queryset,many=True,context={"request":request})

#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer=ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
        
#         return Response('ok')

#     elif request.method  == 'DELETE':
#         if product.orderitems.count()>0:
#             return Response({"error":"Product cannot be deleted "},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# class CollectionList(ListCreateAPIView):
#     queryset=querset=Collection.objects.annotate(products_count=Count('products')).all()
#     serializer_class=CollectionSerializer

   


# @api_view(['GET',"POST"])
# def collection_list(request):
#     if request.method == "GET":
#         querset=Collection.objects.annotate(products_count=Count('products')).all()
#         serializer=CollectionSerializer(querset,many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer=CollectionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)



# class CollectionDetail(RetrieveUpdateDestroyAPIView):
#     queryset=Collection.objects.annotate(products_count=Count('products'))

#     serializer_class=CollectionSerializer

#     def delete(self,request,pk):
#         collection=get_object_or_404(Collection,pk=pk)
#         if collection.products.count()>0:
#             return Response({"error":"Collection cannot be deleted"},status=status.HTTP_400_BAD_REQUEST)
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # @api_view(['GET',"POST",'DELETE'])
# # def collection_detail(request,pk):
# #     collection=get_object_or_404(
# #         Collection.objects.annotate(
#             products_count=Count('products')
#         ),pk=pk
#     ),
#     if request.method =="GET":
#         serializer=CollectionSerializer(collection)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer=CollectionSerializer(collection,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         if collection.products.count >0:
#             return Response({"error":"Cannot delete selected collection"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

