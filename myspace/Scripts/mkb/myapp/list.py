from django.http import HttpResponse

def hai(request):
    return HttpResponse("<h2>Hello world</h2>")