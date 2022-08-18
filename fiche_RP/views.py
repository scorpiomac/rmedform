from django.shortcuts import render
from django.forms import ModelForm
from .models import information
from .models import multistepformexample
#from myform.models import information
#from .models import multistepformexampleForm
from django.http import HttpResponseRedirect



from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.forms import ModelForm, Textarea
from fiche_RP.models import information
from django import forms
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages

class informationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(informationForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Nom "
        self.fields['firstname'].label = "Prenom"
        self.fields['email'].label = "mail"
    class Meta:
        model = information
        fields = ('name', 'firstname', 'email','message')
        widgets = {'message': Textarea(attrs={'cols': 60, 'rows': 10}),}

def information(request):
# on instancie un formulaire
    form = informationForm()
    # on teste si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        # Si oui on récupère les données postées
        form = informationForm(request.POST)
        # on vérifie la validité du formulaire
        if form.is_valid():
            new_information = form.save()
            # on prépare un nouveau message
            messages.success(request,'Nouveau contact '+new_information .name+' '+new_information .email)
            #return redirect(reverse('detail', args=[new_contact.pk] ))
            context = {'pers': new_information }
            return render(request,'detail.html', context)
    # Si méthode GET, on présente le formulaire
    context = {'information_form': form}
    return render(request,'information.html',context)


from django.views.generic import CreateView
from .models import Person


def information(request):

    information_form = informationForm()
    return render(request,'person_form.html', {'information_form' : information_form})




      
##########Formulaire Fiche#################################


from phonenumber_field.modelfields import PhoneNumberField


genre_CHOICES = [
    ('M', 'M.'),
    ('F', 'Mme')
    
]

situation_CHOICES = [
    ('célibataire', 'célibataire'),
    ('marié', 'marié(e)'),
    ('divorcé', 'divorcé(e)'),
    ('Veuf', 'Veuf(ve)')
    
]

class FicheForm(forms.Form):
    nom= forms.CharField(max_length=300)
    nomDj= forms.CharField(max_length=300)
    prenom= forms.CharField(max_length=300)
    genre = forms.ChoiceField( choices=genre_CHOICES)
    nationalite= forms.CharField(max_length=300)
    situation = forms.ChoiceField(choices=situation_CHOICES)
    birth_date = forms.DateField()
    lieu= forms.CharField(max_length=300)
    fixe=forms.CharField(max_length=15)
    mobile=forms.CharField(max_length=15)
    email_professionnel=forms.EmailField()
    email_personnel=forms.EmailField()
    nometp=forms.CharField(max_length=300)
    fixe1=forms.CharField(max_length=15)
    mobile1=forms.CharField(max_length=15)
    email_personnel1=forms.EmailField()
    matricule=forms.CharField(max_length=300)
    Employeur=forms.CharField(max_length=300)
    D_affiliation=forms.DateField()
    D_engagement=forms.DateField()


from .models import Fiche



from django.shortcuts import render
from django.http import HttpResponseRedirect
#from .forms import NewBusinessForm

def createpost(request):
    form = FicheForm(request.POST)
    #print('essai')
    #print(form.is_valid())
    #print(form)
    if request.method == 'POST':
        form = FicheForm(request.POST)
        print(form.is_valid())
        if form.is_valid:
           #if form.is_valid():
            # process form data
            obj = Fiche() #gets new object
            obj.nom= form.cleaned_data['nom']
            obj.nomDj= form.cleaned_data['nomDj']
            obj.prenom= form.cleaned_data['prenom']
            obj.genre = form.cleaned_data['genre']
            obj.nationalite=form.cleaned_data['nationalite']
            obj.situation =form.cleaned_data['situation']
            obj.birth_date = form.cleaned_data['birth_date']
            obj.lieu=form.cleaned_data['lieu']
            obj.fixe=form.cleaned_data['fixe']
            obj.mobile=form.cleaned_data['mobile']
            obj.email_professionnel=form.cleaned_data['email_professionnel']
            obj.email_personnel=form.cleaned_data['email_personnel']
            obj.nometp=form.cleaned_data['nometp']
            obj.fixe1=form.cleaned_data['fixe1']
            obj.mobile1=form.cleaned_data['mobile1']
            obj.email_personnel1=form.cleaned_data['email_personnel1']
            obj.matricule=form.cleaned_data['matricule']
            obj.Employeur=form.cleaned_data['Employeur']
            obj.D_affiliation=form.cleaned_data['D_affiliation']
            obj.D_engagement=form.cleaned_data['D_engagement']


            #finally save the object in db
            obj.save()
            return HttpResponse('Success')
            return HttpResponseRedirect('/')
            return HttpResponseRedirect('/')

    else:
            form = FicheForm(request.POST)
            form = FicheForm()
            

    return render(request, 'multistepformexample.html', {'form': form})