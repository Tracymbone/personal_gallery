from django.shortcuts import render
from .models import Image,Location,Category
# Create your views here.
def index(request):
    images=Image.objects.all()
    locations=Location.objects.all()
    return render(request,'gallery/index.html',{'images':images,'locations':locations})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_articles = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'gallery/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})


def location_results(request,location_id):
    loc=Image.objects.filter(location_id=location_id)
    return render(request,'gallery/location.html',{'image':loc})