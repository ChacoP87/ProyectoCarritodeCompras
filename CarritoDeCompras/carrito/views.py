from django.shortcuts import render

# Create your views here.'
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework import viewsets
from .serializer import ProductSerializer, TiendaSerializer, PrecioSerializer
from .models import Producto, Tienda, Precio

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Producto.objects.all()
    
class TiendaView(viewsets.ModelViewSet):
    serializer_class = TiendaSerializer
    queryset = Tienda.objects.all()

class PrecioView(viewsets.ModelViewSet):
    serializer_class = PrecioSerializer
    queryset = Precio.objects.all()

class ProductsOf(APIView):
    '''
    def get(self, request, tienda_id):
        try:
            productos = Producto.objects.filter(tienda_id=tienda_id)
            serializer = ProductSerializer(productos, many=True)
            return Response(serializer.data)
        except Producto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    '''
        
    def get(self, request):
        try:
            tienda_id = request.data['tienda_id']
            print('Tienda ID: ', tienda_id)
            try:
                productos = Producto.objects.filter(tienda_id=tienda_id)
                serializer = ProductSerializer(productos, many=True)
                return Response(serializer.data)
            except Producto.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
        except:
            return Response({'error':'No se ha encontrado tienda_id en la peticion'}, 
                            status= status.HTTP_400_BAD_REQUEST)