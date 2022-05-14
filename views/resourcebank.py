from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from resourcebank.forms import QuestionsForm,EditQuestionsForm
from resourcebank.models import Answers, Questions
from authenticate.models import User,User_Info
from django.contrib import messages
import sweetify
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import status


@login_required
def questions(request): 
    user_email=request.user.email
    user=User.objects.get(email=user_email)
    # user_info=User_Info.objects.get(email=user_email)
    # print(user)
    form = QuestionsForm(request.POST)
    if request.method == 'POST':
        
        form = QuestionsForm(request.POST)
        if form.is_valid():  
            instance=form.save(commit=False)
            instance.author=user        
            # description = form.cleaned_data['description']
            sweetify.info(request, 'Success!', button='Ok', persistent=True, text='Successfully saved your question',)
            instance.save()
            return redirect('my_questions')
       
    return render(request, 'main_bank/questions.html', {'form':form})
  

@login_required
def my_questions(request): 
    user_id=request.user.pk
    questions= Questions.objects.filter(author=user_id)
    # for question in questions:
    #     print('{}-{}'.format(question.pk,question.description))
    return render(request, 'main_bank/my_questions.html', {'questions':questions})


@login_required
def edit_my_questions(request,pk): 
    user_email=request.user.email
    # user=User.objects.get(email=user_email)
    # user_info=User_Info.objects.get(email=user_email)
    questions=Questions.objects.get(pk=pk)
    my_questions=Questions.objects.filter(pk=pk)
    form=EditQuestionsForm(request.POST or None,instance=questions)
    if request.method == 'POST':
        form=EditQuestionsForm(request.POST or None,instance=questions)
        if form.is_valid():

            form.save()
            return redirect('my_questions')
        else:
            print(form.errors)
    else:
        form=EditQuestionsForm(request.POST or None,instance=questions)
    return render(request, 'main_bank/edit_my_questions.html', {'form':form})




@login_required
def delete_my_post(request):
    user_email=request.user.email
    user=User.objects.get(email=user_email)
    if request.is_ajax and request.method == "POST":
        # context = {}
        question_pk = request.POST['pk']
        Questions.objects.filter(pk=question_pk).delete()
        # print(question_pk)
        # password = request.POST['password']
        
        # account = authenticate(request,username=email, password=password)
    return HttpResponse()

@login_required
def search_result(request):
    if request.is_ajax and request.method == "GET":
        # context = {}
        search_input = request.GET['id_searchbox']
        print(search_input)
        # print(question_pk)
        # password = request.POST['password']
        
        # account = authenticate(request,username=email, password=password)
    return HttpResponse()


# def search_questions(request):
#     user_email=request.user.email
#     user=User.objects.get(email=user_email)
#     if request.is_ajax and request.method == "GET":
       
#         question = request.GET.get('Question')
#         print(question)
       
#     return HttpResponse()

@login_required
def search_questions(request):  
    
    if request.is_ajax and request.method == "GET":        
        # state_id= int(request.GET.get('State_ID'))
        question = request.GET.get('Question').rstrip()
        questions_data=[]        
        question_details=Questions.objects.all().filter(description__icontains=question)

        for sNo,questions in enumerate(question_details,1):
            question_details={'pk':questions.pk,'description':questions.description.title(),\
                'serial_no':sNo, 'created_on':questions.created_on, 'updated_on':questions.updated_on,'author':questions.author.first_name,'code':status.HTTP_200_OK}  

            questions_data.append(question_details) 
        
        return JsonResponse(data=questions_data,safe=False)         
       
    return JsonResponse({"valid":False}, status = 200)   


def answers(request,pk):
    answers=Answers.objects.filter(question=pk)
    print(answers)
   
    return render(request, 'main_bank/view_answers.html',{'answers':answers})
