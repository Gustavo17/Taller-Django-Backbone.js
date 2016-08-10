from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView
from .models import Category, Payment, City, Restaurant

class IndexView(TemplateView):

	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		context['payments'] = Payment.objects.all()
		context['cities'] = City.objects.all()
		restaurants = Restaurant.objects.all()[:5]
		tips = [restaurant.tip_set.all().count() for restaurant in restaurants]
		context['restaurants'] = zip(restaurants, tips)
		return context


def LogOut(request):
	logout(request)
	return redirect('/')