from django.urls import path, include
from .views import CategoryAPIView, AuthorAPIView, WebSiteAPIView, TelegramBotAPIView, FreeCodeAPIView, index, WebSiteDetailsAPIView, TelgrambotDetailsAPIView, freecodesDetailsAPIView
urlpatterns = [
    path("", index, name="index"),
    path("v1/category/", CategoryAPIView.as_view(), name="category"),
    path("v1/authors/", AuthorAPIView.as_view(), name="authors"),
    path("v1/websites/", WebSiteAPIView.as_view(), name="websites"),
    path("v1/websites/<int:pk>/", WebSiteDetailsAPIView.as_view(), name="websitesdetails"),
    path("v1/telegrambots/", TelegramBotAPIView.as_view(), name="telegrambots"),
    path("v1/telegrambots/<int:pk>/", TelgrambotDetailsAPIView.as_view(), name="telegrambotsdetails"),
    path("v1/freecodes/", FreeCodeAPIView.as_view(), name="freecodes"),
    path("v1/freecodes/<int:pk>/", freecodesDetailsAPIView.as_view(), name="freecodesdetails"),
]