"""cricketproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from cricketapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('team_api/<int:id>/',views.TeamDetailsCBV.as_view()),
    path('team_api/',views.TeamListCBV.as_view()),

    path('player_api/<int:id>/',views.PlayerDetailsCBV.as_view()),
    path('player_api/',views.PlayerListCBV.as_view()),

    path('match_api/<int:id>/',views.MatchDetailsCBV.as_view()),
    path('match_api/',views.MatchListCBV.as_view()),

    path('points_api/<int:id>/',views.PointsDetailsCBV.as_view()),
    path('points_api/',views.PointsListCBV.as_view()),
]
