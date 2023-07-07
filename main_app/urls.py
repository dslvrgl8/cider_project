from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"), # <- new route
    path('ciders/', views.CiderList.as_view(), name="cider_list"),
    path('ciders/new/', views.CiderCreate.as_view(), name="cider_create"),
    path('ciders/<int:pk>/', views.CiderDetail.as_view(), name="cider_detail"),
    path('ciders/<int:pk>/update',views.CiderUpdate.as_view(), name="cider_update"),
    path('ciders/<int:pk>/delete',views.CiderDelete.as_view(), name="cider_delete"),
    path('ciders/<int:pk>/flavors/new/', views.FlavorCreate.as_view(), name="flavor_create"),
     path('favorites/<int:pk>/flavors/<int:flavor_pk>/', views.FavoriteFlavorAssoc.as_view(), name="favorite_flavor_assoc"),
]

