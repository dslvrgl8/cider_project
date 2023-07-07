# import models
from .models import Cider, Flavor, Favorite
from django.shortcuts import redirect
from django.views import View
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
#...
from django.views.generic.base import TemplateView
# This will import the class we are extending 
from django.views.generic.edit import CreateView
# after our other imports 
from django.views.generic import DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    # Here we have added the playlists as context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorites"] = Favorite.objects.all()
        return context

#...
class About(TemplateView):
    template_name = "about.html"

 #adds artist class for mock database data
# class Cider:
#     def __init__(self, name, image, bio):
#         self.name = name
#         self.image = image
#         self.bio = bio


# ciders = [
#   Cider("Gorillaz", "https://i.scdn.co/image/ab67616d00001e0295cf976d9ab7320469a00a29",
#           "Gorillaz are once again disrupting the paradigm and breaking convention in their round the back door fashion with Song Machine, the newest concept from one of the most inventive bands around."),
#   Cider("Panic! At The Disco",
#           "https://i.scdn.co/image/58518a04cdd1f20a24cf0545838f3a7b775f8080", "Welcome 👋 The Amazing Beebo was working on a new bio but now he's too busy taking over the world."),
#   Cider("Joji", "https://i.scdn.co/image/7bc3bb57c6977b18d8afe7d02adaeed4c31810df",
#           "Joji is one of the most enthralling artists of the digital age. New album Nectar arrives as an eagerly anticipated follow-up to Joji's RIAA Gold-certified first full-length album BALLADS 1, which topped the Billboard R&B / Hip-Hop Charts and has amassed 3.6B+ streams to date."),
#   Cider("Metallica",
#           "https://i.scdn.co/image/ab67706c0000da84eb6bb372a485d26fd32d1922", "Metallica formed in 1981 by drummer Lars Ulrich and guitarist and vocalist James Hetfield and has become one of the most influential and commercially successful rock bands in history, having sold 110 million albums worldwide while playing to millions of fans on literally all seven continents."),
#   Cider("Bad Bunny",
#           "https://www.clashmusic.com/sites/default/files/sty…e/Bad-Bunny-YHLQMDLG-Album-2020.jpg?itok=tbZNj82L", "Benito Antonio Martínez Ocasio, known by his stage name Bad Bunny, is a Puerto Rican rapper, singer, and songwriter. His music is often defined as Latin trap and reggaeton, but he has incorporated various other genres into his music, including rock, bachata, and soul"),
#   Cider("Kaskade",
#           "https://i1.sndcdn.com/artworks-sNjd3toBZYCG-0-t500x500.jpg", "Ryan Gary Raddon, better known by his stage name Kaskade, is an American DJ, record producer, and remixer."),
# ]

class CiderList(TemplateView):
    template_name = "cider_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["ciders"] = Cider.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["ciders"] = Cider.objects.all()
            # default header for not searching 
            context["header"] = "Best Ciders"
        return context

# ...
class CiderCreate(CreateView):
    model = Cider
    fields = ['name', 'img', 'bio', 'verified_cider']
    template_name = "cider_create.html"
    # this will get the pk from the route and redirect to artist view
    def get_success_url(self):
        return reverse('cider_detail', kwargs={'pk': self.object.pk})

class CiderDetail(DetailView):
    model = Cider
    template_name = "cider_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorites"] = Favorite.objects.all()
        return context


class CiderUpdate(UpdateView):
    model = Cider
    fields = ['name', 'img', 'bio', 'verified_cider']
    template_name = "cider_update.html"

    def get_success_url(self):
        return reverse('cider_detail', kwargs={'pk': self.object.pk})
    
class CiderDelete(DeleteView):
    model = Cider
    template_name = "cider_delete_confirmation.html"
    success_url = "/ciders/"

class FlavorCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        rating = request.POST.get("rating")
        cider = Cider.objects.get(pk=pk)
        Flavor.objects.create(title=title, rating=rating, cider=cider)
        return redirect('cider_detail', pk=pk)
    

class FavoriteFlavorAssoc(View):

    def get(self, request, pk, flavor_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            Favorite.objects.get(pk=pk).flavors.remove(flavor_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            Favorite.objects.get(pk=pk).flavors.add(flavor_pk)
        return redirect('home')
