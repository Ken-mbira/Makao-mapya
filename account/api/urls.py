from django.urls import path
from account.api import views

urlpatterns = [
    path('',views.AccountList.as_view()),
    path('<int:pk>',views.AccountDetail.as_view())
]