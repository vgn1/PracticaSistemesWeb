from django.forms import ModelForm
from models import Director, Company, Movie, Actor

class DirectorForm(ModelForm):
    class Meta:
        model = Director
        exclude = ('user',)

class CompanyForm(ModelForm):
    class Meta:
        model = Dish
        exclude = ('user',)

class MovieForm(ModelForm):
    class Meta:
        model = Dish
        exclude = ('user', 'actors', 'director','company',)

class ActorForm(ModelForm):
    class Meta:
        model = Dish
        exclude = ('user',)