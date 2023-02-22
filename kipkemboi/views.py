from django.shortcuts import render

from . form import UserReg

def reg(request):
    submit_button = request.POST.get("chris")
    name = ''
    email = ''
    password = ''

    rform = UserReg(request.POST or None)
    if rform.is_valid():
        name = rform.cleaned_data.get("name")
        email = rform.cleaned_data.get("email")
        password = rform.cleaned_data.get("password")

    context = {'rform' : rform,'name' : name, 'email' : email,'submit_button' : submit_button}

    return render(request, 'register.html', context)


