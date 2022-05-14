
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib import messages
from authenticate.forms import (CustomUserCreationForm,)
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from authenticate.models import (User, Local_Government,State,Country,User_Info,\
Token,)
from django.utils import timezone
import sweetify

from resourcebank.models import Questions
now = timezone.now()
from django.db.models import Q,Avg, Count, Min, Sum
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from authenticate.sign_up_update import update_new_user_details
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def showLoginPage(request):
    return render(request,'registration/login.html',{})

def login_request(request):
    
    if request.is_ajax and request.method == "POST":
        context = {}
        email = request.POST['username']
        password = request.POST['password']
        
        account = authenticate(request,username=email, password=password)
        if account is None :
            context['message1'] = 'Invalid Login Details!'
            context['message2'] = 'Kindly Try Again With A Valid Email And Password'
            context['status'] = 'Error!'
            context['code']=status.HTTP_401_UNAUTHORIZED            
            return JsonResponse(context, status = 200)
        
        elif account is not None and not account.is_active:
            context['message1'] = 'Sorry, your account is in-Active'
            context['message2'] = 'Kindly Check Your Email For Activation Link Or Contact Support'
            context['status'] = 'Error!'  
            context['code']=status.HTTP_401_UNAUTHORIZED          
            # if Queue Access Object found return not valid 
            return JsonResponse(context, status = 200)

        elif account is None :
            context['message1'] = 'Invalid credentials!'
            context['message2'] = 'Kindly Try Again With A Valid Email And Password'
            context['status'] = 'Error!'
            context['code']=status.HTTP_401_UNAUTHORIZED            
            return JsonResponse(context, status = 200)
        
        elif account :
                login(request, account)
                try:
                    token = Token.objects.get(user=account)
                except Token.DoesNotExist:
                    token = Token.objects.create(user=account)
                context['message'] = 'Successfully authenticated.'
                context['status'] = 'Success!'
                context['code']=status.HTTP_200_OK     
                              
                return JsonResponse(context, status = 200) 

        else:
                         
            context['status'] = 'Error'
            context['message'] = 'Invalid credentials'
            context['message2'] = 'Kindly Try Again With A Valid Email And Password'
            context['code']=status.HTTP_401_UNAUTHORIZED           
            return JsonResponse(context, status = 200)

    return JsonResponse({}, status = 200)

# @receiver(user_logged_out, sender=User)
# def update_login_time(sender, request, user,**kwargs):
#     user_id=request.user.staff_id#Get Cuurent User Staff Id
#     staff_id= User.objects.all().get(staff_id=user_id)#Convert This to A User Object
#     new_time=staff_id.last_login  
   
#     User.objects.filter(pk=staff_id.pk).update(my_last_login=new_time)
    

@login_required
def home(request):
    user_id=request.user.id_numb#Get Cuurent User Staff Id        
    questions=Questions.objects.filter(pk=23)    
    return render(request, 'authenticate/home.html', {})
def signup(request):    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # user=form.cleaned_data['staff_id']          
            user = form.cleaned_data['id_numb']  
            NO_ID_MSG="Sorry, We couldn't Find the User ID {} On Our Database, \
Please contact your staff adviser".format(user).title()

            acct_created_msg='User Account Created,Kindly \
Note That You Must Verify Your Email To Log In'
            
            user_details=User_Info.objects.all().filter(id_numb=user)
           
            if (user_details.exists())==False:
                sweetify.error(request, 'User Details Not Found!', button='Ok', persistent=True,\
                text=NO_ID_MSG)
                                
                form = CustomUserCreationForm(request.POST)
            else: 
                userDb_details=User_Info.objects.get(id_numb=user)   

                first_name=userDb_details.first_name
                middle_name=userDb_details.middle_name
                last_name=userDb_details.last_name
                email=userDb_details.email
                display_name='{} {}'.format(userDb_details.first_name,userDb_details.last_name)
                        
                instance=form.save()
                new_user=User.objects.get(id_numb=instance.id_numb)
                User.objects.filter(pk=new_user.pk).update(
                first_name=first_name,middle_name=middle_name,last_name=last_name,\
                email=email,display_name=display_name) 
                # sweetify.info(request, 'Success!', button='Ok', persistent=True, text=acct_created_msg,)     
                
                current_site = get_current_site(request)
                mail_subject = 'Activate Your Account On NACOSS'
                message = render_to_string('registration/account_activation_email.html', {
                    'user': display_name,
                    'domain': current_site.domain,
                    'uid': new_user.pk,
                    'token': account_activation_token.make_token(instance)
                })
                to_email = email
                to_list = [to_email]
                from_email = settings.EMAIL_HOST_USER
                
                send_mail(mail_subject, message, from_email, to_list, fail_silently=True)
                 
                return redirect('activation_sent')
 
    else:
        form = CustomUserCreationForm()
 
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            Log_msg="Successfully Changed Password"
           
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password_change_done')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change_form.html', {
        'form': form
    })


def account_activation_sent(request):   
    return render(request, 'registration/account_activation_sent.html', {})

def activate(request, uid, token):
    try:
        user = User.objects.get(pk=uid)
        
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        Log_msg="Activated Account For {}".format(user)
       
        return render(request, 'registration/account_activation_done.html', {})        
      
    else:
        return render(request,'registration/account_activation_failed.html',{})