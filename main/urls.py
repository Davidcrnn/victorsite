from django.urls import path
from django.views.generic.detail import DetailView

from .views import HomePageView, AboutPageView, BioPageView, MentionPageView, SerieListView, SerieDetailView, ProduitDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('bio/', BioPageView.as_view(), name='bio'),
    path('mentions-legales/', MentionPageView.as_view(), name= 'mentions-legales'),
    path("series/", SerieListView.as_view(), name= 'serie'),
    path("series/<int:id>/", SerieDetailView.as_view(), name= 'serie-detail'),
    path('<int:id>/', ProduitDetailView.as_view(), name= 'produit-detail'),
]

