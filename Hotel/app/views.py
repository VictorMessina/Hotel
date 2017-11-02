"""
Definition of views.
"""

from app.models import *
from app.postgres import nationality_functions, user_functions, user_type_functions, user_info_functions
from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime


def sign_up(request):
    if request.method == "GET":
        all_nationality = Nationality.objects.all()
        return render(request, 'app/signup.html', {'all_nationality': all_nationality})
    elif request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        cellphone = request.POST.get('cellphone')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')

        # Get user type data
        nationality_id = request.POST.get('nationality')
        last_address = request.POST.get('last_address')
        identification_number_passport = request.POST.get('identification_number_passport')
        identification_number_citizen_card = request.POST.get('identification_number_citizen_card')
        resident = request.POST.get('resident')

        if identification_number_citizen_card == "":
            identification_number = identification_number_passport
        else:
            identification_number = identification_number_citizen_card

        # Get user data
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        description = request.POST.get('description')

        if user_functions.find_user(user_name) is not None: 
            
            print('User already registed, please try again')
            return HttpResponseRedirect('/signup')

        elif password != password2:

            print("password don't match")
            return HttpResponseRedirect('/signup')

        else:
            try:
                user_type = user_type_functions.create_user_type(identification_number, resident, last_address, nationality_id)
                user = user_functions.create_user(user_name, password, description)
                user_info = user_info_functions.create_user_info(first_name, last_name, email, telephone, cellphone, gender, birthday, identification_number)
                return HttpResponseRedirect('/')
            except Exception:
                print("user not registered")
                return HttpResponseRedirect('/signup')

# fazer a pagina de perfil

def nationality_details(request, nationality_id):
    nationality = nationality_functions.find_nationality_by_id(nationality_id)
    return render_to_response('app/nationalitydetails.html',{'nationality': nationality})


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
