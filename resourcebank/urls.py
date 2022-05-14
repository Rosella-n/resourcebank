from django.urls import path,include
import views

urlpatterns=[
    path('questions/',views.questions, name='questions'),
    path('my_questions/',views.my_questions, name='my_questions'),
    path('edit_questions/<int:pk>/',views.edit_my_questions, name='edit_questions'),
    path('answers/<int:pk>/',views.answers,name="answers"),
    path('post/ajax/deletemypost',views.delete_my_post, name='deletemypost'),
    path('get/ajax/search',views.search_result, name='search'),
    path('get/ajax/get_search_results',views.search_questions,name='get_search_results'),
]