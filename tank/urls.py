from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tanks/', views.TankListView.as_view(), name="tanks"),
    path('tanks/<int:pk>', views.TankDetailView.as_view(), name='tanks_detail'),
    path('characteristics/', views.CharacteristicsListView.as_view(), name="characteristics"),
    path('characteristics/<int:pk>', views.CharacteristicsDetailView.as_view(), name='characteristics_detail'),

]