"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import RecyclableItemView, RecyclingHistoryView, RecyclingTransactionView, RVMView
from account.views import registration_view, qrcode_authentication_view, test_permission_view, generate_qrcode_view
from rest_framework.authtoken.views import obtain_auth_token
from account.views import CustomObtainAuthToken

urlpatterns = [
    path('https://rvm-production.up.railway.app/rvm/api/register', registration_view),
    path('rvm/api/login', CustomObtainAuthToken.as_view()),
    path('https://rvm-production.up.railway.app/rvm/api/qrcode-auth', qrcode_authentication_view),
    path('https://rvm-production.up.railway.app/rvm/api/qrcode-generate', generate_qrcode_view),
    path('https://rvm-production.up.railway.app/rvm/api/test-permission', test_permission_view),

    path('https://rvm-production.up.railway.app/admin', admin.site.urls),
    path('https://rvm-production.up.railway.app/rvm/api/recyclableItem', RecyclableItemView.getAll),
    path('https://rvm-production.up.railway.app/rvm/api/recyclableItem/add', RecyclableItemView.addRecyclableItem),
    path('https://rvm-production.up.railway.app/rvm/api/recyclableItem/<int:id>', RecyclableItemView.getRecyclableItemById),
    path('https://rvm-production.up.railway.app/rvm/api/recyclableItem/update/<int:id>', RecyclableItemView.updateRecyclableItem),
    path('https://rvm-production.up.railway.app/rvm/api/recyclableItem/delete/<int:id>', RecyclableItemView.deleteRecyclableItem),

    path('https://rvm-production.up.railway.app/rvm/api/recyclingHistory', RecyclingHistoryView.getAll),
    path('https://rvm-production.up.railway.app/rvm/api/recyclingHistory/add', RecyclingHistoryView.addRecyclingHistory),
    path('https://rvm-production.up.railway.app/rvm/api/recyclingHistory/<int:id>', RecyclingHistoryView.getRecyclingHistoryById),
    path('https://rvm-production.up.railway.app/rvm/api/recyclingHistory/update/<int:id>', RecyclingHistoryView.updateRecyclingHistory),
    path('https://rvm-production.up.railway.app/rvm/api/recyclingHistory/delete/<int:id>', RecyclingHistoryView.deleteRecyclingHistory),

    path('https://rvm-production.up.railway.app/rvm/api/recyclingTransaction', RecyclingTransactionView.getAll),
    path('https://rvm-production.up.railway.app/rvm/api/recyclingTransaction/add', RecyclingTransactionView.addRecyclingTransaction),
    path('https://rvm-production.up.railway.app/rvm/api/recyclingTransaction/<int:id>', RecyclingTransactionView.getRecyclingTransactionById),
    path('https://rvm-production.up.railway.app/rvm/api/recyclingTransaction/update/<int:id>', RecyclingTransactionView.updateRecyclingTransaction),
    path('https://rvm-production.up.railway.app/rvm/api/recyclingTransaction/delete/<int:id>', RecyclingTransactionView.deleteRecyclingTransaction),

    path('https://rvm-production.up.railway.app/rvm/api/rvm', RVMView.getAll),
    path('https://rvm-production.up.railway.app/rvm/api/rvm/add', RVMView.addRVM),
    path('https://rvm-production.up.railway.app/rvm/api/rvm/<int:id>', RVMView.getRVMById),
    path('https://rvm-production.up.railway.app/rvm/api/rvm/update/<int:id>', RVMView.updateRVM),
    path('https://rvm-production.up.railway.app/rvm/api/rvm/delete/<int:id>', RVMView.deleteRVM),
]
