from django.http import HttpResponse, HttpResponseRedirect


# def home(request):
#     print(dir(request))
#     print(request.get_full_path())
#     return HttpResponse("<html><body><h1> Hello World </></body></html>")

def home(request):
    response = HttpResponse()
    response.write("<p> now paragraph</p>")
    response.status_code = 200
    return response

def redirect_somewhere(request):
    return HttpResponseRedirect('/somewhere')