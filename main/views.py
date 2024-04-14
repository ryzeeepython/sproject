from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginUserForm, TestForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UserAccount, User
from django.urls import reverse_lazy
import os
import mimetypes
from .pdf_generator import pdf_generator

pdf_generator = pdf_generator.Main()




# Create your views here.
def index(request): 
    return render(request, 'main/index.html')

def auth(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/lobby')
                else:
                    return HttpResponse('Disabled account')
            else:
                print('Access denied')
                return render(request, 'main/login.html', {'form': form, 'access_denied': True})
        else: 
            print(form.errors)
    else:
        form = LoginUserForm()

    return render(request, 'main/auth.html', {'form': form})   

@login_required(login_url='/register')
def test(request): 

    if request.method == 'POST':

        form = TestForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            counter = 0
            if data['q1'][0] == '3': 
                counter += 1
            if data['q2'][0] == '1':
                counter += 1
            if data['q3'][0] == '1':
                counter += 1
            if data['q4'][0] == '2': 
                counter += 1
            if data['q5'][0] == '3':
                counter += 1
            if data['q6'][0] == '3':
                counter += 1
            if data['q7'][0] == '2':
                counter += 1
            
            res  = counter/7 * 100 // 1.
            user_acc = UserAccount.objects.get(user_id = request.user.pk)
            user_acc.test_mark = res 
            user_acc.is_done_test = True
            user_acc.save()
            return redirect('/results')
            #user_acc = UserAccount(user = request.user, test_mark = res, is_done_test = True)
           
    else:
        form = RegisterUserForm()  

    return render(request, 'main/test.html', {'form': TestForm})

@login_required(login_url='/register')
def show_res(request): 
    user = UserAccount.objects.get(user_id = request.user.pk)
    if not(user.test_mark): 
        return redirect('/test')
    if user.test_mark > 70: 
        return render(request, 'main/good_res.html', {'user_acc': user})
    else: 
        return render(request, 'main/bad_res.html', {'user_acc': user})

    
@login_required(login_url='/register')
def download_file(request): 
    user = User.objects.get(id = request.user.pk)
    user_acc = UserAccount.objects.get(user_id = request.user.pk)
    filename = str(user_acc.unique_code) + '.png'
    pdf_generator.make_pdf(user.first_name, user_acc.unique_code)

    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(BASE_DIR)
        # Define the full file path
        filepath = BASE_DIR + '/main/filedownload/' + filename
        # # Open the file for reading content
        path = open(filepath, 'rb')
        # # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # # Return the response value
        return response
    else:
        # Load the template
        return redirect('/results')
    
def registration(request): 
    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.first_name = user_form.cleaned_data['name']
            user.save()
            user_acc = UserAccount(user=user)
            code = pdf_generator.generate_code()
            user_acc.unique_code = code
            user_acc.save()
            login(request, user)
            return redirect('/lobby')
    else:
        user_form = RegisterUserForm()  
    return render(request, 'main/registration.html', {'form': user_form})

@login_required(login_url=reverse_lazy('main:auth'), redirect_field_name=None)
def page_1(request): 
    next_page = 2
    return render(request, 'main/page_1.html', {'page_num': next_page})

@login_required(login_url=reverse_lazy('main:auth'), redirect_field_name=None)
def page_2(request): 
    next_page = 3
    prev_page = 1
    return render(request, 'main/page_2.html', {'page_num': next_page, "prev_page": prev_page})

@login_required(login_url=reverse_lazy('main:auth'), redirect_field_name=None)
def page_3(request): 
    next_page = 4
    prev_page = 2
    return render(request, 'main/page_3.html', {'page_num': next_page, "prev_page": prev_page})

@login_required(login_url=reverse_lazy('main:auth'), redirect_field_name=None)
def page_4(request): 
    next_page = 5
    prev_page = 3
    return render(request, 'main/page_4.html', {'page_num': next_page, "prev_page": prev_page})

@login_required(login_url=reverse_lazy('main:auth'), redirect_field_name=None)
def page_5(request): 
    next_page = 6
    prev_page = 4
    return render(request, 'main/page_5.html', {'page_num': next_page, "prev_page": prev_page})

@login_required(login_url=reverse_lazy('main:auth'), redirect_field_name=None)
def page_6(request): 
    next_page = 6
    prev_page = 5
    return render(request, 'main/page_6.html', {'page_num': next_page, "prev_page": prev_page})

def bad_res(request): 
    return render(request, 'main/test.html')

def good_res(request): 
    return render(request, 'main/test.html')

@login_required(login_url=reverse_lazy('main:auth'), redirect_field_name=None)
def lobby(request): 
    return render(request, 'main/lobby.html')


def logout_user(request):
    logout(request)
    return redirect('/auth')