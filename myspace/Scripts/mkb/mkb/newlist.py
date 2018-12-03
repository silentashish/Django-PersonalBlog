from django.http import HttpResponse

def saiho(request):
    return HttpResponse("hello from otherside ")