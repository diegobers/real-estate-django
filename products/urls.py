from django.urls import path

from . import views


urlpatterns = [  
    path('', views.CasaListView.as_view(), name='catalogue'),
    path('detalhes/<int:pk>/', views.CasaDetailView.as_view(), name='casa-detail'),
    #path('pesquisa', views.ProductSearchView, name='search'),
]