from django.shortcuts import render
from testadmin.forms import myform, model_form


# Create your views here.

def index(request):
    if request.method == 'POST':
        user_form=myform(request.POST)
        profile_form=model_form(request.POST)

        if user_form.is_valid():
            user=user_form.save()
            print("success in one saving")

        elif profile_form.is_valid():
            pro=profile_form.save()
            print("success in two form")

        else:
            print(user_form.errors,profile_form.errors)
            print('form is not save')
    else:
        user_form=myform(request.POST)
        profile_form=model_form(request.POST)

    return render(request,'custom_admin/index.html',{'firstform':myform,'secondform':model_form})
