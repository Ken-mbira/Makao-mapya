from django.urls import path

from house.api import views
urlpatterns = [
    path('',views.HouseList.as_view()),
    path('<int:pk>',views.HouseDetail.as_view()),
    path('country/',views.CountryList.as_view()),
    path('city/',views.CityList.as_view()),
    path('category/',views.CategoryList.as_view())
]