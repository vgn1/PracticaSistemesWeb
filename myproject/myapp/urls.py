from django.conf.urls import url
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView, RedirectView

from rest_framework.urlpatterns import format_suffix_patterns

from models import Director, Movie, Company, Actor,\
					MovieReview,MovieCategory, Review
from forms import DirectorForm, CompanyForm, MovieForm, ActorForm
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

	#Create Movie
	url(r'^movie/create/$',
        MovieCreate.as_view(),
        name='movie_create'),

	#Edit Movie
	url(r'^movie/(?P<pk>\d+)/edit/$',
    	LoginRequiredCheckIsOwnerUpdateView.as_view(
        	model=Movie,
            form_class=MovieForm),
        name='movie_edit'),

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

	#Create Actor
	url(r'^actor/create/$',
        ActorCreate.as_view(),
        name='actor_create'),

	#Edit Actor
	url(r'^actor/(?P<pk>\d+)/edit/$',
    	LoginRequiredCheckIsOwnerUpdateView.as_view(
        	model=Actor,
            form_class=ActorForm),
        name='actor_edit'),

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
	#Create Director
	url(r'^director/create/$',
        DirectorCreate.as_view(),
        name='director_create'),

	#Edit Director
	url(r'^director/(?P<pk>\d+)/edit/$',
    	LoginRequiredCheckIsOwnerUpdateView.as_view(
        	model=Director,
            form_class=DirectorForm),
        name='director_edit'),

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

	#Create Company
	url(r'^company/create/$',
        CompanyCreate.as_view(),
        name='company_create'),

	#Edit Company
	url(r'^company/(?P<pk>\d+)/edit/$',
    	LoginRequiredCheckIsOwnerUpdateView.as_view(
        	model=Company,
            form_class=CompanyForm),
        name='company_edit'),


    # RESTful API

    url(r'^api/auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/movie/$',
        APIMovieList.as_view(), name='movie-list'),
    url(r'^api/movie/(?P<pk>\d+)/$',
        APIMovieDetail.as_view(), name='movie-detail'),
    url(r'^api/director/$',
        APIDirectorList.as_view(), name='director-list'),
    url(r'^api/director/(?P<pk>\d+)/$',
        APIDirectorDetail.as_view(), name='director-detail'),
    url(r'^api/actor/$',
        APIActorList.as_view(), name='actor-list'),
    url(r'^api/actor/(?P<pk>\d+)/$',
        APIActorDetail.as_view(), name='actor-detail'),
	url(r'^api/company/$',
        APICompanyList.as_view(), name='company-list'),
    url(r'^api/company/(?P<pk>\d+)/$',
        APICompanyDetail.as_view(), name='company-detail'),
	url(r'^api/moviereview/$',
        APIMovieReviewList.as_view(), name='moviereview-list'),
    url(r'^api/moviereview/(?P<pk>\d+)/$',
        APIMovieReviewDetail.as_view(), name='moviereview-detail'),
	url(r'^api/moviecategory/$',
        APIMovieCategoryList.as_view(), name='moviecategory-list'),
    url(r'^api/moviecategory/(?P<pk>\d+)/$',
        APIMovieCategoryDetail.as_view(), name='moviecategory-detail'),
]

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api','json', 'xml'])
