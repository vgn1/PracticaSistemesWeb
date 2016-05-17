#from rest_framework.fields import CharField
#from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
#from rest_framework.serializers import HyperlinkedModelSerializer
#from models import MovieReview, Movie, Actor, Company, Director, MovieCategory
#
#class MovieSerializer(HyperlinkedModelSerializer):
#    uri = HyperlinkedIdentityField(view_name='myapp:movie-detail')
#    director = HyperlinkedRelatedField(many=False, read_only=True, view_name='myapp:director-detail')
#    actors = HyperlinkedRelatedField(many=True, read_only=True, view_name='myapp:actor-detail')
#	company = HyperlinkedRelatedField(many=False, read_only=True, view_name='myapp:company-detail')
#	restaurantreview_set = HyperlinkedRelatedField(many=True, read_only=True,
#                                                   view_name='myrestaurants:restaurantreview-detail')
#    user = CharField(read_only=True)
#
#
#    class Meta:        model = Restaurant
#        fields = ('uri', 'name', 'year', 'overview', 'user', 'director', 'actors', 'company', 'restaurantreview_set')
#
#
#class DishSerializer(HyperlinkedModelSerializer):
#    uri = HyperlinkedIdentityField(view_name='myrestaurants:dish-detail')
#    restaurant = HyperlinkedRelatedField(view_name='myrestaurants:restaurant-detail', read_only=True)
#    user = CharField(read_only=True)
#
#    class Meta:
#        model = Dish
#        fields = ('uri', 'name', 'description', 'price', 'image', 'user', 'date', 'restaurant')
