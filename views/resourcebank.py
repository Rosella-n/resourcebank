from multiprocessing import context
from urllib.request import Request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from resourcebank.forms import QuestionsForm,EditQuestionsForm, AnswerForm, TestsaveForm
from resourcebank.models import Answers, Questions,AnswerRating,QuestionRating
from authenticate.models import User,User_Info
from django.contrib import messages
import sweetify
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import status
from django.db.models import Q,Avg, Count, Min, Sum

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

# @login_required
# def answers(request,pk):
#     user_email=request.user.email
#     user=User.objects.get(email=user_email)

#     answers=Answers.objects.filter(question=pk)
#     # print(answers)
#     questions=Questions.objects.filter(pk=pk)
#     question=Questions.objects.get(pk=pk)
#     form = AnswerForm(request.POST or None,instance=question)
#     if request.method == 'POST':
        
#         form = AnswerForm(request.POST or None, request.FILES,instance=question)
#         if form.is_valid():
            
#             # instance=form.save(commit=False)
#             # instance.author=user        
#             # instance.question=question
#             # instance.okoiiiiiii="My Name is Rose"

           
#             # instance.save()
#             form.save()
#             sweetify.info(request, 'Success!', button='Ok', persistent=True, text='Successfully saved your Answer',) 

#         else:
#             form = AnswerForm()
#             return  form.errors

#     return render(request, 'main_bank/view_answers.html',{'questions':questions, 'answers':answers, 'form':form})

@login_required
def get_answer(request):  
    if request.is_ajax and request.method == "GET":   
        question_pk = request.GET.get('Question')
        dropdown =  request.GET.get('Dropdown')
        if dropdown=="1":
                answer_details=Answers.objects.filter(question__pk=question_pk)\
                    .order_by('rating')
        elif  dropdown=="2":
                answer_details=Answers.objects.filter(question__pk=question_pk)\
                    .order_by('-rating')
        elif  dropdown=="3":
                answer_details=Answers.objects.filter(question__pk=question_pk)\
                    .order_by('created_on')
        elif  dropdown=="4":
                answer_details=Answers.objects.filter(question__pk=question_pk)\
                    .order_by('-created_on')
        else:
                answer_details=Answers.objects.filter(question__pk=question_pk)
        answer_data=[]
        # dropdown =  request.GET.get('Dropdown')
        # question_details=Answers.objects.filter(Q('question.pk'=answer))
        # answer_details=Answers.objects.filter(question__pk=question_pk)
        for sNo,answers in enumerate(answer_details,1):
                answer_details={'pk':answers.pk,'description':answers.answer.title(),\
                    'serial_no':sNo, 'created_on':answers.created_on, 'updated_on':answers.updated_on,'author':answers.author.first_name,'code':status.HTTP_200_OK}  

                answer_data.append(answer_details) 
        return JsonResponse(data=answer_data,safe=False)
            
       
    return JsonResponse({"valid":False}, status = 200) 

@login_required
def check_user_ratingstatus(request):
    user_id = request.user.pk
    user=User.objects.get(pk=user_id)
    if request.is_ajax and request.method == "GET":

        answer_id=int(request.GET.get('Answer_ID'))
        
       
        # Queue=Task_Queues.objects.get(pk=answer_id)
        # if QueueAccess.objects.filter(access_for=user,task_queue_code\
        #     =Queue).exists():
        if AnswerRating.objects.filter(user=user,answer=answer_id).exists():
            # if Queue Access Object found return not valid
            print('false')
            return JsonResponse({"valid":False}, status = 200)
           
        else:
            # if  not found, then we can Add Access To That Task Queue.
            print('true')
            return JsonResponse({"valid":True}, status = 200)

    return JsonResponse({}, status = 400)


@login_required    
def rate_answer(request):
    user_id = request.user.pk
    user=User.objects.get(pk=user_id) 
    if request.is_ajax and request.method == "POST":
        answer_id=int(request.POST['Answer_ID'])
        rating=int(request.POST['Rating'])
        answer=AnswerRating.objects.get(answer=answer_id)
        current_rating=answer.rating
        num_views= answer.no_of_views
        rating=int(rating*20)
        new_num_views=num_views+1
        new_rating=rating+current_rating/new_num_views
        new_rating=int(new_rating/20)
        AnswerRating.objects.filter(answer=answer_id).update(rating=new_rating,no_of_views=new_num_views)
        print( current_rating)
        print(rating)
        print(num_views)
    return HttpResponse()


def testsave(request):
    user_email=request.user.email
    user=User.objects.get(email=user_email)
    # user_info=User_Info.objects.get(email=user_email)
    # print(user)
    form = TestsaveForm(request.POST or None,request.FILES)
    if request.method == 'POST':
        
        form = TestsaveForm(request.POST or None,request.FILES)
        if form.is_valid():  
            form.save()
            sweetify.info(request, 'Success!', button='Ok', persistent=True, text='Successfully saved your question',)
            
        else:
            form = TestsaveForm()
       
    return render(request, 'main_bank/testsave.html', {'form':form})



# rating
#  no_of_views
# Answer_ID
# Rating


@login_required
def answers(request,pk):
    user_email=request.user.email
    user=User.objects.get(email=user_email)
   
    answers=Answers.objects.filter(question=pk)
    
    questions=Questions.objects.filter(pk=pk)
    question=Questions.objects.get(pk=pk)
    form = AnswerForm(request.POST or None,)
    
    if request.method == 'POST':
        
        form = AnswerForm(request.POST or None,request.FILES)
        if form.is_valid():
            
            instance=form.save(commit=False)
            instance.author=user
            instance.question=question
            form.save()
            sweetify.info(request, 'Success!', button='Ok', persistent=True, text='Successfully saved your Answer',) 



        else:
            form = AnswerForm()
            return  form.errors


    return render(request, 'main_bank/view_answers.html',{'questions':questions, 'answers':answers, 'form':form})


def display_answers(request,pk): 
    
    answers= Answers.objects.filter(pk=pk)
    return render(request, 'main_bank/display_answers.html', {'answers':answers})