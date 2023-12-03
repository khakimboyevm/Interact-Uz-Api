from rest_framework.request import Request
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse


def index(request: HttpResponse):
      response_index = '<center><b>Barcha Api Manzillari</b></center><br><center><a href="v1/category/">Category</a></center><br><center><a href="v1/authors/">Authors</a></center><br><center><a href="v1/websites/">Websites</a></center><br><center><a href="v1/telegrambots/">Telegrambots</a></center><br><center><a href="v1/freecodes/">Freecodes</a></center><br><br><center><a href="interactadmin/">Admin Panel</a></center><br><br><center>Login: interactadmin<br>password: interactadmin</center><br><center>Admin panelden royhatdan otilmasa apilani gorib bolmidi</center>'
      return HttpResponse(response_index)

class CategoryAPIView(APIView):
    def get(self, request: Request):
            category = Category.objects.all().values()
            return Response(data={"category": category})
    
class AuthorAPIView(APIView):
    def get(self, request: Request):
            authors = Authors.objects.all().values()
            return Response(data={"authors": authors})
    
class WebSiteDetailsAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, Request, pk):
        try:
            web_site = Web_sites.objects.get(pk=pk)
            return Response(data={"web_site": {
                "id":web_site.id,
                "name": web_site.name,
                "slug":web_site.slug,
                "type_catg_id": web_site.type_catg.name,
                "author_id": web_site.author.name,
                "about_item": web_site.about_item,
                "image": web_site.image.url if web_site.image else None,
                "screen1": web_site.screen1.url if web_site.screen1 else None,
                "screen2": web_site.screen2.url if web_site.screen2 else None,
                "screen3": web_site.screen3.url if web_site.screen3 else None,
                "price_type": web_site.price_type,
                "link": web_site.link,
                "price": web_site.price

            }})
        except Web_sites.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class WebSiteAPIView(APIView):
    def get(self, request: Request):
            web_sites = Web_sites.objects.all().order_by("-id").values()
            return Response(data={"website": web_sites})
    

class TelgrambotDetailsAPIView(APIView):
    def get(self, request, pk):
        try:
            telegrambot = telegram_bot.objects.get(pk=pk)

            # Accessing related model attributes
            type_catg_name = telegrambot.type_catg.name if telegrambot.type_catg else None
            author_name = telegrambot.author.name if telegrambot.author else None

            return Response(data={
                "telegrambot": {
                    "id": telegrambot.id,
                    "name": telegrambot.name,
                    "slug": telegrambot.slug,
                    "type_catg_id": type_catg_name,
                    "author_id": author_name,
                    "about_item": telegrambot.about_item,
                    "image": telegrambot.image.url if telegrambot.image else None,
                    "screen1": telegrambot.screen1.url if telegrambot.screen1 else None,
                    "screen2": telegrambot.screen2.url if telegrambot.screen2 else None,
                    "screen3": telegrambot.screen3.url if telegrambot.screen3 else None,
                    "price_type": telegrambot.price_type,
                    "link": telegrambot.link,
                    "price": telegrambot.price
                }
            })
        except telegram_bot.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class TelegramBotAPIView(APIView):
    def get(self, request: Request):
            telegram_bots = telegram_bot.objects.all().order_by("-id").values()
            return Response(data={"telegrambots": telegram_bots})
    
class freecodesDetailsAPIView(APIView):
    def get(self, request, pk):
        try:
            freecode = free_codes.objects.get(pk=pk)

            # Accessing related model attributes
            type_catg_name = freecode.type_catg.name if freecode.type_catg else None
            author_name = freecode.author.name if freecode.author else None

            return Response(data={
                "telegrambot": {
                    "id": freecode.id,
                    "name": freecode.name,
                    "slug": freecode.slug,
                    "type_catg_id": type_catg_name,
                    "author_id": author_name,
                    "about_item": freecode.about_item,
                    "image": freecode.image.url if freecode.image else None,
                }
            })
        except free_codes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class FreeCodeAPIView(APIView):
    def get(self, request: Request):
            free_code = free_codes.objects.all().order_by("-id").values()
            return Response(data={"freecodes": free_code})