from django.shortcuts import render, get_object_or_404
from django.views.generic   import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Produit, Serie

class HomePageView(TemplateView):
    template_name= 'home.html'
    model = Serie

    def get(self, request):
         series = Serie.objects.all()
         stu = {"serie_name": series}
         return render(request, 'home.html', stu)

class AboutPageView(TemplateView):
    template_name= 'about.html'

class BioPageView(TemplateView):
    template_name = 'bio.html'

class MentionPageView(TemplateView):
    template_name = 'mentions.html'

class ProduitListView(ListView):
    model = Produit
    template_name = 'produit.html'

class SerieListView(ListView):
    model = Serie
    template_name = 'serie.html'
    context_object_name = 'products_list'

class SerieDetailView(DetailView):
    model = Serie
    template_name = 'serie_detail.html'

    def get_object(self):
        id_= self.kwargs.get("id")
        return get_object_or_404(Serie, id=id_)

class ProduitDetailView(DetailView):
    model = Produit
    template_name = 'produit_detail.html'

    def get_object(self):
        id_= self.kwargs.get("id")
        return get_object_or_404(Produit, id=id_)
