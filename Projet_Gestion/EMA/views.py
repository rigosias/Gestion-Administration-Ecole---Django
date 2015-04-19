from django.shortcuts import render
from EMA.forms import Inscription
#from EMA.models import Eleve,Matiere,Note

# Create your views here.

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    #context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    
    return render(request, 'EMA/index.html',{})

def formulaire_inscription(request):
    if request.method == 'POST':
        form = Inscription(request.POST)

        if form.is_valid():

            form.save(commit=True)

            no_Dossier = form.cleaned_data['no_Dossier']
            compte = form.cleaned_data['compte']
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            email = form.cleaned_data['email']

            return index(request)

        else:
            print form.errors

    else:
        form = formulaire_inscription()

        


    return render(request, 'EMA/index.html',{'form':} )
            


        
