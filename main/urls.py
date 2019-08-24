from django.urls import path

from .views import HomePageView, AboutPageView, BioPageView, MentionPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('bio/', BioPageView.as_view(), name='bio'),
    path('mentions-legales/', MentionPageView.as_view(), name= 'mentions-legales')
]