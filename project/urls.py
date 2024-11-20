from django.contrib import admin
from django.urls import path, include
from shop.views import CategoryViewset,ListProductsViewset
from rest_framework import routers



router =routers.SimpleRouter()
router.register('category',CategoryViewset,basename='category')
router.register('product',ListProductsViewset, basename='product')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/',include(router.urls)),
    # path('api/products/',ListProductsSerializerAPIview.as_view()),

]
