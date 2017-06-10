# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.models import User

# Create your views here.

class index(TemplateView):
    template_name = "home.html"

home_index = index.as_view()
