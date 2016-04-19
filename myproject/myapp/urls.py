from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView
from models import Director, Movie, Company, Actor,\
					MovieReview,MovieCategory, Review
from views import MovieDetail, MovieList, ActorList, ActorDetail, review,\
 					DirectorList, DirectorDetail, CompanyList, CompanyDetail

urlpatterns = [

	# Home page
    url(r'^$',
        TemplateView.as_view(template_name="myapp/principal.html"),
        name="Principal"),

	#Movies list
	url(r'^movie/$',
		MovieList.as_view(
			context_object_name='latest_movie_list',
			template_name='myapp/movie_list.html'),
		name='movie_list'),

	#Movies detail
	url(r'^movie/(?P<pk>\d+)/$',
		MovieDetail.as_view(
			model=Movie,
			template_name='myapp/movie_detail.html'),
		name='movie_detail'),


	#Actor list
	url(r'^actor/$',
		ActorList.as_view(
			context_object_name='latest_actor_list',
			template_name='myapp/actor_list.html'),
		name='actor_list'),

	#Actor detail
	url(r'^actor/(?P<pk>\d+)/$',
		ActorDetail.as_view(
			model=Actor,
			template_name='myapp/actor_detail.html'),
		name='actor_detail'),

	#Director list
	url(r'^director/$',
		DirectorList.as_view(
			context_object_name='latest_director_list',
			template_name='myapp/director_list.html'),
		name='director_list'),

	#Director detail
	url(r'^director/(?P<pk>\d+)/$',
		DirectorDetail.as_view(
			model=Director,
			template_name='myapp/director_detail.html'),
		name='director_detail'),

	#Company list
	url(r'^company/$',
		CompanyList.as_view(
			context_object_name='latest_company_list',
			template_name='myapp/company_list.html'),
		name='company_list'),

	#Company detail
	url(r'^company/(?P<pk>\d+)/$',
		CompanyDetail.as_view(
			model=Company,
			template_name='myapp/company_detail.html'),
		name='company_detail'),


]
