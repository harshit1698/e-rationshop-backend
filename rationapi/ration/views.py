from django.shortcuts import render
import base64
import random, json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from io import BytesIO
import json
# from Crypto.Cipher import AES
# from simplecrypt import encrypt, decrypt

import requests
from django.contrib.auth import get_user_model
from django.core import mail
from django.core.mail import send_mail, EmailMultiAlternatives

from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.utils.html import strip_tags
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import *
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated

# importing models
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# from rationapi.settings import BASE_URL
from ration.models import *
from datetime import datetime

# importing serializers
from ration.serializers.serializers import *

from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from datetime import datetime
from django.template.loader import render_to_string
import base64
import random, json
from rest_framework import status
import smtplib
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from django.utils.decorators import method_decorator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from io import BytesIO
from django.core import mail
from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import logout


# Create your views here.
# User = get_user_model()


class Global_Stock_API(CreateAPIView):
    # permission_classes=[]
    permission_classes = [IsAuthenticated]  # it will check if the user is authenticated or not
    authentication_classes = [JSONWebTokenAuthentication,SessionAuthentication]  # it will authenticate the person by JSON web token
    serializer_class = Global_item_Serializer
    queryset = Global_item_table.objects.all()


class List_Stock(ListAPIView):
    permission_classes = [IsAuthenticated]  # it will check if the user is authenticated or not
    authentication_classes = [JSONWebTokenAuthentication,SessionAuthentication]  # it will authenticate the person by JSON web token
    serializer_class = Global_item_Serializer
    # queryset = Global_item_table.objects.all(
    # )

    def get_queryset(self):
        qs=Global_item_table.objects.all()
        id=self.request.GET.get('id')
        name=self.request.GET.get('name')
        month=self.request.GET.get('month')
        year=self.request.GET.get('year')

        if month is not None and year is not None:
            m=int(month)
            y=int(year)

            history=History_table.objects.get(month=m,year=y)
            qs=Global_item_table.objects.filter(History_id=history)
            return qs
            
        if name is not None:
            qs=Global_item_table.objects.filter(Q(item_name=name))
        if id is not None:
            qs=Global_item_table.objects.filter(Q(id=id))
        return qs

class Global_Item_Update(UpdateAPIView,RetrieveAPIView):
    permission_classes = [IsAuthenticated]  # it will check if the user is authenticated or not
    authentication_classes = [JSONWebTokenAuthentication,SessionAuthentication]  # it will authenticate the person by JSON web token
    serializer_class = Global_item_Serializer
    queryset = Global_item_table.objects.all()
    lookup_field='id'


class New_Shop_Request(ListAPIView):
    permission_classes = [IsAuthenticated]  # it will check if the user is authenticated or not
    authentication_classes = [JSONWebTokenAuthentication,SessionAuthentication]  # it will authenticate the person by JSON web token
    serializer_class = Request_Create_Serializer
    # queryset = Global_item_table.objects.all(

    def get_queryset(self):
        qs=Request.objects.filter(is_reviewed=False)
        r_id=self.request.GET.get("id")
        if r_id is not None:
            region=Region_table.objects.get(pin=r_id)
            qs=Request.objects.filter(Q(is_reviewed=False) & Q(region_id=region)).order_by('qualification')
        return qs

class All_Shop_Detail(ListAPIView):
    permission_classes = [IsAuthenticated]  # it will check if the user is authenticated or not
    authentication_classes = [JSONWebTokenAuthentication,SessionAuthentication]  # it will authenticate the person by JSON web token
    serializer_class = Request_Serializer
    # queryset = Global_item_table.objects.all(

    def get_queryset(self):
        qs=Shop_table.objects.filter(Q(is_requested=False))
        return qs

# CreateAPIView for user registration
class UserAPIView(CreateAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class Update_Request(APIView):
    permission_classes = [IsAuthenticated]  # it will check if the user is authenticated or not
    authentication_classes = [JSONWebTokenAuthentication,SessionAuthentication]
    
    def get(self, request, *args, **kwargs):
        id1=request.GET.get('id')
        is_request=request.GET.get('req')
        print(id1)
        print(is_request)
        if is_request=="1":
            print(1)
            shop=Shop_table.objects.filter(id=id1)
            shop.update(is_requested=False)
            # shop.is_requested=False
            # shop.save()
        elif is_request=="2":
            print(2)
            shop=Shop_table.objects.filter(id=id1)
            shop.update(is_blocked=True,is_requested=False)
            # shop.is_blocked=True
            # shop.is_requested=False
            # shop.save()
        elif is_request=="3":
            shop=Shop_table.objects.filter(id=id1)
            shop.update(is_blocked=False,is_requested=False)
        return Response({"status":"Okay"},status=200)


class Blocked_Shops(ListAPIView):
    permission_classes = [IsAuthenticated]  # it will check if the user is authenticated or not
    authentication_classes = [JSONWebTokenAuthentication,SessionAuthentication]  # it will authenticate the person by JSON web token
    serializer_class = Request_Serializer
    queryset = Shop_table.objects.filter(is_blocked=True)  


class Year_API(ListAPIView):
    permission_classes = [IsAuthenticated]  # it will check if the user is authenticated or not
    authentication_classes = [JSONWebTokenAuthentication,SessionAuthentication]  # it will authenticate the person by JSON web token
    serializer_class = Year_Serializer
    queryset = History_table.objects.order_by().values('year').distinct()


class Request_Create(CreateAPIView):
    permission_classes=[]
    authentication_classes=[]
    serializer_class=Request_Create1_Serializer
    queryset=Request.objects.all()


class Request_Accept_API(APIView):
    permission_classes=[]
    authentication_classes=[]

    def post(self,request,*args,**kwargs):
        id=request.GET.get("id")
        req_obj=Request.objects.get(id=id)
        email=req_obj.email

        check_exist =User.objects.filter(email=email)

        u1=None

        name=req_obj.name.split(" ")

        if check_exist.count()>0:
            u1=check_exist.first()
            # pass
        else:
            u1=User.objects.create_user(username=email,email=email,first_name=name[0],last_name=name[1],password="eration12345")

        region_id=req_obj.region_id

        region_id.is_open=False
        region_id.save()

        disable_objs=Request.objects.filter(region_id=region_id)

        for obj in disable_objs:
            obj.is_reviewed=True
            obj.save()

        role=Role_table.objects.get(role_name="Shopkeeper")

        acc_user=Account_table.objects.create(auth_id=u1,role_id=role,contact=req_obj.contact_no)

        header={"Content-Type":"application/json"}
        data={"email":email,"pwd":"eration12345"}
        res=requests.post("http://127.0.0.1:8000/send-mail/",data=json.dumps(data),headers=header)


        shop=Shop_table.objects.create(shopkeeper_id=acc_user,region_id=region_id,noti_flag=False,address=req_obj.address,contact_no=req_obj.contact_no)


        return JsonResponse({"email":acc_user.id})


class ExememptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class Send_Mail(ExememptMixin, APIView):
    permission_classes=[]
    authentication_classes=[]

    def post(self,request,*args,**kwargs):
        stream = BytesIO(request.body)
        print(stream)
        data = JSONParser().parse(stream)
        # amount=data["amount"]
        email=data["email"]
        password=data["pwd"]
        from_email = settings.EMAIL_HOST_USER
        to = email
        subject = "Your Userid and password for E-RationShop "
        # html_message = render_to_string('email2.html',
                                        # context={'amount': amount,'month':mon})
        # plain_message = strip_tags(html_message)
        msg = "emai : "+email+" password : "+password+" \n Thank You"
        # send_mail(subject,msg,  from_email, [to],html_message=plain_message)
        msg = EmailMultiAlternatives(subject, msg, from_email, [to], bcc=[]) #plain
        # msg.attach_alternative(html_message, "text/html")
        msg.send()

        return JsonResponse({"status":"Done"})


class Recruit_region(UpdateAPIView,RetrieveAPIView,CreateAPIView):
    permission_classes=[]
    authentication_classes=[]
    serializer_class=Region_Serializer
    lookup_field="pin"
    queryset=Region_table.objects.all()

class Recruit_region1(CreateAPIView):
    permission_classes=[]
    authentication_classes=[]
    serializer_class=Region_Serializer
    # lookup_field="pin"
    queryset=Region_table.objects.all()

class Open_Regions(ListAPIView):
    permission_classes=[]
    authentication_classes=[]
    serializer_class=Region_Serializer

    def get_queryset(self):
        qs=Region_table.objects.filter(Q(is_open=True))
        return qs


class Update_Rating(APIView):
    permission_classes=[]
    authentication_classes=[]

    def put(self,request,*args,**kwrags):
        month=datetime.now().month
        year=datetime.now().year

        rating=float(request.GET.get("rating"))
        shop_id=int(request.GET.get("id"))

        history_id=History_table.objects.get(month=month,year=year)

        obj=Monthly_Rating.objects.filter(Q(history_id=history_id)&Q(shop_id=shop_id))

        monthly_obj=None
        exist=False

        if obj.count()>0:
            exist=True
            monthly_obj=obj.first()
            monthly_obj.rating=(rating+monthly_obj.rating)/2
            monthly_obj.save()
        else:
            monthly_obj=Monthly_Rating.objects.create(history_id=history_id,rating=rating,shop_id=shop_id)

        return JsonResponse({"rating":rating,"month":datetime.now().month,"year":datetime.now().year,"exist":exist})


class Get_last_Ratings(APIView):
    permission_classes=[]
    authentication_classes=[]

    def get(self,request,*args,**kwargs):

        list_shop=Shop_table.objects.filter(is_blocked=False)

        res={}
        count=0
        if list_shop.count()>0:
            for shop_obj in list_shop:
                obj=Monthly_Rating.objects.filter(Q(shop_id=shop_obj.id)).order_by('-history_id')
                if obj.count()>0:
                    rat=0
                    rat=obj[0].rating+obj[1].rating+obj[2].rating
                    rat=rat/3
                    if rat<3:
                        tmp={}
                        tmp["id"]=shop_obj.id
                        tmp["rating"]=rat
                        tmp["contact"]=shop_obj.contact_no
                        res["shop {}".format(count)]=tmp
                        count+=1
                        # res["id"]=shop_obj.id


                # print(obj[0].history_id)
                # print(obj[1].history_id)
                # obj.size()
                # for x in obj:

        return JsonResponse(res)








