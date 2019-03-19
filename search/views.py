from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
import requests
from .forms import searchForm
import urllib.parse


def home(request):
    response = requests.get(
        'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
    imageData = response.json()
    return render(request, 'search/home.html', {
        'Picture': imageData['url'],
        'Description': imageData['explanation']
    })


def query(request):
    if request.method == 'GET':
        form = searchForm()
        return render(request, 'search/query.html', {'form': form})


def results(request):

    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = searchForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            s1 = form.cleaned_data.get('Key_Words')
            s2 = form.cleaned_data.get('Lower_Year_Bound')
            s3 = form.cleaned_data.get('Upper_Year_Bound')
            s4 = form.cleaned_data.get('General_Search')
            s5 = form.cleaned_data.get('Title')
            s6 = form.cleaned_data.get('NASA_ID')

            urlAtt = dict()
            if (s1 != ''):
                urlAtt['keywords'] = s1
            else:
                s1 = "None Given"
            if (s2 != None):
                urlAtt['year_start'] = str(s2)
            else:
                s2 = "None Given"
            if (s3 != None):
                urlAtt['year_end'] = str(s3)
            else:
                s3 = "None Given"
            if (s4 != ''):
                urlAtt['q'] = s4
            else:
                s4 = "None Given"
            if (s5 != ''):
                urlAtt['title'] = s5
            else:
                s5 = "None Given"
            if (s6 != ''):
                urlAtt['nasa_id'] = s6
            else:
                s6 = "None Given"

            if (len(urlAtt) != 0):
                response = requests.get(
                    'https://images-api.nasa.gov/search?' + urllib.parse.urlencode(urlAtt, doseq=True))
                imageData = response.json()
            else:
                response = requests.get(
                    'https://images-api.nasa.gov/search?q=OkayCanWePleaseEnterSomeSearchTerms')
                imageData = response.json()

        items = list()
        items = imageData['collection']['items']

        return render(request, 'search/results.html', {
            'Keywords': s1,
            'Lower_Bound': s2,
            'Upper_Bound': s3,
            'General': s4,
            'Title': s5,
            'NASA_ID': s6,
            'Hits': imageData["collection"]['metadata']["total_hits"],
            'Href': imageData["collection"]["href"],
            'Items': items
        })
