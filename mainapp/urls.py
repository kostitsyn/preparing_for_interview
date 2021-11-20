from django.urls import path
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.GoodsListView.as_view(), name='goods'),
]
