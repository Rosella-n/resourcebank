from django.urls import path,include
import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
urlpatterns=[
    path('questions/',views.questions, name='questions'),
    path('my_questions/',views.my_questions, name='my_questions'),
    path('testsave/',views.testsave, name='testsave'),
    path('upload_file/',views.upload_file, name='upload_file'),
    path('download_file/',views.download_file, name='download_file'),
    url(r'^download_file/(?P<path>.*)$',serve, {'document_root':settings.MEDIA_ROOT}),
    path('edit_questions/<int:pk>/',views.edit_my_questions, name='edit_questions'),
    path('answers/<int:pk>/',views.answers,name="answers"),
    path('display_answers/<int:pk>/',views.display_answers,name="display_answers"),
    path('post/ajax/deletemypost',views.delete_my_post, name='deletemypost'),
    path('post/ajax/rateanswer',views.rate_answer, name='rateanswer'),
    path('get/ajax/check_ratingstatus',views.check_user_ratingstatus, name='check_ratingstatus'),
    path('get/ajax/search',views.search_result, name='search'),
    path('get/ajax/get_answer',views.get_answer, name='get_answer'),
    path('get/ajax/get_search_results',views.search_questions,name='get_search_results'),
]


if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)