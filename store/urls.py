
from django.db import router
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from . import views
from pprint import pprint


router=SimpleRouter()
router.register("products",views.ProductViewSet)
router.register("collection",views.CollectionViewSet)
pprint(router.urls)



urlpatterns=router.urls

# urlpatterns=[
#     path('',include(router.urls))
#     # path("products/",views.ProductList.as_view()),
#     # path("collection/",views.CollectionList.as_view()),

#     # path("products/<int:id>/",views.ProductDetails.as_view()),
#     # path('collection/<int:pk>/',views.CollectionDetail.as_view(),name="collection-detail")
# ]