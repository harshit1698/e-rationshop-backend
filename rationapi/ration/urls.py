"""rationapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from ration import views
# from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('add-item-admin/',views.Global_Stock_API.as_view()),
    path('list-item-admin/',views.List_Stock.as_view()),
    path('update-item-admin/<int:id>',views.Global_Item_Update.as_view()),
    path('view-request/',views.New_Shop_Request.as_view()),
    path('all-shops/',views.All_Shop_Detail.as_view()),
    path('user-register/',views.UserAPIView.as_view()),
    path('update-shop-permission/',views.Update_Request.as_view()),
    path('blocked-shops/',views.Blocked_Shops.as_view()),
    path('year-list/',views.Year_API.as_view()),
    path('create-request/',views.Request_Create.as_view()),
    path('confirm-request/',views.Request_Accept_API.as_view()),
    path('send-mail/',views.Send_Mail.as_view()),
    path('new-requirement/<int:pin>/',views.Recruit_region.as_view()),
    path('new-region/',views.Recruit_region1.as_view()),
    path('view-new-recruit/',views.Open_Regions.as_view()),
    path('update-rating/',views.Update_Rating.as_view()),
    path('get-details/',views.Get_last_Ratings.as_view()),
    # path('admin/', admin.site.urls),
    # path('api/jwt/',obtain_jwt_token),
]
