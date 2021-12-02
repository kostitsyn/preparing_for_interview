from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.GoodsListView.as_view(), name='goods'),
    path('catalog/<str:pk>/', mainapp.GoodsListByCatalog.as_view(), name='category'),
]
