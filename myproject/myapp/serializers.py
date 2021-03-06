from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import MovieReview, Movie, Actor, Company, Director, MovieCategory

class MovieSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='myapp:movie-detail')
    director = HyperlinkedRelatedField(many=False, read_only=True, view_name='myapp:director-detail')
    actors = HyperlinkedRelatedField(many=True, read_only=True, view_name='myapp:actor-detail')
    company = HyperlinkedRelatedField(many=True, read_only=True, view_name='myapp:company-detail')
    user = CharField(read_only=True)

    class Meta:        
        model = Movie
        fields = ('uri', 'name', 'year', 'overview', 'user', 'director', 'actors', 'company')


class ActorSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='myapp:actor-detail')
    #movies = HyperlinkedRelatedField(many=True, view_name='myapp:movie-detail', read_only=True)

    class Meta:
        model = Actor
        fields = ('uri','name', 'birthday', 'biography')

class DirectorSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='myapp:director-detail')

    class Meta:
        model = Director
        fields = ('uri', 'name', 'birthday', 'biography')

class CompanySerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='myapp:company-detail')

    class Meta:
        model = Company
        fields = ('uri', 'name', 'homePage')
 
class MovieReviewSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='myapp:moviereview-detail')
    movies = HyperlinkedRelatedField(many=False, read_only=True, view_name='myapp:movie-detail')

    class Meta:
        model = MovieReview
        fields = ('uri','rating', 'comment', 'user','movies')

class MovieCategorySerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='myapp:moviecategory-detail')
    movie = HyperlinkedRelatedField(many=False, read_only=True, view_name='myapp:movie-detail')

    class Meta:
        model = MovieCategory
        fields = ('uri', 'category', 'user','movie')


