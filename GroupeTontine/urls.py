from django.urls import path
from .views import Profil, gerer_paiment, home, about, Liste_groupe, groupe_detail,new_groupe, Mes_groupe, gerer_groupe, participer

urlpatterns = [
    path("", home, name="index"),
    path("about/", about, name="about"),
    path("groupes/", Liste_groupe, name="groupe"),
    path("groupes/new", new_groupe, name="new_groupe"),
    path("groupes/mes", Mes_groupe, name="mesgroupe"),
    path("groupes/<int:id>/", groupe_detail, name="detail"),
    path("groupes/mes<int:id>/", gerer_groupe, name="gerer"),    
    path("groupes/participer/<int:id>/", participer, name="participer"),
    path("utilisateur/profil<int:id>/", Profil, name="profil"),
    path("paiment/<int:id>/", gerer_paiment, name="paiment"),

    
    

]
