from django.shortcuts import render

# Create your views here.

#define a view and pass in a request

# a persone type a url on a webpage
# they are making a request to the server
def home(request):
    return render(request, 'home.html', {})

# render the request and pointed it to the html file


def about(request):
    return render(request, 'about.html', {})
