from django.shortcuts import render

# Create your views here.

#define a view and pass in a request

# a persone type a url on a webpage
# they are making a request to the server
def home(request):
    # api url => http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=100&API_KEY=6DB8BBCC-987C-4386-B75A-CDA5238F4725
    # connect to the api and bring it here 

    # import inside the view where we need to use it
    # request is use to go out on internet get the data and bring it back
    # instal in the virtual env
    import json
    import requests

    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=100&API_KEY=6DB8BBCC-987C-4386-B75A-CDA5238F4725")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."
                                # transferring it into return
                                # now we can accey it in our home page
    return render(request, 'home.html', {'api': api})

# render the request and pointed it to the html file


def about(request):
    return render(request, 'about.html', {})

# do other request for the other pages