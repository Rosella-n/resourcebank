from django.contrib import admin
from resourcebank.models import *
# Register your models here.
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('description','created_on','updated_on','author','file',)
    list_per_page = 30
admin.site.register(Questions,QuestionsAdmin)

class AnswersAdmin(admin.ModelAdmin):
    list_display = ('pk','answer','created_on','updated_on','author','file')
    list_per_page = 30
admin.site.register(Answers,AnswersAdmin)

class QuestionRatingAdmin(admin.ModelAdmin):
    list_display = ('question','user','rated_on','rating','no_of_views')
    list_per_page = 30
admin.site.register(QuestionRating,QuestionRatingAdmin)


class AnswerRatingAdmin(admin.ModelAdmin):
    list_display = ('answer','user','rated_on','rating','no_of_views')
    list_per_page = 30
admin.site.register(AnswerRating,AnswerRatingAdmin)

class TestsaveAdmin(admin.ModelAdmin):
    list_display = ('suggestion','add_file')
    list_per_page = 30
admin.site.register(Testsave,TestsaveAdmin)

class UploadFileAdmin(admin.ModelAdmin):
    list_display = ('title','add_file')
    list_per_page = 30
admin.site.register(UploadFile,UploadFileAdmin)

