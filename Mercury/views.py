from django.shortcuts import render
#from .models import VotreModeleDeDonnees  # Remplacez 'VotreModeleDeDonnees' par le nom de votre modèle
from datetime import datetime

def index(request):
    # Ici, vous pouvez effectuer des opérations liées à la requête (si nécessaire)
    #objets = VotreModeleDeDonnees.objects.all()  # Obtenez tous les objets du modèle (si besoin)

    # Vous pouvez également passer des données à la template en utilisant le dictionnaire context
    #context = {'objets': objets}

    date = datetime.today()
    return render(request, 'index.html' , context= {'date': date})  # Renvoie la réponse en utilisant le template 'mon_template.html'
