from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic import ListView
from models import MovieReview, Movie, Actor, Company, Director, MovieCategory

class MovieList(ListView):
	model = Movie
	template_name = 'myapp/movie_list.html'
	context_object_name = 'latest_movie_list'

class MovieDetail(DetailView):
	model = Movie
	template_name = 'myapp/movie_detail.html'

	def get_context_data(self, **kwargs):
		context = super(MovieDetail, self).get_context_data(**kwargs)
		#context['RATING_CHOICES'] = MovieReview.RATING_CHOICES
		return context

class ActorList(ListView):
	model = Actor
	template_name = 'myapp/actor_list.html'
	queryset=Actor.objects.all()
	context_object_name = 'latest_actor_list'
	latest_actor_list=queryset

class ActorDetail(DetailView):
	model = Actor
	template_name = 'myapp/actor_detail.html'
	def get_context_data(self, **kwargs):
		context = super(ActorDetail, self).get_context_data(**kwargs)
		#context['RATING_CHOICES'] = MovieReview.RATING_CHOICES
		return context

class CompanyList(ListView):
	model = Company
	template_name = 'myapp/company_list.html'
	context_object_name = 'latest_company_list'

class CompanyDetail(DetailView):
	model = Company
	template_name = 'myapp/company_detail.html'

class DirectorList(ListView):
	model = Director
	template_name = 'myapp/director_list.html'
	context_object_name = 'latest_director_list'

class DirectorDetail(DetailView):
	model = Director
	template_name = 'myapp/director_detail.html'

def category(request, pk):
	movie = get_object_or_404(Movie, pk=pk)
	category = MovieCategory(
		rating=request.POST['rating'],
		user=request.user,
		movie=movie)
	category.save()
	return HttpResponseRedirect(reverse('myapp:movie_detail',
		args=(movie.id,ea)))

def review(request, pk):
	movie = get_object_or_404(Movie, pk=pk)
	review = MovieReview(
		rating=request.POST['rating'],
		comment=request.POST['comment'],
		user=request.user,
		movie=movie)
	review.save()
	return HttpResponseRedirect(reverse('myapp:movie_detail',
		args=(movie.id,ea)))
