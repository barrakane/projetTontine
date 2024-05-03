from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import GroupeTontine, Membre, Paiment, User
# Create your views here.



def home(request):
    message = "Bonjour vous etes a la pages d'acceuil"
    context = {'message': message}
    return render(request, "pages/index.html", context)

def about(request):
    return render(request, "pages/about.html")
 
@login_required(login_url="/login/")
def Liste_groupe(request):
    user = request.user
    print("user",user)
    Groupetontines = GroupeTontine.objects.all()
    return render(request, "groupes/groupe_liste.html", {"Groupetontines": Groupetontines} )

def groupe_detail(request, id):
    groupe_details = get_object_or_404(GroupeTontine, id=id)
    return render(request, "groupes/groupe_detail.html", {"groupe_details": groupe_details} )



@login_required(login_url="/login/")
def Mes_groupe(request):
    user = request.user
    print("user", user)
    groupeTontines = GroupeTontine.objects.filter(auteur=user)
    return render(request, "groupes/Mes_Groupe.html", {"groupeTontines": groupeTontines})


def gerer_groupe(request, id):
    group_id = get_object_or_404(GroupeTontine, id=id)
    idgroup = int(group_id.id)
    group =  GroupeTontine.objects.get(id=idgroup)
    membre = Membre.objects.filter(group=group)
    return render(request, "groupes/gerer_groupe.html", {"membre": membre})




@login_required(login_url="/login/")
def new_groupe(request):
    if request.method == "POST":
        auteur = request.user
        nom = request.POST['nom']
        cotisation = request.POST['cotisation']
        frequence = request.POST['frequence']
        dateDebut = request.POST['dateDebut']
        groupe = GroupeTontine.objects.create(
            auteur=auteur,
            nom=nom,
            montantCotisation=cotisation,
            frequencePaiment=frequence,
            dateDebut=dateDebut,
        )
        groupe.save()
        return redirect("/groupes/")
        
        
    return render(request, "groupes/new_groupe.html")


    
   
    
    
    
def participer(request, id):
    membre = get_object_or_404(GroupeTontine, id=id)
    user = request.user
    if request.method == "POST":
        idGroupe = groupes
        name = request.POST['name']
        prenom = request.POST['prenom']
        telephone = request.POST['telephone']
        adress = request.POST['adress']
        

        groupes = Membre.objects.create(
            
            name=name,
            prenom=prenom,
            telephone=telephone,
            adress=adress,
            participation = idGroupe,
            
            
        )
        groupes.save()
        return redirect("/groupes/")
        
        
    return render(request, "groupes/participer/participer.html", {"membre": membre})





@login_required(login_url="/login/")
def Profil(request ):
    user = request.user
    print("user",user)
    profil = User.objects.all()
    return render(request, "utilisateur/profil.html", {"profil": profil} )


@login_required(login_url="/login/")
def gerer_paiment(request, id):
    membres = get_object_or_404(Membre, id=id)
    if request.method == "POST":    
        membre = membres
        montant = request.POST['montant']
        tour = request.POST['tour']
       
        paiments = Paiment.objects.create(
            membre=membres,
            montant=montant,
            tour=tour,

        )
        paiments.save()
        return redirect("/groupes/")
        
        
    return render(request, "paiment/paiment.html" ,{"membres": membres})










@login_required
def payment_history(request):
    
    paiment = Paiment.objects.all().order_by('-date')
    return render(request, 'paiment/paiment.html', {'paiment': paiment})

