from django.http import HttpResponse

def contact(request):
    return HttpResponse("<h2>contact page hello what's up </h2>")