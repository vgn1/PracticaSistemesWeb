from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from models import MovieReview, Movie, Actor, Company, Director, MovieCategory
from forms import DirectorForm, CompanyForm, MovieForm, ActorForm
from serializers import DirectorSerializer, CompanySerializer, MovieReviewSerializer 
from serializers import MovieCategorySerializer, MovieSerializer, ActorSerializer




class ConnegResponseMixin(TemplateResponseMixin):

	def render_json_object_response(self, objects, **kwargs):
		json_data = serializers.serialize(u"json", objects, **kwargs)
		return HttpResponse(json_data, content_type=u"application/json")

	def render_xml_object_response(self, objects, **kwargs):
		xml_data = serializers.serialize(u"xml", objects, **kwargs)
		return HttpResponse(xml_data, content_type=u"application/xml")

	def render_to_response(self, context, **kwargs):
		if 'extension' in self.kwargs:
			try:
				objects = [self.object]
			except AttributeError:
				objects = self.object_list
			if self.kwargs['extension'] == 'json':
				return self.render_json_object_response(objects=objects)
			elif self.kwargs['extension'] == 'xml':
				return self.render_xml_object_response(objects=objects)
		return super(ConnegResponseMixin, self).render_to_response(context)


class LoginRequiredMixin(object):
	@method_decorator(login_required())
	def dispatch(self, *args, **kwargs):
		return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
	def get_object(self, *args, **kwargs):
		obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
		if not obj.user == self.request.user:
			raise PermissionDenied
		return obj

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
	template_name = 'myapp/form.html'


class MovieList(ListView, ConnegResponseMixin):
	model = Movie
	template_name = 'myapp/movie_list.html'
	context_object_name = 'latest_movie_list'

class MovieDetail(DetailView, ConnegResponseMixin):
	model = Movie
	template_name = 'myapp/movie_detail.html'

	def get_context_data(self, **kwargs):
		context = super(MovieDetail, self).get_context_data(**kwargs)
		context['RATING_CHOICES'] = MovieReview.RATING_CHOICES
		return context

class MovieCreate(LoginRequiredMixin, CreateView):
	model = Movie
	template_name = 'myapp/movie_form.html'
	success_url = '../'
	form_class = MovieForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(MovieCreate, self).form_valid(form)

class MovieEdit(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
	model=Movie
	form_class=MovieForm
	template_name = 'myapp/movie_form.html'
	success_url = '../../'
	

class MovieDelete(DeleteView):
	model = Movie
	template_name = 'myapp/delete_form.html'
	success_url = '../../'
	

class ActorList(ListView, ConnegResponseMixin):
	model = Actor
	template_name = 'myapp/actor_list.html'
	queryset=Actor.objects.all()
	context_object_name = 'latest_actor_list'
	latest_actor_list=queryset

class ActorDetail(DetailView, ConnegResponseMixin):
	model = Actor
	template_name = 'myapp/actor_detail.html'
	def get_context_data(self, **kwargs):
		context = super(ActorDetail, self).get_context_data(**kwargs)
		#context['RATING_CHOICES'] = MovieReview.RATING_CHOICES
		return context


class ActorCreate(LoginRequiredMixin, CreateView):
	model = Actor
	template_name = 'myapp/actor_form.html'
	form_class = ActorForm
	success_url = '../'

	def form_valid(self, form):
		form.instance.user = self.request.user
		#form.instance.movie = Movie.objects.get(id=self.kwargs['pk'])
		return super(ActorCreate, self).form_valid(form)

class ActorEdit(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
	model=Actor
	form_class=ActorForm
	template_name = 'myapp/actor_form.html'
	success_url = '../../'

class ActorDelete(DeleteView):
	model = Actor
	template_name = 'myapp/delete_form.html'
	success_url = '../../'


class CompanyList(ListView, ConnegResponseMixin):
	model = Company
	template_name = 'myapp/company_list.html'
	context_object_name = 'latest_company_list'

class CompanyDetail(DetailView, ConnegResponseMixin):
	model = Company
	template_name = 'myapp/company_detail.html'


class CompanyCreate(LoginRequiredMixin, CreateView):
	model = Company
	template_name = 'myapp/company_form.html'
	form_class = CompanyForm
	success_url = '../'

	def form_valid(self, form):
		form.instance.user = self.request.user
		#form.instance.movie = Movie.objects.get(id=self.kwargs['pk'])
		return super(CompanyCreate, self).form_valid(form)

class CompanyEdit(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
	model=Company
	form_class=CompanyForm
	template_name = 'myapp/company_form.html'
	success_url = '../../'

class CompanyDelete(DeleteView):
	model = Company
	template_name = 'myapp/delete_form.html'
	success_url = '../../'

class DirectorList(ListView, ConnegResponseMixin):
	model = Director
	template_name = 'myapp/director_list.html'
	context_object_name = 'latest_director_list'

class DirectorDetail(DetailView, ConnegResponseMixin):
	model = Director
	template_name = 'myapp/director_detail.html'

class DirectorCreate(LoginRequiredMixin, CreateView):
	model = Director
	template_name = 'myapp/director_form.html'
	form_class = DirectorForm
	success_url = '../'

	def form_valid(self, form):
		form.instance.user = self.request.user
		#form.instance.movie = Movie.objects.get(id=self.kwargs['pk'])
		return super(DirectorCreate, self).form_valid(form)

class DirectorEdit(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
	model=Director
	form_class=DirectorForm
	template_name = 'myapp/director_form.html'
	success_url = '../../'

class DirectorDelete(DeleteView):
	model = Director
	template_name = 'myapp/delete_form.html'
	success_url = '../../'




"""class MovieReviewCreate(LoginRequiredMixin, CreateView):
	model = MovieReview
	template_name = 'myapp/form.html'
	form_class = MovieReview
	
	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.movie = Movie.objects.get(id=self.kwargs['pk'])
		return super(MovieReviewCreate, self).form_valid(form)"""

#class DirectorDelete(DeleteView):
#	model = Director
#	template_name = 'myapp/delete_form.html'
#	success_url = '/myapp/director.html'
#	success_message = 'Director Removed.'

def category(request, pk):
	movie = get_object_or_404(Movie, pk=pk)
	category = MovieCategory(
		rating=request.POST.get('rating'),
		user=request.user,
		movie=movie)
	category.save()
	return HttpResponseRedirect(reverse('myapp:movie_detail',
		args=(movie.id,)))

@login_required()
def review(request, pk):
	movie = get_object_or_404(Movie, pk=pk)

	review = MovieReview(
		rating=request.POST.get('rating'),
		comment=request.POST.get('comment'),
		user=request.user,
		movies=movie)
	review.save()
	#return HttpResponseRedirect("../../../"+str(movie.id)+"/")
	return HttpResponseRedirect(reverse('myapp:movie_detail', args=(movie.id,)))

### RESTful API views ###

class IsOwnerOrReadOnly(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):
		# Read permissions are allowed to any request,
		# so we'll always allow GET, HEAD or OPTIONS requests.
		if request.method in permissions.SAFE_METHODS:
			return True
		# Instance must have an attribute named `owner`.
		return obj.user == request.user

class APIMovieList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
	model = Movie
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer

class APIMovieDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsOwnerOrReadOnly,)
	model = Movie
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer

class APIDirectorList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
	model = Director
	queryset = Director.objects.all()
	serializer_class = DirectorSerializer

class APIDirectorDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsOwnerOrReadOnly,)
	model = Director
	queryset = Director.objects.all()
	serializer_class = DirectorSerializer

class APIActorList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
	model = Actor
	queryset = Actor.objects.all()
	serializer_class = ActorSerializer

class APIActorDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsOwnerOrReadOnly,)
	model = Actor
	queryset = Actor.objects.all()
	serializer_class = ActorSerializer

class APICompanyList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
	model = Company
	queryset = Company.objects.all()
	serializer_class = CompanySerializer

class APICompanyDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsOwnerOrReadOnly,)
	model = Company
	queryset = Company.objects.all()
	serializer_class = CompanySerializer

class APIMovieReviewList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
	model = MovieReview
	queryset = MovieReview.objects.all()
	serializer_class = MovieReviewSerializer

class APIMovieReviewDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsOwnerOrReadOnly,)
	model = MovieReview
	serializer_class = MovieReviewSerializer

class APIMovieCategoryList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
	model = MovieCategory
	queryset = MovieCategory.objects.all()
	serializer_class = MovieCategorySerializer

class APIMovieCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsOwnerOrReadOnly,)
	model = MovieCategory
	queryset = MovieCategory.objects.all()
	serializer_class = MovieCategorySerializer


