from django.urls import path
from account.api import views

urlpatterns = [
    path('auth/',views.AccountList.as_view()),
    path('auth/<int:pk>/',views.AccountDetail.as_view()),
]