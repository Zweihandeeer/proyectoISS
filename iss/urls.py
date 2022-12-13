from django.contrib import admin
from django.urls import path
from iss.views import home, login, nuevas_observaciones, observaciones, coach, player, cmatchup, coachview2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name="home"),
    path('login/', login, name="login"),
    path('coach/', coach, name="coach"),
    path('player/', player, name="player"),
    path('coachmatchup/', cmatchup, name="matchup"),
    path('coachobservaciones/', nuevas_observaciones, name="coachobservaciones"),
    path('observaciones/', observaciones, name="observaciones"),
    path('coachview2/', coachview2, name="coachview2"),
]
