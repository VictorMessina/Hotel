"""
Definition of views.
"""

import json
from datetime import datetime
from app.models import *
from app.postgres import nationality_functions, user_functions, user_type_functions, user_info_functions, rooms_functions 
from django.contrib import messages
from django.contrib.auth.views import logout
from django.forms.models import model_to_dict
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core import serializers

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
            messages.error(request,'User already registed, please try again')
            return HttpResponseRedirect('/signup')

        elif password != password2:
            messages.error(request, "password don't match")
            return HttpResponseRedirect('/signup')

        else:
            try:
                user_type = user_type_functions.create_user_type(identification_number, resident, last_address, nationality_id)
                user = user_functions.create_user(user_name, password, description)
                user_info = user_info_functions.create_user_info(first_name, last_name, email, telephone, cellphone, gender, birthday, identification_number)
                messages.success(request,'user registered')
                return HttpResponseRedirect('/')
            except Exception:
                messages.error(request,'user not registered')
                return HttpResponseRedirect('/signup')


def login(request):
    if request.method == "GET":
        return render(request, 'app/index.html')
    else:
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        validation = user_functions.validate_login(user_name, password)

        if validation is True:
            user_data = user_functions.find_all_user_data(user_name)
            login_data = model_to_dict(user_data['user'])
            user_type_data = model_to_dict(user_data['userType'])
            nationality_data = model_to_dict(user_data['nationality'])
            user_info_data = serializers.serialize('json',[user_data['userInfo']])
            user_info_data = json.loads(user_info_data)[0]
            request.session['login_data'] = login_data
            request.session['user_info_data'] = user_info_data
            request.session['user_type_data'] = user_type_data
            request.session['nationality_data'] = nationality_data
            return render(request, 'app/profile.html')
        else:
            messages.error(request, 'Username or password is wrong, try again')
            return HttpResponseRedirect('/')


def logout(request):
    logout(request)


def profile(request):
    try:
        if request.method == "GET":
            userData = user_functions.find_all_user_data(request.session['login_data']['user_name'])
            return render(request, 'app/profile.html')
    except Exception:
        messages.error(request,'Please login to access your profile')
        return HttpResponseRedirect('/')


def edit_profile(request):
    try:

        if request.method == "GET":

            userData = user_functions.find_all_user_data(request.session['login_data']['user_name'])
            all_nationality = Nationality.objects.all()
            return render(request, 'app/editprofile.html', {'all_nationality': all_nationality})

        elif request.method == "POST":

            function_id = int(request.POST.get('function_id'))
            user_id = request.POST.get('user_id')
            user_type_id = request.POST.get('user_type_id')
            update_validation = None

            if function_id == 1:

                user_name = request.POST.get('user_name')
                update_validation = user_functions.update_user_name(user_name, user_id)

            elif function_id == 2:

                password = request.POST.get('password')
                confirm_password = request.POST.get('confirm_password')
                update_validation = user_functions.update_password(password, confirm_password, user_id)

            elif function_id == 3:

                first_name = request.POST.get('first_name')
                update_validation = user_info_functions.update_first_name(first_name, user_id)

            elif function_id == 4:

                last_name = request.POST.get('last_name')
                update_validation = user_info_functions.update_last_name(last_name, user_id)

            elif function_id == 5:

                email = request.POST.get('email')
                update_validation = user_info_functions.update_email(email, user_id)

            elif function_id == 6:

                telephone = request.POST.get('telephone')
                update_validation = user_info_functions.update_telephone(telephone, user_id)

            elif function_id == 7:

                cellphone = request.POST.get('cellphone')
                update_validation = user_info_functions.update_cellphone(cellphone, user_id)

            elif function_id == 8:

                gender = request.POST.get('gender')
                update_validation = user_info_functions.update_gender(gender, user_id)

            elif function_id == 9:

                birthday = request.POST.get('birthday')
                update_validation = user_info_functions.update_birthday(birthday, user_id)

            elif function_id == 10:

                nationality_id = request.POST.get('nationality_id')
                resident = request.POST.get('resident')
                identification_number_passport = request.POST.get('identification_number_passport')
                identification_number_citizen_card = request.POST.get('identification_number_citizen_card')

                if identification_number_citizen_card == "":
                    identification_number = identification_number_passport
                else:
                    identification_number = identification_number_citizen_card

                update_validation = user_type_functions.update_nationality(identification_number, resident, nationality_id, user_type_id)

            elif function_id == 11:

                last_address = request.POST.get('last_address')
                update_validation = user_type_functions.update_last_address(last_address, user_type_id)

            if update_validation is True:

                if function_id == 1:
                    user_data = user_functions.find_all_user_data(user_name)
                else:
                    user_data = user_functions.find_all_user_data(request.session['login_data']['user_name'])

                messages.success(request,'User updated')
                login_data = model_to_dict(user_data['user'])
                user_type_data = model_to_dict(user_data['userType'])
                nationality_data = model_to_dict(user_data['nationality'])
                user_info_data = serializers.serialize('json',[user_data['userInfo']])
                user_info_data = json.loads(user_info_data)[0]
                request.session['login_data'] = login_data
                request.session['user_info_data'] = user_info_data
                request.session['user_type_data'] = user_type_data
                request.session['nationality_data'] = nationality_data
                return render(request, 'app/profile.html')
            else:
                messages.error(request,'User not updated')
                return HttpResponseRedirect('/profile')
    except Exception:
        messages.error(request,'Please login to access this area')
        return HttpResponseRedirect('/')

def rooms_details(request, room_id):
    room = rooms_functions.find_all_room_data(room_id)
    return render(request,'app/roomsdetails.html',{'room': room})


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
