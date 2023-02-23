from django.shortcuts import render

from .form import UserReg
from .form import PeopleReg
from .form import StudentReg


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

    context = {'rform': rform, 'name': name, 'email': email, 'submit_button': submit_button}

    return render(request, 'register.html', context)


def reg_people(request):
    submit_people_button = request.POST.get("peoplebtn")
    name = ''
    age = ''
    phone = ''
    city = ''

    people_form = PeopleReg(request.POST or None)
    if people_form.is_valid():
        name = people_form.cleaned_data.get("name")
        age = people_form.cleaned_data.get("age")
        phone = people_form.cleaned_data.get("phone")
        city = people_form.cleaned_data.get("city")
    context = {'people_form': people_form,
               'name': name,
               'age': age,
               'city': city,
               'phone': phone,
               'submit_people_button': submit_people_button
               }
    return render(request, 'people.html', context)


def reg_students(request):
    submit_student_button = request.POST.get("studentsbtn")
    name = ''
    gender = ''
    school = ''
    parent = ''
    phone = ''

    student_form = StudentReg(request.POST or None)
    if student_form.is_valid():
        name = student_form.cleaned_data.get("name")
        gender = student_form.cleaned_data.get("gender")
        school = student_form.cleaned_data.get("school")
        parent = student_form.cleaned_data.get("parent")
        phone = student_form.cleaned_data.get("phone")
    context = {
        'people_form': student_form,
        'name': name,
        'phone': phone,
        'submit_student_button': submit_student_button,
        'gender': gender,
        'school': school,
        'parent': parent
    }
    return render(request, 'people.html', context)
