from django.urls import path, include
from rest_framework import routers
from carrito import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductView, 'products')
router.register(r'tiendas', views.TiendaView, 'tiendas')
router.register(r'prices', views.PrecioView, 'prices')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/productsof/', views.ProductsOf.as_view(), name='productsof')
]