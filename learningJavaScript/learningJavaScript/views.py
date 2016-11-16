from django.shortcuts import render, redirect
from django.http.response import (HttpResponse, Http404)
from django.views.generic import View
from django.template import loader, Context
from django.shortcuts import get_object_or_404
from django.views.generic import View


class Home(View):
	def get(self, request):
		return render(request, 'home.html')